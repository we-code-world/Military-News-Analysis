# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: lock.py
@time: 2021/6/28 8:59
"""

import os
lock_path = "lock/"
#设置lock文件路径
def set_lock_path(path):
    global lock_path
    lock_path = path
#检查是否是唯一一个运行时的函数
def function_lock(func):
    if not os.path.exists("lock"):
        os.mkdir("lock")
    set_lock_file = lock_path + func +".clk"
    if os.path.exists(set_lock_file):
        print("函数"+func+"已被执行，无法同时执行另一个函数，这可能导致无法想象的错误！")
        return False
    else:
        fp = open(set_lock_file,"a+")
        fp.close()
        return True

#检查是否是唯一一个运行时的进程
def process_lock(proc):
    if not os.path.exists("lock"):
        os.mkdir("lock")
    set_lock_file = lock_path + proc +".clk"
    if os.path.exists(set_lock_file):
        print("进程"+proc+"已被执行，无法同时执行另一个进程，这可能导致无法想象的错误！")
        return False
    else:
        fp = open(set_lock_file,"a+")
        fp.close()
        return True

#解锁
def unlock(lock_file):
    return os.remove(lock_path + lock_file + ".clk")
