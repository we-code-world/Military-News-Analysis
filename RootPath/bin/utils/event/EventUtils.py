# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: EventUtils.py
@time: 2021/8/20 21:18
"""
import copy
from utils.file.xlsx import writeXls
from utils.file.path import getPathListBySuffix
from utils.format.TimeFormat import doTimeFormat

event_classes = []
event_class_triggers = {}
all_event_triggers = []
event_items = {}
location_list = []
weapon_list = []
country_list = []
location_replace = []
weapon_replace = []
country_replace = []
unknown_trigger_file = ""
my_tmp_events_after_merge = []


def createAllItemsList(opt):
    global unknown_trigger_file
    class_files = getPathListBySuffix(opt.ResPath + "/format/trigger/classes", "txt")
    for class_file in class_files:
        class_name = class_file.split("/")[-1].split(".")[0]
        event_class_triggers[class_name] = []
        file_open = open(class_file, "r", encoding="utf-8")
        trigger_lines = file_open.readlines()
        file_open.close()
        event_classes.append(class_name)
        if class_name == "unknown":
            unknown_trigger_file = open(class_file, "a", encoding="utf-8")
        for trigger_line in trigger_lines:
            triggers = trigger_line.strip()
            if triggers == "":
                continue
            trigger_list = triggers.split(" ")
            for trigger in trigger_list:
                all_event_triggers.append(trigger)
            event_class_triggers[class_name].append(trigger_list)
    location_file = open(opt.ResPath + "/format/location/Location.txt", "r", encoding="utf-8")
    read_location = location_file.readlines()
    location_file.close()
    for line in read_location:
        location_items = line.strip()
        location_list.append(location_items)
    location_list.sort(key=lambda x: len(x))
    weapon_file = open(opt.ResPath + "/format/weapon/Weapon.txt", "r", encoding="utf-8")
    read_weapon = weapon_file.readlines()
    weapon_file.close()
    for line in read_weapon:
        weapon_items = line.strip()
        weapon_list.append(weapon_items)
    weapon_list.sort(key=lambda x: len(x))
    country_file = open(opt.ResPath + "/format/country/Country.txt", "r", encoding="utf-8")
    read_country = country_file.readlines()
    country_file.close()
    for line in read_country:
        country_items = line.strip()
        country_list.append(country_items)
    country_list.sort(key=lambda x: len(x))
    location_replace_file = open(opt.ResPath + "/format/location/replace.txt", "r", encoding="utf-8")
    read_replace_location = location_replace_file.readlines()
    location_replace_file.close()
    for line in read_replace_location:
        location_items = line.strip().split(" ")
        if len(location_items) == 1:
            replace_item = ""
        elif len(location_items) > 1:
            replace_item = location_items[1]
        else:
            continue
        source_item = location_items[0]
        location_replace.append((source_item, replace_item))
    weapon_replace_file = open(opt.ResPath + "/format/weapon/replace.txt", "r", encoding="utf-8")
    read_replace_weapon = weapon_replace_file.readlines()
    weapon_replace_file.close()
    for line in read_replace_weapon:
        weapon_items = line.strip().split(" ")
        if len(weapon_items) == 1:
            replace_item = ""
        elif len(weapon_items) > 1:
            replace_item = weapon_items[1]
        else:
            continue
        source_item = weapon_items[0]
        weapon_replace.append((source_item, replace_item))
    country_replace_file = open(opt.ResPath + "/format/country/replace.txt", "r", encoding="utf-8")
    read_replace_country = country_replace_file.readlines()
    country_replace_file.close()
    for line in read_replace_country:
        country_items = line.strip().split(" ")
        if len(country_items) == 1:
            replace_item = ""
        elif len(country_items) > 1:
            replace_item = country_items[1]
        else:
            continue
        source_item = country_items[0]
        country_replace.append((source_item, replace_item))


def getEventClassList():
    return event_classes


def getTriggerList(event_class):
    return event_class_triggers[event_class]


def addTrigger(trigger):
    global all_event_triggers
    all_event_triggers.append(trigger)
    event_class_triggers["unknown"].append(trigger)


def getUnknownFile():
    return unknown_trigger_file


def getAllTriggers():
    return all_event_triggers


def closeUnknownFile():
    global unknown_trigger_file
    unknown_trigger_file.close()


def createEventItems(opt):
    class_items_file = open(opt.ResPath + "/format/trigger/Classes.txt", "r", encoding="utf-8")
    read_lines = class_items_file.readlines()
    for read_line in read_lines:
        event_name_items = read_line.strip().split("-->")
        event_items[event_name_items[0]] = event_name_items[1].split(" ")


def getTimeDict(texts, time="2020-12-31 15:18"):
    time_dict = {}
    for text in texts:
        format_start_time, format_end_time = doTimeFormat(text, time)
        format_time = format_start_time + "[cut]" + format_end_time
        if format_time == "[cut]":
            time_dict[text] = text
        else:
            time_dict[text] = format_time
    return time_dict


def getTmpEvents():
    return my_tmp_events_after_merge


def cleanTmpEvents():
    global my_tmp_events_after_merge
    my_tmp_events_after_merge = []


def getStandardDict(texts, item_list, item_replace, freq=1):
    replace_dict = {}
    tmp_dict = {}
    texts_after_replace = []
    for text in texts:
        add_text = text
        for source_item, replace_item in item_replace:
            add_text = add_text.replace(source_item, replace_item)
        texts_after_replace.append(add_text)
        replace_dict[text] = add_text
    text_list = {x for x in texts_after_replace}
    rtn_text_list = []
    texts_sort = []
    for text in text_list:
        number = texts.count(text)
        texts_sort.append((text, number))
        if number <= freq:
            continue
        rtn_text_list.append((text, number))
    texts_sort.sort(key=lambda x: x[1])
    rtn_text_list.sort(key=lambda x: x[1], reverse=True)
    for text, number in texts_sort:
        tmp_dict[text] = text
        addSign = True
        for high_text, high_number in rtn_text_list:
            if (text in high_text) and (number <= high_number):
                tmp_dict[text] = high_text
                addSign = False
                break
        if addSign:
            for item in item_list:
                if text in item:
                    tmp_dict[text] = item
                    break
    return replace_dict, tmp_dict


def getLocationDict(texts):
    location_dict = {}
    text_list = {x for x in texts}
    replace_location_dict, tmp_location_dict = getStandardDict(texts, location_list, location_replace)
    for text in text_list:
        location_dict[text] = tmp_location_dict[replace_location_dict[text]]
    return location_dict


def getWeaponDict(texts, country_dict, weapon_country):
    weapon_dict = {}
    weapon_country_dict = {}
    text_list = {x for x in texts}
    replace_weapon_dict, tmp_weapon_dict = getStandardDict(texts, weapon_list, weapon_replace)
    for text in text_list:
        weapon_dict[text] = tmp_weapon_dict[replace_weapon_dict[text]]
    weapons, countries = weapon_country["weapon"], weapon_country["country"]
    format_weapon_distance = {}
    for text in text_list:
        format_weapon = weapon_dict[text]
        format_weapon_distance[format_weapon] = 999
        weapon_country_dict[format_weapon] = ""
    for weaponList, countryList in zip(weapons, countries):
        for seq_index, weapon in weaponList:
            weapon_start = weapon["offset"]
            weapon_end = weapon_start + weapon["length"]
            format_weapon_text = weapon_dict[weapon["text"]]
            min_distance = format_weapon_distance[format_weapon_text]
            for seq_index_, country in countryList:
                country_start = country["offset"]
                country_end = country_start + country["length"]
                format_country_text = country_dict[country["text"]]
                distance = 999
                if country_end <= weapon_start:
                    distance = weapon_start - country_end
                elif country_start >= weapon_end:
                    distance = country_start - weapon_end
                if (distance < min_distance) and ("[split]" not in format_country_text):
                    weapon_country_dict[format_weapon_text] = format_country_text
                    format_weapon_distance[format_weapon_text] = distance
                    min_distance = distance
    for text in text_list:
        weapon_dict[text] = weapon_country_dict[weapon_dict[text]] + "[cut]" \
                            + str(format_weapon_distance[weapon_dict[text]]) + "[cut]" + weapon_dict[text]
    return weapon_dict


def getCountryDict(texts):
    country_dict = {}
    text_list = {x for x in texts}
    replace_country_dict, tmp_country_dict = getStandardDict(texts, country_list, country_replace)
    for text in text_list:
        country_dict[text] = tmp_country_dict[replace_country_dict[text]]
    return country_dict


def mergeEventItems(event):
    rtn_event = copy.deepcopy(event)
    items_keys = ["time", "location", "weapon", "country"]
    rtn_items = {}
    items = event["items"]
    for key in items_keys:
        key_items = items[key]
        key_rtn_items = copy.deepcopy(key_items)
        first_items = key_items["first"]
        second_items = key_items["second"]
        rtn_first_items = []
        check_sign = [1] * len(first_items)
        check_second_sign = [1] * len(second_items)
        for item_index, first_item in enumerate(first_items):
            if check_sign[item_index] == 0:
                continue
            check_sign[item_index] = 0
            key_item, item_number = first_item
            check_item = key_item.replace("‘", "").replace("’", "").replace("“", "").replace("”", "")
            for other_item_index, first_other_item in enumerate(first_items):
                if item_index == other_item_index:
                    continue
                key_other_item, other_item_number = first_other_item
                check_other_item = key_other_item.replace("‘", "").replace("’", "").replace("“", "").replace("”", "")
                if check_item in check_other_item:
                    item_number += other_item_number
                    check_item = check_other_item
                    check_sign[other_item_index] = 0
                elif check_other_item in check_item:
                    item_number += other_item_number
                    check_sign[other_item_index] = 0
            for other_item_index, second_other_item in enumerate(second_items):
                if check_second_sign[other_item_index] == 0:
                    continue
                key_other_item, other_item_number = second_other_item
                check_other_item = key_other_item.replace("‘", "").replace("’", "").replace("“", "").replace("”", "")
                if check_item in check_other_item:
                    item_number += other_item_number
                    check_item = check_other_item
                    check_second_sign[other_item_index] = 0
                elif check_other_item in check_item:
                    item_number += other_item_number
                    check_second_sign[other_item_index] = 0
            rtn_first_items.append((check_item, item_number))
        rtn_second_items = []
        for other_item_index, second_other_item in enumerate(second_items):
            if check_second_sign[other_item_index] == 0:
                continue
            rtn_second_items.append(second_other_item)
        key_rtn_items["first"] = rtn_first_items
        key_rtn_items["second"] = rtn_second_items
        rtn_items[key] = key_rtn_items
    return rtn_event


def cleanEvents(events, number=2, check_weapon=False):
    rtn_events = []
    items_keys = ["time", "location", "weapon", "country"]
    for event in events:
        items_number = 0
        items = event["items"]
        for key in items_keys:
            role = items[key]
            if len(role["first"]) > 0:
                items_number += 1
            elif check_weapon and (key == "weapon"):
                break
        if items_number >= number:
            rtn_events.append(event)
    return rtn_events


def fuseItem(items_a, items_b):
    items = copy.deepcopy(items_a)
    for item_b in items_b:
        addSign = True
        for item in items:
            if item in items_b:
                items.remove(item)
                items.append(item_b)
                addSign = False
                break
            elif item_b in item:
                addSign = False
                break
        if addSign:
            items.append(item_b)
    return items


def mergeEvents(events):
    rtn_events = []
    tmp_events = []
    items_keys = ["time", "location", "weapon", "country"]
    for event in events:
        addSign = True
        items = event["items"]
        for key in items_keys:
            role = items[key]
            if len(role["first"]) == 0:
                addSign = False
                break
        if addSign:
            tmp_events.append(event)
    tmp_events_sign = [1] * len(tmp_events)
    for event_index, event in enumerate(tmp_events):
        if tmp_events_sign[event_index] == 0:
            continue
        rtn_event = copy.deepcopy(event)
        items = rtn_event["items"]
        times = items["time"]["first"]
        locations = items["location"]
        weapons = items["weapon"]
        countries = items["country"]
        tmp_events_sign[event_index] = 0
        for other_event_index, other_event in enumerate(tmp_events):
            if tmp_events_sign[other_event_index] == 1:
                other_items = other_event["items"]
                other_times = other_items["time"]["first"]
                format_time = times[0][0]
                format_other_time = other_times[0][0]
                if format_time != format_other_time:
                    continue
                tmp_events_sign[other_event_index] = 0
                locations["first"] += other_items["location"]["first"]
                weapons["first"] += other_items["weapon"]["first"]
                countries["first"] += other_items["country"]["first"]
                locations["second"] += other_items["location"]["second"]
                weapons["second"] += other_items["weapon"]["second"]
                countries["second"] += other_items["country"]["second"]
        rtn_items = {"time": times, "location": locations, "weapon": weapons, "country": countries}
        rtn_event["items"] = rtn_items
        rtn_events.append(rtn_event)
    return rtn_events


def getEventItems(event):
    result_event = {"eventClass": "", "startTime": "", "endTime": "", "eventLocations": [], "eventTriggers": [],
                    "relateWeapons": [], "subjectCountries": [], "objectCountries": [], "eventStatus": event["tense"],
                    "eventPolarity": event["polarity"], "newsPos": ""}
    result_event["eventTriggers"].append(event["trigger"]["text"])
    check_event_items = event["items"]
    result_time = check_event_items["time"][0][0].split("[cut]")
    if len(result_time) != 2:
        return result_event
    result_event["startTime"] = result_time[0]
    result_event["endTime"] = result_time[1]
    result_locations_all = check_event_items["location"]
    result_locations_first = result_locations_all["first"]
    result_locations_second = result_locations_all["second"]
    result_locations_list = result_locations_first
    result_locations = result_locations_first + result_locations_second
    if len(result_locations_first) == 0:
        result_locations_list = result_locations_second
    for result_location in result_locations_list:
        format_location = result_location[0]
        for location_, unused_number in result_locations:
            if location_ in format_location:
                format_location = location_
        if format_location not in result_event["eventLocations"]:
            result_event["eventLocations"].append(format_location)
    result_weapon_all = check_event_items["weapon"]
    result_weapon_first = result_weapon_all["first"]
    result_weapon_second = result_weapon_all["second"]
    result_weapons = result_weapon_first + result_weapon_second
    result_weapon_list = result_weapon_first
    if len(result_weapon_first) == 0:
        result_weapon_list = [result_weapon_second[0]]
    for result_weapon, unused_num in result_weapon_list:
        format_country_weapon = result_weapon.split("[cut]")
        format_country = format_country_weapon[0]
        format_country_distance = format_country_weapon[1]
        format_weapons = format_country_weapon[2].split("[split]")
        for weapon__, unused_number in result_weapons:
            if weapon__ == result_weapon:
                continue
            inner_country_weapon = weapon__.split("[cut]")
            inner_country = inner_country_weapon[0]
            inner_country_distance = inner_country_weapon[1]
            inner_weapons = inner_country_weapon[2].split("[split]")
            for format_weapon in format_weapons:
                for inner_weapon in inner_weapons:
                    if format_weapon in inner_weapon:
                        format_weapon = inner_weapon
                        if inner_country_distance < format_country_distance:
                            format_country = inner_country
                            format_country_distance = inner_country_distance
                if format_weapon not in result_event["relateWeapons"]:
                    result_event["relateWeapons"].append(format_weapon)
        if format_country not in result_event["subjectCountries"]:
            result_event["subjectCountries"].append(format_country)
    result_country_all = check_event_items["country"]
    result_country_first = result_country_all["first"]
    result_country_second = result_country_all["second"]
    result_countries = result_country_first + result_country_second
    result_country_list = result_country_first
    if len(result_country_first) == 0:
        result_country_list = [result_country_second[0]]
    for result_country, unused_num in result_country_list:
        objectSign = False
        if "[object]" in result_country:
            objectSign = True
            result_country = result_country.split("[object]")[0]
        format_countries = result_country.split("[split]")
        for country_, unused_number in result_countries:
            if country_ == result_country:
                continue
            inner_countries = country_.split("[object]")[0].split("[split]")
            for format_country in format_countries:
                for inner_country in inner_countries:
                    if format_country in inner_country:
                        format_country = inner_country
                if format_country not in result_event["subjectCountries"]:
                    if format_country not in result_event["objectCountries"]:
                        if objectSign:
                            result_event["objectCountries"].append(format_country)
                        else:
                            result_event["subjectCountries"].append(format_country)
    return result_event


def ComplementByEachOther(events, event_class):
    events_result = []
    tmp_events = []
    events = cleanEvents(events)
    if len(events) == 0:
        return []
    items_keys = ["time", "location", "weapon", "country"]
    for event in events:
        items = event["items"]
        for key in items_keys:
            role = items[key]
            if len(role["first"]) > 0:
                continue
            max_len = 0
            for other_event in events:
                other_role_key_first = other_event["items"][key]["first"]
                role_list_len = len(other_role_key_first)
                if (role_list_len > 0) and (role_list_len > max_len):
                    max_len = max(len(other_role_key_first), max_len)
                    role["first"] = other_role_key_first
            items[key] = role
        event["items"] = items
        tmp_events.append(event)
    tmp_events = cleanEvents(tmp_events, number=3, check_weapon=True)
    if len(tmp_events) == 0:
        return []
    tmp_events_result = mergeEvents(tmp_events)
    global my_tmp_events_after_merge
    my_tmp_events_after_merge += copy.deepcopy(tmp_events_result)
    for tmp_event in tmp_events_result:
        result_event = getEventItems(tmp_event)
        result_event["eventClass"] = event_class
        if result_event["startTime"] == "":
            continue
        events_result.append(result_event)
    return events_result
