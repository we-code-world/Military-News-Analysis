# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: Event.py
@time: 2021/8/13 19:01
"""
from utils.logger import *
from utils.lock import *
from event.fusion import eventsFuse
from utils.options import EventArgs


def mainFunction():
    set_event_logConfig()
    # if process_lock("model")==False:
    #    return 0

    args = EventArgs().get_parser()

    # args.sourcePath = "E:/Rootpath/data/test"

    assert args.operation in ['fusion'], 'Undefined operation in Event'

    operation_func = args.operation  # 根据输入参数决定执行的操作

    if operation_func == 'fusion':
        eventsFuse(args, get_logger("fusion"))

    # return unlock("model")


if __name__ == '__main__':
    mainFunction()
