# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: lock.py
@time: 2021/6/28 8:59
"""

import os
import logging

log_path = "log/"


# 设置log文件路径
def set_log_path(path):
    global log_path
    log_path = path


# 设置Model的logConfig
def set_model_logConfig():
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logging.basicConfig(
        filename=log_path + "model.log",
        filemode="a+",
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=logging.INFO
    )


# 设置Database的logConfig
def set_event_logConfig():
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logging.basicConfig(
        filename=log_path + "event.log",
        filemode="a+",
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=logging.INFO
    )


# 设置Scrapper的logConfig
def set_scrapper_logConfig():
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    logging.basicConfig(
        filename=log_path + "scrapper.log",
        filemode="a+",
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
        level=logging.INFO
    )


# 获取对应的logger
def get_logger(log_name):
    logger = logging.getLogger(log_name)
    return logger
