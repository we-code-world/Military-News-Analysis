"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: MyThread.py
@time: 2021/7/6 21:23
"""
import threading

lock = threading.RLock()


class MyEventThread(threading.Thread):
    def __init__(self, thread_id, name, query_insert, query_select, func, cursor, url):
        threading.Thread.__init__(self)
        self.id = thread_id
        self.name = name
        self.query_insert = query_insert
        self.query_select = query_select
        self.func = func
        self.cursor = cursor
        self.url = url

    def run(self):
        f = open(self.url + self.name + ".txt", 'r', encoding='utf-8')
        coarse_lines = f.readlines()
        coarse_lists = []
        for coarse_line in coarse_lines:
            coarse_list = coarse_line.strip("\n").strip(" ").split(",,,")
            coarse_lists.append(coarse_list)
        lines = self.func(coarse_lists, self.cursor, lock)
        for line in lines:
            lock.acquire()
            self.cursor.execute(self.query_insert, line)
            lock.release()
        f.close()
