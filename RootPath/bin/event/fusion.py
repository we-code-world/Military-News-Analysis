# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: fusion.py
@time: 2021/9/13 19:14
"""
import copy
import json
from utils.file.xlsx import createXls, writeXls
from utils.database.connect import getConn, delConn
from utils.event.EventFormat import formatTime, formatLoc, formatWeapon, formatCountry
from utils.event.EventUtils import createAllItemsList, getTriggerList, createEventItems, getEventClassList, \
    ComplementByEachOther, getTimeDict, getLocationDict, getWeaponDict, getCountryDict, getUnknownFile, \
    closeUnknownFile, getAllTriggers, addTrigger, getTmpEvents, cleanTmpEvents
from utils.file.path import getPathListBySuffix


# 返回格式为（事件:触发词、主体、客体、句子编号、备选集）
def getEvent(texts):
    events = []

    all_times = []
    all_locations = []
    all_weapons = []
    all_countries = []
    all_texts = []

    time_items = []
    location_items = []
    weapon_items = []
    country_items = []

    max_index = len(texts) - 1
    less_sentences = set(range(0, max_index + 1))

    for index, example in enumerate(texts):
        arguments = example["arguments"]
        times = arguments["time"]
        locations = arguments["loc"]
        weapons = arguments["weapon"]
        countries = arguments["country"]

        inner_times = []
        inner_locations = []
        inner_weapons = []
        inner_countries = []

        inner_text = []

        for role in times:
            inner_times.append((index, role))
            time_items.append(role["text"])
        for role in locations:
            inner_locations.append((index, role))
            location_items.append(role["text"])
        for role in weapons:
            inner_weapons.append((index, role))
            weapon_items.append(role["text"])
        for role in countries:
            inner_countries.append((index, role))
            country_items.append(role["text"])
        inner_text += time_items
        inner_text += location_items
        inner_text += weapon_items
        inner_text += country_items
        all_times.append(inner_times)
        all_locations.append(inner_locations)
        all_weapons.append(inner_weapons)
        all_countries.append(inner_countries)
        all_texts.append(inner_text)
    weapon_country = {"weapon": all_weapons, "country": all_countries}
    all_items_text = {"time": time_items, "location": location_items, "weapon": weapon_items, "country": country_items}

    for index, example in enumerate(texts):
        sentence = example["sentence"]
        trigger_events = example["events"]
        trigger_arguments = example["arguments"]
        times = trigger_arguments["time"]
        locations = trigger_arguments["loc"]
        weapons = trigger_arguments["weapon"]
        countries = trigger_arguments["country"]

        for trigger_event in trigger_events:
            event_item = {}
            items = {}
            item_for_times = {}
            item_for_locations = {}
            item_for_weapons = {}
            item_for_countries = {}

            inner_times = []
            inner_locations = []
            inner_weapons = []
            inner_countries = []

            inner_list = []

            inner_times_add = []
            inner_locations_add = []
            inner_weapons_add = []
            inner_countries_add = []

            less_times = []
            less_locations = []
            less_weapons = []
            less_countries = []

            less_list = []

            less_times_add = []
            less_locations_add = []
            less_weapons_add = []
            less_countries_add = []

            last_times = []
            last_locations = []
            last_weapons = []
            last_countries = []

            next_times = []
            next_locations = []
            next_weapons = []
            next_countries = []

            event_trigger = trigger_event["trigger"]
            event_subject = trigger_event["subject"]
            event_object = trigger_event["object"]
            event_polarity = copy.deepcopy(trigger_event["labels"]["polarity"])
            event_tense = copy.deepcopy(trigger_event["labels"]["tense"])
            subject_text = event_subject["text"]
            object_text = event_object["text"]

            all_event_triggers = getAllTriggers()
            unknown_trigger_file = getUnknownFile()
            if event_trigger["text"] not in all_event_triggers:
                unknown_trigger_file.write(event_trigger["text"] + "\n")
                addTrigger(event_trigger["text"])

            for role in times:
                role_text = role["text"]
                if (role_text in subject_text) or (role_text in object_text):
                    inner_times.append((index, role))
                    inner_list.append(role_text)
                else:
                    less_times.append((index, role))
                    less_list.append(role_text)
            for role in locations:
                role_text = role["text"]
                if (role_text in subject_text) or (role_text in object_text):
                    inner_locations.append((index, role))
                    inner_list.append(role_text)
                else:
                    less_locations.append((index, role))
                    less_list.append(role_text)
            for role in weapons:
                role_text = role["text"]
                if (role_text in subject_text) or (role_text in object_text):
                    inner_weapons.append((index, role))
                    inner_list.append(role_text)
                else:
                    less_weapons.append((index, role))
                    less_list.append(role_text)
            for role in countries:
                role_text = role["text"]
                if (role_text in subject_text) or (role_text in object_text):
                    inner_countries.append((index, role))
                    inner_list.append(role_text)
                else:
                    less_countries.append((index, role))
                    less_list.append(role_text)

            less_sentences.discard(index)

            if index == 0:
                next_times = all_times[1]
                next_locations = all_locations[1]
                next_weapons = all_weapons[1]
                next_countries = all_countries[1]
                less_sentences.discard(1)

            elif index == max_index:
                last_times = all_times[index - 1]
                last_locations = all_locations[index - 1]
                last_weapons = all_weapons[index - 1]
                last_countries = all_countries[index - 1]
                less_sentences.discard(index - 1)

            else:
                last_times = all_times[index - 1]
                next_times = all_times[index + 1]
                last_locations = all_locations[index - 1]
                next_locations = all_locations[index + 1]
                last_weapons = all_weapons[index - 1]
                next_weapons = all_weapons[index + 1]
                last_countries = all_countries[index - 1]
                next_countries = all_countries[index + 1]
                less_sentences.discard(index - 1)
                less_sentences.discard(index + 1)

            for seq_index, text in enumerate(all_texts):
                if seq_index in [index - 1, index, index + 1]:
                    continue

                inner_sign = False
                for inner_text in inner_list:
                    if inner_text in text:
                        inner_times_add += all_times[seq_index]
                        inner_locations_add += all_locations[seq_index]
                        inner_weapons_add += all_weapons[seq_index]
                        inner_countries_add += all_countries[seq_index]
                        inner_sign = True
                        break
                if inner_sign:
                    less_sentences.discard(seq_index)
                    continue

                for less_text in less_list:
                    if less_text in text:
                        less_times_add += all_times[seq_index]
                        less_locations_add += all_locations[seq_index]
                        less_weapons_add += all_weapons[seq_index]
                        less_countries_add += all_countries[seq_index]
                        less_sentences.discard(seq_index)
                        break

            item_for_times["inner"] = inner_times
            item_for_times["less"] = less_times
            item_for_times["last"] = last_times
            item_for_times["next"] = next_times
            item_for_times["inner_add"] = inner_times_add
            item_for_times["less_add"] = less_times_add
            item_for_locations["inner"] = inner_locations
            item_for_locations["less"] = less_locations
            item_for_locations["last"] = last_locations
            item_for_locations["next"] = next_locations
            item_for_locations["inner_add"] = inner_locations_add
            item_for_locations["less_add"] = less_locations_add
            item_for_weapons["inner"] = inner_weapons
            item_for_weapons["less"] = less_weapons
            item_for_weapons["last"] = last_weapons
            item_for_weapons["next"] = next_weapons
            item_for_weapons["inner_add"] = inner_weapons_add
            item_for_weapons["less_add"] = less_weapons_add
            item_for_countries["inner"] = inner_countries
            item_for_countries["less"] = less_countries
            item_for_countries["last"] = last_countries
            item_for_countries["next"] = next_countries
            item_for_countries["inner_add"] = inner_countries_add
            item_for_countries["less_add"] = less_countries_add

            items["time"] = item_for_times
            items["location"] = item_for_locations
            items["weapon"] = item_for_weapons
            items["country"] = item_for_countries

            event_item["trigger"] = event_trigger
            event_item["subject"] = event_subject
            event_item["object"] = event_object
            event_item["polarity"] = event_polarity
            event_item["tense"] = event_tense
            event_item["keySentence"] = index
            event_item["items"] = items

            events.append(event_item)
    all_less_times = []
    all_less_locations = []
    all_less_weapons = []
    all_less_countries = []
    for index in range(0, max_index + 1):
        if index in less_sentences:
            all_less_times += all_times[index]
            all_less_locations += all_locations[index]
            all_less_weapons += all_weapons[index]
            all_less_countries += all_countries[index]
    less_item = {"time": all_less_times, "location": all_less_locations,
                 "weapon": all_less_weapons, "country": all_less_countries}
    return events, less_item, all_items_text, weapon_country


def getFormatDict(items_texts, weapon_country, time="2020-12-31 15:18"):
    time_dict = getTimeDict(items_texts["time"], time=time)
    location_dict = getLocationDict(items_texts["location"])
    country_dict = getCountryDict(items_texts["country"])
    weapon_dict = getWeaponDict(items_texts["weapon"], country_dict, weapon_country)
    items_dicts = {"time": time_dict, "location": location_dict, "weapon": weapon_dict, "country": country_dict}
    return items_dicts


def doFormat(items_key, items_values, format_dict=None):
    rtn_format_items = []
    format_values = []
    format_items = set()
    assert items_key in ["time", "location", "weapon", "country"], \
        "key must be 'time', 'location', 'weapon', 'country'"
    for item_id, item_value in items_values:
        item_text = item_value["text"]
        format_item = format_dict[item_text]
        format_values.append(format_item)
        format_items.add(format_item)
        if "[split]" in format_item:
            format_items_split = format_item.split("[cut]")[-1].split("[split]")
            for split_item in format_items_split:
                format_values.append(split_item)
                format_items.add(split_item)
    for item in format_items:
        rtn_format_items.append((item, format_values.count(item)))
    return rtn_format_items


def getFormatEvent(events, less_items, level_weights=None, format_dicts=None):
    if level_weights is None:
        level_weights = [2] * 7
    rtn_events = []
    less_format_items = {}
    less_items_keys = list(less_items.keys())
    for less_key in less_items_keys:
        less_format_items[less_key] = doFormat(less_key, less_items[less_key],
                                               format_dict=format_dicts[less_key])
    for event in events:
        items = event["items"]
        rtn_event = copy.deepcopy(event)
        rtn_items = {}
        items_keys = list(items.keys())
        for key in items_keys:
            level_items = items[key]
            level_keys = list(level_items.keys())
            key_items = {}
            key_items_keys = []
            for level_index, level_key in enumerate(level_keys):
                format_items = doFormat(key, level_items[level_key], format_dict=format_dicts[key])
                for format_item, number in format_items:
                    if format_item not in key_items_keys:
                        key_items[format_item] = number
                    else:
                        key_items[format_item] = key_items[format_item] + number
                key_items_keys = list(key_items.keys())
                for key_items_key in key_items_keys:
                    key_items[key_items_key] = key_items[key_items_key] * level_weights[level_index]
            for format_item, number in less_format_items[key]:
                if format_item not in key_items_keys:
                    key_items[format_item] = number
                else:
                    key_items[format_item] = key_items[format_item] + number
            key_items_items = list(key_items.items())
            rtn_key_items = {"first": [], "second": []}
            if len(key_items_items) > 0:
                key_items_items.sort(key=lambda x: x[1], reverse=True)
                for key_items_item, key_items_number in key_items_items:
                    if key_items_number >= 32:
                        rtn_key_items["first"].append((key_items_item, key_items_number))
                    elif key_items_number >= 16:
                        rtn_key_items["second"].append((key_items_item, key_items_number))
            rtn_items[key] = rtn_key_items
        rtn_event["items"] = rtn_items
        rtn_events.append(rtn_event)

    return rtn_events


# 每个event的格式
# 返回的event_txt格式为(事件串，事件类型)
def doFusion(events, article_path):
    format_functions = {
        "time": formatTime,
        "location": formatLoc,
        "weapon": formatWeapon,
        "country": formatCountry
    }
    events_txt = []
    events_json = []
    event_class_list = getEventClassList()
    for event_class in event_class_list:
        tmp_events = []
        trigger_lists = getTriggerList(event_class)
        for triggers in trigger_lists:
            same_events = []
            for event in events:
                if event["trigger"]["text"] in triggers:
                    add_event = copy.deepcopy(event)
                    same_events.append(add_event)
            tmp_events += ComplementByEachOther(same_events, event_class)
        for tmp_event in tmp_events:
            tmp_event["newsPos"] = article_path
            events_json.append(tmp_event)
    return events_txt, events_json


def eventsFuse(opt, logger):
    SourcePath = opt.sourcePath
    pathList = getPathListBySuffix(SourcePath, "json")
    years = []
    pathListOfYear = {}  # 将相对路径按年份分开存储
    for each_path in pathList:
        path_pieces = each_path.split("/")  # 路径为绝对路径，最后部分为 /{year}/json/{id}.json
        year = path_pieces[-3]
        if year not in years:
            years.append(year)
            pathListOfYear[year] = []
        pathListOfYear[year].append((path_pieces[-2], path_pieces[-1].split(".")[0]))
    getConn()
    createAllItemsList(opt)
    createEventItems(opt)
    for yearFolder in years:
        events_jsons = []
        EventSavePath = opt.DataPath + "/" + yearFolder + "/" + opt.EventFolder
        basePath = SourcePath + "/" + yearFolder + "/"
        EventXlsPath = basePath + "events.xls"
        nameList = ["事件元素抽取结果", "事件元素备选集结果", "事件元素权重结果", "事件信息融合结果", "事件标准化结果", "装备事件元素整合"]
        tittles = [
            ["新闻编号", "句子内容", "触发词__主体__客体", "时间", "地点", "武器", "国家"],
            ["新闻编号", "触发词", "主体", "客体", "第一级", "第二级", "第三级", "第四级", "第五级", "第六级", "第七级"],
            ["新闻编号", "触发词", "主体", "客体", "时间", "地点", "武器", "国家"],
            ["新闻编号", "触发词", "主体", "客体", "时间", "地点", "武器", "国家"],
            ["新闻编号", "事件类别", "开始时间", "结束时间", "事件地点", "事件触发词", "相关武器", "主体国家", "客体国家",
             "事件状态", "事件极性"],
            ["新闻编号", "事件类别", "开始时间", "结束时间", "事件地点", "事件触发词", "相关武器", "主体国家", "客体国家",
             "事件状态", "事件极性"]
        ]
        createXls(EventXlsPath, nameList, tittles)

        all_file = open(basePath + "result.txt", "w+", encoding="utf-8")
        trigger_file = open(basePath + "triggers.txt", "w+", encoding="utf-8")
        text_number = 0

        for inner, number in pathListOfYear[yearFolder]:
            article_path = f"/{yearFolder}/{opt.ArticleFolder}/{number}"
            relativePath = inner + "/" + number + ".json"  # 拼接出相对路径
            event_file = open(basePath + relativePath, "r", encoding="utf-8")
            sentences = json.load(event_file)
            event_file.close()

            time = ""
            location = ""
            weapon = ""
            country = ""
            event_text = ""
            sentence_content = ""
            for sentence in sentences:
                for role_ in sentence["arguments"]["time"]:
                    time = time + ";" + role_["text"]
                for role_ in sentence["arguments"]["loc"]:
                    location = location + ";" + role_["text"]
                for role_ in sentence["arguments"]["weapon"]:
                    weapon = weapon + ";" + role_["text"]
                for role_ in sentence["arguments"]["country"]:
                    country = country + ";" + role_["text"]
                for event_ in sentence["events"]:
                    event_text = event_text + ";" + event_["trigger"]["text"] + "__" + event_["subject"]["text"] + \
                                 "__" + event_["object"]["text"]
                time += "\n"
                location += "\n"
                weapon += "\n"
                country += "\n"
                event_text += "\n"
                sentence_content += sentence["sentence"] + "\n"
            event_data = [number, sentence_content, event_text, time[1:], location[1:], weapon[1:], country[1:]]
            writeXls(EventXlsPath, event_data, 0)

            all_file.write("第" + number + "篇\n")
            txt_file = open(basePath + "txt/" + number + ".txt", "r", encoding="utf-8")
            lines = txt_file.readlines()

            # 获取所有的事件，及事件对应的关键句序列
            events, less_items, all_items_text, weapon_country = getEvent(sentences)

            level_trigger = ""
            level_subject = ""
            level_object = ""
            level_items = [""] * 7
            level_keys = ["inner", "less", "last", "next", "inner_add", "less_add"]
            for tmp_event in events:
                level_trigger = level_trigger + ";" + tmp_event["trigger"]["text"]
                level_subject = level_subject + ";" + tmp_event["subject"]["text"]
                level_object = level_object + ";" + tmp_event["object"]["text"]
                role = tmp_event["items"]
                all_level_time = role["time"]
                all_level_location = role["location"]
                all_level_weapon = role["weapon"]
                all_level_country = role["country"]
                for level_index, level_key in enumerate(level_keys):
                    tmp_times = ""
                    tmp_locations = ""
                    tmp_weapons = ""
                    tmp_countries = ""
                    for index, tmp_time in all_level_time[level_key]:
                        tmp_times += tmp_time["text"]
                    for index, tmp_location in all_level_location[level_key]:
                        tmp_locations += tmp_location["text"]
                    for index, tmp_weapon in all_level_weapon[level_key]:
                        tmp_weapons += tmp_weapon["text"]
                    for index, tmp_country in all_level_country[level_key]:
                        tmp_countries += tmp_country["text"]
                    level_items[level_index] = level_items[level_index] + "时间：" + tmp_times + " 地点：" \
                                               + tmp_locations + " 武器：" + tmp_weapons + " 国家：" \
                                               + tmp_countries + "\n"

            event_data_level = [number, level_trigger, level_subject, level_object] + level_items
            writeXls(EventXlsPath, event_data_level, 1)

            items_format_dicts = getFormatDict(all_items_text, weapon_country, time=lines[3].strip())
            events_after_format = getFormatEvent(events, less_items,
                                                 format_dicts=items_format_dicts)

            format_trigger = ""
            format_subject = ""
            format_object = ""
            format_time = ""
            format_location = ""
            format_weapon = ""
            format_country = ""
            for tmp_event in events_after_format:
                format_trigger = format_trigger + ";" + tmp_event["trigger"]["text"]
                format_subject = format_subject + ";" + tmp_event["subject"]["text"]
                format_object = format_object + ";" + tmp_event["object"]["text"]
                role = tmp_event["items"]
                all_format_time = role["time"]
                for tmp_time_0, tmp_time_num in all_format_time["first"]:
                    format_time += tmp_time_0 + "(" + str(tmp_time_num) + ");"
                for tmp_time_0, tmp_time_num in all_format_time["second"]:
                    format_time += tmp_time_0 + "(" + str(tmp_time_num) + ");"
                format_time += "\n"
                all_format_location = role["location"]
                for tmp_location_0, tmp_location_num in all_format_location["first"]:
                    format_location += tmp_location_0 + "(" + str(tmp_location_num) + ");"
                for tmp_location_0, tmp_location_num in all_format_location["second"]:
                    format_location += tmp_location_0 + "(" + str(tmp_location_num) + ");"
                format_location += "\n"
                all_format_weapon = role["weapon"]
                for tmp_weapon_0, tmp_weapon_num in all_format_weapon["first"]:
                    format_weapon += tmp_weapon_0 + "(" + str(tmp_weapon_num) + ");"
                for tmp_weapon_0, tmp_weapon_num in all_format_weapon["second"]:
                    format_weapon += tmp_weapon_0 + "(" + str(tmp_weapon_num) + ");"
                format_weapon += "\n"
                all_format_country = role["country"]
                for tmp_country_0, tmp_country_num in all_format_country["first"]:
                    format_country += tmp_country_0 + "(" + str(tmp_country_num) + ");"
                for tmp_country_0, tmp_country_num in all_format_country["second"]:
                    format_country += tmp_country_0 + "(" + str(tmp_country_num) + ");"
                format_country += "\n"

            event_data_format = [number, format_trigger, format_subject, format_object, format_time, format_location,
                                 format_weapon, format_country]
            writeXls(EventXlsPath, event_data_format, 2)

            events_txt, events_json = doFusion(events_after_format, article_path)

            tmp_events_after_merge = getTmpEvents()
            merge_trigger = ""
            merge_subject = ""
            merge_object = ""
            merge_time = ""
            merge_location = ""
            merge_weapon = ""
            merge_country = ""
            for tmp_event in tmp_events_after_merge:
                merge_trigger = merge_trigger + ";" + tmp_event["trigger"]["text"]
                merge_subject = merge_subject + ";" + tmp_event["subject"]["text"]
                merge_object = merge_object + ";" + tmp_event["object"]["text"]
                role = tmp_event["items"]
                all_merge_time = role["time"]
                for tmp_time_0, tmp_time_num in all_merge_time:
                    merge_time += tmp_time_0 + ";"
                merge_time += "\n"
                all_merge_location = role["location"]
                for tmp_location_0, tmp_location_num in all_merge_location["first"]:
                    merge_location += tmp_location_0 + ";"
                merge_location += "\n"
                all_merge_weapon = role["weapon"]
                for tmp_weapon_0, tmp_weapon_num in all_merge_weapon["first"]:
                    merge_weapon += tmp_weapon_0 + ";"
                merge_weapon += "\n"
                all_merge_country = role["country"]
                for tmp_country_0, tmp_country_num in all_merge_country["first"]:
                    merge_country += tmp_country_0 + ";"
                merge_country += "\n"

            event_data_format = [number, merge_trigger, merge_subject, merge_object, merge_time, merge_location,
                                 merge_weapon, merge_country]
            writeXls(EventXlsPath, event_data_format, 3)

            cleanTmpEvents()

            event_type = ""
            start_time = ""
            end_time = ""
            all_locations = ""
            event_triggers = ""
            relate_weapons = ""
            subject_countries = ""
            object_countries = ""
            event_status = ""
            event_polarity = ""
            for tmp_event in events_json:
                event_type += ";" + tmp_event["eventClass"]
                start_time += ";" + tmp_event["startTime"]
                end_time += ";" + tmp_event["endTime"]
                tmp_all_locations = ""
                for role in tmp_event["eventLocations"]:
                    tmp_all_locations += ";" + role
                all_locations += tmp_all_locations

                tmp_event_triggers = ""
                for role in tmp_event["eventTriggers"]:
                    tmp_event_triggers += ";" + role
                event_triggers += tmp_event_triggers

                tmp_relate_weapons = ""
                for role in tmp_event["relateWeapons"]:
                    tmp_relate_weapons += ";" + role
                relate_weapons += tmp_relate_weapons

                tmp_subject_countries = ""
                for role in tmp_event["subjectCountries"]:
                    tmp_subject_countries += ";" + role
                subject_countries += tmp_subject_countries

                tmp_object_countries = ""
                for role in tmp_event["objectCountries"]:
                    tmp_object_countries += ";" + role
                object_countries += tmp_object_countries
                event_status += tmp_event["eventStatus"]
                event_polarity += tmp_event["eventPolarity"]
                event_data_each = [number, tmp_event["eventClass"], tmp_event["startTime"], tmp_event["endTime"],
                                   tmp_all_locations, tmp_event_triggers, tmp_relate_weapons, tmp_subject_countries,
                                   tmp_object_countries, tmp_event["eventStatus"], tmp_event["eventPolarity"]]
                writeXls(EventXlsPath, event_data_each, 4)
            event_data_add = [number, event_type, start_time, end_time, all_locations, event_triggers, relate_weapons,
                              subject_countries, object_countries, event_status, event_polarity]
            writeXls(EventXlsPath, event_data_add, 5)

            events_jsons += events_json
            '''
            for event_txt, event_class in events_txt:
                EventSaveFile_txt = EventSavePath + "/" + event_class + ".txt"
                event_file_txt = open(EventSaveFile_txt, "w+", encoding="utf-8")
                event_file.write(event_txt + "\n")
                event_file_txt.close()'''
            # writeEvents(opt, events_jsons, yearFolder, number)
            '''
            test1
            for line in lines:
                all_file.write(line)
            all_file.write("\n剩余未添加事件元素：\n")
            less_items_list = [less_items["time"], less_items["location"], less_items["weapon"], less_items["country"]]
            for less_item in less_items_list:
                items = []
                for seq_id, inner_role in less_item:
                    items.append(inner_role["text"])
                all_file.write(str(items) + "\n")
            print("第" + number + "篇")
            for event in events:
                all_file.write("第" + str(event["keySentence"]) + "个句子   ")
                all_file.write("触发词：" + str(event["trigger"]["text"]) + "\n")
                role = event["items"]
                all_file.write("备选元素集：\n")

                my_role = role["time"]
                my_list = [my_role["inner"], my_role["less"], my_role["last"],
                           my_role["next"], my_role["inner_add"], my_role["less_add"]]
                for index, item in enumerate(my_list):
                    items = []
                    for seq_id, inner_role in item:
                        items.append(inner_role["text"])
                    all_file.write("第" + str(index + 1) + "级时间：" + str(items) + "\n")
                my_role = role["location"]
                all_file.write("\n")
                my_list = [my_role["inner"], my_role["less"], my_role["last"],
                           my_role["next"], my_role["inner_add"], my_role["less_add"]]
                for index, item in enumerate(my_list):
                    items = []
                    for seq_id, inner_role in item:
                        items.append(inner_role["text"])
                    all_file.write("第" + str(index + 1) + "级地点：" + str(items) + "\n")
                my_role = role["weapon"]
                all_file.write("\n")
                my_list = [my_role["inner"], my_role["less"], my_role["last"],
                           my_role["next"], my_role["inner_add"], my_role["less_add"]]
                for index, item in enumerate(my_list):
                    items = []
                    for seq_id, inner_role in item:
                        items.append(inner_role["text"])
                    all_file.write("第" + str(index + 1) + "级武器：" + str(items) + "\n")
                all_file.write("\n")
                my_role = role["country"]
                my_list = [my_role["inner"], my_role["less"], my_role["last"],
                           my_role["next"], my_role["inner_add"], my_role["less_add"]]
                for index, item in enumerate(my_list):
                    items = []
                    for seq_id, inner_role in item:
                        items.append(inner_role["text"])
                    all_file.write("第" + str(index + 1) + "级国家及组织：" + str(items) + "\n")
                all_file.write("\n\n")
            all_file.write("\n\n\n")
            test end
            '''
            '''
            test2
            '''
            for line in lines:
                all_file.write(line)
            all_file.write("\n所有规范化事件：\n")
            trigger_write = []
            # print("第" + number + "篇\n")
            for event in events_json:
                '''event_write = {"触发词": event["trigger"]["text"]}
                event_items = event["items"]
                if event_items["time"][1] >= 16:
                    event_write["时间"] = event_items["time"][0]
                else:
                    event_write["时间"] = ""
                if event_items["location"][1] >= 16:
                    event_write["地点"] = event_items["location"][0]
                else:
                    event_write["地点"] = ""
                if event_items["weapon"][1] >= 16:
                    event_write["武器"] = event_items["weapon"][0]
                else:
                    event_write["武器"] = ""
                if event_items["country"][1] >= 16:
                    event_write["国家或组织"] = event_items["country"][0]
                else:
                    event_write["国家或组织"] = ""'''
                all_file.write(f"{str(event)}\n")
                trigger_write += event['eventTriggers']
            for trigger in set(trigger_write):
                trigger_file.write(f"{trigger} ")
            text_number += 1
            all_file.write("\n\n\n")
            trigger_file.write("\n")
            '''
            events_txt, events_json, key_sentences_txt = doFusion(events)
            events_jsons += events_json
            for event_txt, event_class in events_txt:
                EventSaveFile_txt = EventSavePath + "/" + event_class + ".txt"
                event_file_txt = open(EventSaveFile_txt, "w+", encoding="utf-8")
                event_file.write(event_txt + "\n")
                event_file_txt.close()
            writeEvents(opt, events_jsons, yearFolder, number)
            '''
        all_file.close()
        print(text_number)
        trigger_file.close()
    delConn()
    closeUnknownFile()
