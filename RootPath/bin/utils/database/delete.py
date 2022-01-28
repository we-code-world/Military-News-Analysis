from utils.database.connect import *


def deleteDB():
    getConn()
    try:
        cursor.execute('DROP TABLE RDEvent;')
    except:
        print('数据表RDEvent已删除！')
    try:
        cursor.execute('DROP TABLE accidentEvent;')
    except:
        print('数据表accidentEvent已删除！')
    try:
        cursor.execute('DROP TABLE conflictEvent;')
    except:
        print('数据表conflictEvent已删除！')
    try:
        cursor.execute('DROP TABLE practiceEvent;')
    except:
        print('数据表practiceEvent已删除！')
    try:
        cursor.execute('DROP TABLE provocativeEvent;')
    except:
        print('数据表provocativeEvent已删除！')
    try:
        cursor.execute('DROP TABLE transactionEvent;')
    except:
        print('数据表transactionEvent已删除！')
    try:
        cursor.execute('DROP TABLE user;')
    except:
        print('数据表user已删除！')
    try:
        cursor.execute('DROP TABLE administrator;')
    except:
        print('数据表administrator已删除！')
    try:
        cursor.execute('DROP TABLE weapon;')
    except:
        print('数据表weapon已删除！')
    try:
        cursor.execute('DROP TABLE weapons;')
    except:
        print('数据表weapons已删除！')
    try:
        cursor.execute('DROP TABLE Locations;')
    except:
        print('数据表Locations已删除！')
    try:
        cursor.execute('DROP TABLE keySentence')
    except:
        print('数据表keySentence已删除！')
    try:
        cursor.execute('DROP TABLE news;')
    except:
        print('数据表news已删除！')
    delConn()
