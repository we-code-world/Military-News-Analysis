import pymysql

# 数据库连接对象
db: pymysql.connections.Connection

# 游标对象
cursor: pymysql.cursors.Cursor


def getConn():
    global db, cursor
    # 建立数据库连接
    db = pymysql.connect('localhost', 'news_event', 'news_event', 'military_events')
    # 获取游标对象
    cursor = db.cursor()


def getCursor():
    return cursor


def doCommit():
    db.commit()


def delConn():
    global db, cursor
    cursor.close()
    db.commit()
    db.close()


if __name__ == '__main__':
    mycursor = getConn()
    delConn()
