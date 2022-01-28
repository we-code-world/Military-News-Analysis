# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: Model.py
@time: 2021/7/17 17:01
"""
from utils.logger import *
from utils.lock import *
from utils.options import ModelArgs
from model.model_train import trainModel
from model.model_evaluate import evaluateModel
from model.model_predict import startRecognize


def mainFunction():
    set_model_logConfig()
    # if process_lock("model")==False:
    #    return 0

    args = ModelArgs().get_parser()

    assert args.operation in ['train', 'evaluate', 'predict'], 'Undefined operation in Model'

    operation_func = args.operation  # 根据输入参数决定执行的操作

    if operation_func == 'train':
        trainModel(args, get_logger("train"))
    if operation_func == 'evaluate':
        evaluateModel(args, get_logger("evaluate"))
    if operation_func == 'predict':
        startRecognize(args, get_logger("predict"))

    # return unlock("model")


if __name__ == '__main__':
    mainFunction()
