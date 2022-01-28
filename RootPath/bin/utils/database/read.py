# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: read.py
@time: 2021/8/19 21:47
"""
from utils.database.connect import getCursor

weapon_classes = []
weapon_Super_classes = []


def getNewsID(year, fileName):
    cursor = getCursor()
    query_news = f'''select * from news where newsPos = "/{year}/Articles/{fileName}"'''
    cursor.execute(query_news)
    news_id = cursor.fetchone()[0]
    return news_id


def queryWeaponClasses():
    global weapon_classes
    global weapon_Super_classes
    query_classes = []
    query_Super_classes = []
    query_weapon_Super_class = '''select * from weapons group by weaponSClass'''
    query_weapon_class = '''select * from weapons group by weaponClass'''
    cursor = getCursor()
    cursor.execute(query_weapon_Super_class)
    weapon_Super_class = cursor.fetchall()
    for super_class in weapon_Super_class:
        check_super_class = super_class[3]
        if (check_super_class != "") and (check_super_class not in query_Super_classes):
            query_Super_classes.append(check_super_class)
            weapon_Super_classes.append((check_super_class, super_class[0]))
    cursor.execute(query_weapon_class)
    weapon_class = cursor.fetchall()
    for each_class in weapon_class:
        check_class = each_class[2]
        if (check_class != "") and (check_class not in query_classes):
            query_classes.append(check_class)
            weapon_classes.append((check_class, each_class[0]))


def getWeaponClasses():
    return weapon_classes


def getWeaponSuperClasses():
    return weapon_Super_classes


def getWeaponByName(name):
    cursor = getCursor()
    query_weapon_by_name = '''select * from weapons where weaponName = %s'''
    cursor.execute(query_weapon_by_name, name)
    cursor.fetchall()
