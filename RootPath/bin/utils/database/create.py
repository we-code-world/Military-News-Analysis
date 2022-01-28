from utils.database.connect import *


def createDB():
    getConn()
    try:
        cursor.execute(
            '''create table user(
            Userid int NOT NULL AUTO_INCREMENT primary key,
            userName VARCHAR(50),
            account VARCHAR(50),
            password VARCHAR(50),
            Sex int,Email VARCHAR(50),
            Telephone VARCHAR(50),
            Address VARCHAR(50),
            QQ VARCHAR(50)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表user已存在！')
    try:
        cursor.execute(
            '''create table administrator(
            Userid int NOT NULL AUTO_INCREMENT primary key,
            userName VARCHAR(50),
            account VARCHAR(50),
            password VARCHAR(50)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表administrator已存在！')

    try:
        cursor.execute(
            '''create table news(
            newsID int NOT NULL AUTO_INCREMENT primary key,
            newsTime datetime,
            url VARCHAR(50)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表news已存在！')
    try:
        cursor.execute(
            '''create table weaponSentence(
            SentenceID int NOT NULL AUTO_INCREMENT primary key,
            newsID int,
            weaponName VARCHAR(20),
            SentenceContent Varchar(500)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表weaponSentence已存在！')
    try:
        cursor.execute(
            '''create table weapon(
            weaponID int NOT NULL AUTO_INCREMENT primary key,
            weaponName VARCHAR(50),
            weaponClass VARCHAR(20),
            weaponSClass VARCHAR(20),
            weaponCountry VARCHAR(200)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表weapon已存在！')
    try:
        cursor.execute(
            '''create table weapons(
            weaponID int NOT NULL AUTO_INCREMENT primary key,
            weaponName VARCHAR(50),
            weaponClass VARCHAR(20),
            weaponSClass VARCHAR(20),
            weaponCountry VARCHAR(200)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表weapons已存在！')
    try:
        cursor.execute(
            '''create table Locations(
            posID int NOT NULL AUTO_INCREMENT primary key,
            FirstPos VARCHAR(50),
            SecondPos VARCHAR(50),
            ThirdPos VARCHAR(50),
            standardPos VARCHAR(50),
            longitude DOUBLE,
            latitude DOUBLE
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表Locations已存在！')
    try:
        cursor.execute(
            '''create table Events(
            eventID int NOT NULL AUTO_INCREMENT primary key,
            eventClass CHAR(10),
            startTime datetime,
            endTime datetime,
            eventLocations CHAR(20),
            eventTriggers CHAR(20),
            relateWeapons CHAR(20),
            subjectCountries CHAR(20),
            objectCountries CHAR(20),
            eventStatus INT,
            eventPolarity INT,
            newsPos CHAR(20)
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表Events已存在！')
    try:
        cursor.execute(
            '''create table RDEvent(
            RDEventID int NOT NULL AUTO_INCREMENT primary key,
            RDEventTime datetime,
            RDEventLocation VARCHAR(20),
            RDCountry VARCHAR(20),
            RDOrganization VARCHAR(20),
            RDEventTrigger VARCHAR(20),
            relateWeapon VARCHAR(20),
            SentenceID int
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表RDEvent已存在！')
    try:
        cursor.execute(
            '''create table accidentEvent(
            accidentEventID int NOT NULL AUTO_INCREMENT primary key,
            accidentEventTime datetime,
            accidentEventLocation VARCHAR(20),
            accidentEventTrigger VARCHAR(20),
            relateWeapon VARCHAR(20),
            SentenceID int
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表accidentEvent已存在！')
    try:
        cursor.execute(
            '''create table conflictEvent(
            conflictEventID int NOT NULL AUTO_INCREMENT primary key,
            conflictEventTime datetime,
            conflictEventLocation VARCHAR(20),
            activeSubject VARCHAR(20),
            sufferSubject VARCHAR(20),
            conflictEventTrigger VARCHAR(20),
            relateWeapon VARCHAR(20),
            SentenceID int
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表conflictEvent已存在！')
    try:
        cursor.execute(
            '''create table practiceEvent(
            practiceEventID int NOT NULL AUTO_INCREMENT primary key,
            practiceSEventTime datetime,
            practiceEEventTime datetime,
            practiceEventLocation VARCHAR(20),
            practiceWeapon VARCHAR(20),
            practiceEventTrigger VARCHAR(20),
            practiceSubject VARCHAR(20),
            SentenceID int
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表practiceEvent已存在！')
    try:
        cursor.execute(
            '''create table provocativeEvent(
            provocativeEventID int NOT NULL AUTO_INCREMENT primary key,
            provocativeEventTime datetime,
            provocativeEventLocation VARCHAR(20),
            provocativeEventTrigger VARCHAR(20),
            activeSubject VARCHAR(20),
            sufferSubject VARCHAR(20),
            relateWeapon VARCHAR(20),
            SentenceID int
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表provocativeEvent已存在！')
    try:
        cursor.execute(
            '''create table transactionEvent(
            transactionEventID int NOT NULL AUTO_INCREMENT primary key,
            transactionEventTime datetime,
            transactionEventTrigger VARCHAR(20),
            transactionWeapon VARCHAR(20),
            saleCountry VARCHAR(20),
            transactionStatus VARCHAR(20),
            SentenceID int
        )ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;''')
    except:
        print('数据表transactionEvent已存在！')
    delConn()
