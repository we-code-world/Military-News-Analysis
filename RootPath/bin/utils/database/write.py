# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: write.py
@time: 2021/8/19 21:48
"""
from utils.database.connect import getCursor, doCommit


# value: (tittle, time, url, source, path)
def writeNews(values):
    cursor = getCursor()
    query_insert = '''insert into news(newsID, newsTittle, newsTime, url, newsSource, newsPos) 
                      values (null,%s,%s,%s,%s,%s) '''
    cursor.execute(query_insert, values)
    doCommit()


def writeSentence(sentence):
    cursor = getCursor()
    query_insert = '''insert into KeySentence(
                        SentenceID, newsID, SentenceNum, matchTime, matchLoc, weaponName, EventTrigger) 
                        values (null,%s,%s,%s,%s,%s,%s)'''
    sentences_id = []
    return sentences_id


def writeNewWeapon(value):
    cursor = getCursor()
    write_back_weapon_new = '''insert into weapons(weaponID, weaponName, weaponClass, weaponSClass, weaponCountry)
                               values (null,%s,%s,%s,%s)
                            '''
    cursor.execute(write_back_weapon_new, value)
    weaponId = cursor.lastrowid
    cursor.execute('commit;')
    return weaponId


def writeEvent(value):
    query_insert = f'''insert into events(eventID, eventClass, startTime, endTime,
                    eventLocations, eventTriggers, relateWeapons, subjectCountries, objectCountries,
                    eventStatus, eventPolarity, newsPos) 
                    values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor = getCursor()
    cursor.execute(query_insert, value)


'''
if __name__ == "__main__":
    
    from utils.database.connect import getConn, delConn
    getConn()
    cursor = getCursor()
    f = open("E:/Rootpath/resource/Country.txt", "a+", encoding="utf-8")
    query_get = "select * from locations"
    cursor.execute(query_get)
    locations_res = cursor.fetchall()
    locations = []
    for location_res in locations_res:
        loc = location_res[1]
        if loc is not None and loc not in locations:
            locations.append(loc)
    for location in locations:
        f.write(location + "\n")
    f.close()
    delConn()
'''
