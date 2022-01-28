# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: getModel.py
@time: 2021/7/11 19:49
"""
from classes.Dataset.Bayes import *
from classes.Dataset.Bert import *
from classes.Dataset.Cnn import *
from utils.dataset.buildDataset import findBertDataset
import json


def getBayesDataset(opt):
    model_type = opt.ModelType
    assert model_type in ['Classify']
    if model_type == 'Classify':
        dataset = BayesClassifyDataset(opt)
        return dataset


def getBertDataset(opt, tokenizer, logger, max_seq_len):
    model_type = opt.ModelType
    mode = opt.operation
    # 判断模型类型是否正确
    assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
    # 根据操作选择训练集合评估集
    f = open(opt.ExamplePath + "/" + opt.operation + "/event.json", encoding='utf-8')
    examples = json.load(f)
    logger.info(f"total sentence examples num is {len(examples)}")
    f.close()
    dataset, examples, _ = findBertDataset(mode, examples, model_type, tokenizer, logger, max_seq_len)
    return dataset, examples


def getCnnDataset(opt):
    model_type = opt.ModelType
    assert model_type in ['BiLSTM_CRF']
    if model_type == 'BiLSTM_CRF':
        dataset = BiLSTM_CRFDataset(opt)
        return dataset
