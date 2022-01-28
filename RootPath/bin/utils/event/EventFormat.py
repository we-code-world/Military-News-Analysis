# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: EventFormat.py
@time: 2021/7/6 21:18
"""
from utils.database.connect import getCursor, doCommit
from utils.file.path import getFatherPath
from utils.database.read import getWeaponClasses, getWeaponSuperClasses

# 设置数据库查询语句
# 请求
query_weapon_by_name = '''select weaponID from weapons where weaponName = %s;'''
query_weapon_Sclass = '''select * from weapons group by weaponSClass'''
query_weapon_class = '''select * from weapons group by weaponClass'''
query_location_id = '''select posID from locations where FirstPos = %s or SecondPos = %s'''

# 写回
write_back_weapon_new = '''insert into weapons(weaponID,weaponName,weaponClass,weaponSClass,weaponCountry)
                           values (null,%s,%s,%s,%s)'''
write_back_weapon_old = '''update weapons 
                           set weaponName=%s, weaponClass=%s, weaponSClass=%s, weaponCountry=%s
                           where weaponID=%d'''
write_back_location = '''insert into locations(posID,SecondPos,PosLevel) values (null,%s,0)'''


def TXT2json(path):
    jsonSavePath = getFatherPath(path)


# 执行时间格式化
def formatTime(Times):
    times = []
    for Time in Times:
        start_end_time = Time.split(" ")
        times.append((start_end_time[0], start_end_time[1]))
    return times


# 执行地点格式化,返回地点的id序列
def formatLoc(Locations):
    LocationList = []
    cursor = getCursor()
    for location in Locations:
        write_value = (location, location)
        cursor.execute(query_location_id, write_value)
        thisLocation = cursor.fetchone()
        locationId = 0
        if thisLocation is None:
            write_value = location
            cursor.execute(write_back_location, write_value)
            locationId = cursor.lastrowid
            cursor.execute('commit;')
        else:
            locationId = thisLocation[0]
        LocationList.append(str(locationId))
    doCommit()
    return LocationList


# {"country": "美国", "name": "B-52战略轰炸机"}
# 执行武器装备格式化
# 查询数据库中的武器
# 拼接最终结果为“国名 + 武器种类 + 武器编号”
def formatWeapon(weapon):
    weapon_SuperClasses = getWeaponSuperClasses()
    weapon_Classes = getWeaponClasses()
    cursor = getCursor()
    weaponCountry = weapon["country"]
    weaponName = weapon["name"]
    weaponClass = ""
    weaponSuperClass = ""
    LEVEL = "C-"
    weaponId = 0
    for weapon_ID, weapon_Class in weapon_Classes:
        if weapon_Class in weaponName:
            LEVEL = "A-"
            weaponClass = weapon_Class
            weaponId = weapon_ID
    for weapon_ID, weapon_SuperClass in weapon_SuperClasses:
        if weapon_SuperClass in weaponName:
            LEVEL = "B-"
            weaponSuperClass = weapon_SuperClass
            weaponId = weapon_ID
    cursor.execute(query_weapon_by_name, weaponName)
    thisWeapon = cursor.fetchone()
    if thisWeapon is None:
        write_value = (weaponName, weaponClass, weaponSuperClass, weaponCountry)
        cursor.execute(write_back_weapon_new, write_value)
        weaponId = cursor.lastrowid
        cursor.execute('commit;')
    else:
        weaponId = thisWeapon[0]
    standardWeapon = weaponCountry + "-" + LEVEL + str(weaponId)
    return standardWeapon


def formatCountry(country="美国"):
    standardCountry = ""
    return standardCountry
