# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: EventForDB.py
@time: 2021/8/19 21:18
"""
import copy
from utils.database.read import getWeaponClasses, getWeaponSuperClasses, getWeaponByName
from utils.database.write import writeEvent, writeNewWeapon

EventNames = ['accident', 'conflict', 'practice', 'provocative', 'rd', 'transaction']


# 执行武器装备格式化
# 查询数据库中的武器
# 拼接最终结果为“国名 + 武器种类 + 武器编号”
def getStandardWeapon(weapons=[{"country": "美国", "name": "B-52战略轰炸机"}]):
    weaponList = []
    weapon_SuperClasses = getWeaponSuperClasses()
    weapon_Classes = getWeaponClasses()
    for weapon in weapons:
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
        thisWeapon = getWeaponByName(weaponName)
        if thisWeapon is None:
            write_value = (weaponName, weaponClass, weaponSuperClass, weaponCountry)
            weaponId = writeNewWeapon(write_value)
        else:
            weaponId = thisWeapon[0]
        standardWeapon = weaponCountry + "-" + LEVEL + str(weaponId)
        weaponList.append(standardWeapon)
    return weaponList


def writeEvents(opt, events, year, number):

    for event in events:
        event_class = event["class"]
        event_ = opt.get_default(event_class)
        event_value = opt.get_default(event_class + "_value")
        writeEvent(event_value)