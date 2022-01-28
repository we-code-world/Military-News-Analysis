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
from classes.Example.Bayes import *
from classes.Example.Bert import *
from classes.Example.Cnn import *
import json

from utils.model.functionsUtils import getLastTypeDict


def buildBayesDataset(opt):
    model_type = opt.ModelType
    assert model_type in ['Classify']
    if model_type == 'Classify':
        dataset = BayesClassifyDataset(opt)
        return dataset


def findBertDataset(mode, examples, model_type, tokenizer, logger, max_seq_len):
    """
    将所有的句子及标注内容作为example的输入，并通过对应的函数转换成对应的feature
    将获取的feature转换成对应的dataset数据集
    同时在构建example的过程中统计对应元素个数
    返回的三个值分别为构建的dataset数据集，与feature一一对应的原始数据集，所有的原始example
    """
    role_num = 0
    if model_type == 'Trigger':
        features = []
        dataset = []
        for example in examples:
            triggers = []
            weapons = example["arguments"]["weapon"]
            for event in example['events']:
                if "trigger" not in list(event.keys()):
                    example["events"].remove(event)
                else:
                    triggers.append(event['trigger'])
            for weapon in weapons:
                role_num += 1
                feature = BertTriggerExample(text=example['sentence'],
                                             weapon=weapon,
                                             triggers=triggers).toTriggerFeature(
                    tokenizer=tokenizer,
                    logger=logger,
                    max_seq_len=max_seq_len)
                if feature is not None:
                    features.append(feature)
                    dataset.append(example)
        logger.info(f"{model_type}: total trigger num is {role_num}")
        logger.info(f"{model_type}: total dataset num is {len(dataset)}")
        return BertTriggerDataset(features, mode), dataset, examples
    if model_type in ['Country', 'TimeLoc', 'Weapon']:
        features = []
        dataset = []
        for example in examples:
            arguments = example['arguments']
            Example = BertRoleExample(text=example['sentence'], terms=arguments)
            if model_type == 'Country':
                role_num += len(arguments["country"])
                feature = Example.toCountryFeature(tokenizer=tokenizer,
                                                   mode=mode,
                                                   logger=logger,
                                                   max_seq_len=max_seq_len)
                if feature is not None:
                    features.append(feature)
                    dataset.append(example)
            elif model_type == 'TimeLoc':
                role_num += len(arguments["time"]) + len(arguments["loc"])
                feature = Example.toTimeLocFeature(tokenizer=tokenizer,
                                                   mode=mode,
                                                   logger=logger,
                                                   max_seq_len=max_seq_len)
                if feature is not None:
                    features.append(feature)
                    dataset.append(example)
            elif model_type == 'Weapon':
                role_num += len(arguments["weapon"])
                feature = Example.toWeaponFeature(tokenizer=tokenizer,
                                                  mode=mode,
                                                  logger=logger,
                                                  max_seq_len=max_seq_len)
                if feature is not None:
                    features.append(feature)
                    dataset.append(example)
        logger.info(f"{model_type}: total item num is {role_num}")
        logger.info(f"{model_type}: total dataset num is {len(dataset)}")
        return BertDataset(features, mode), dataset, examples
    if model_type == 'SubObj':
        features = []
        dataset = []
        for example in examples:
            for event in example['events']:
                if event["subject"]["text"] != "":
                    role_num += 1
                if event["object"]["text"] != "":
                    role_num += 1
                feature = BertRoleExample(text=example['sentence'], terms=event).toSubObjFeature(
                    tokenizer=tokenizer,
                    mode=mode,
                    logger=logger,
                    max_seq_len=max_seq_len)
                if feature is not None:
                    features.append(feature)
                    dataset.append(example)
        logger.info(f"{model_type}: total item num is {role_num}")
        logger.info(f"{model_type}: total dataset num is {len(dataset)}")
        return BertSubObjDataset(features, mode), dataset, examples
    if model_type == 'Attribution':
        features = []
        dataset = []
        for example in examples:
            for event in example['events']:
                role_num += 2
                if "labels" not in list(event.keys()):
                    event['labels'] = {"tense": "其他", "polarity": "可能"}
                feature = BertAttributionExample(text=example['sentence'],
                                                 trigger=event['trigger'],
                                                 label=event['labels']).toAttributionFeature(
                    tokenizer=tokenizer,
                    logger=logger,
                    max_seq_len=max_seq_len)
                if feature is not None:
                    features.append(feature)
                    dataset.append(example)
        logger.info(f"{model_type}: total item num is {role_num}")
        logger.info(f"{model_type}: total dataset num is {len(dataset)}")
        return BertAttributionDataset(features, mode), dataset, examples


def buildBertDataset(opt, tokenizer, model_type, fileName, logger, max_seq_len):
    mode = opt.operation
    # 判断模型类型是否正确
    assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
    # 根据模型类型确定读取的原始文件位置
    f = open(fileName, "r", encoding='utf-8')
    examples = json.load(f)
    return findBertDataset(mode, examples, model_type, tokenizer, logger, max_seq_len)


def buildCnnDataset(opt):
    model_type = opt.ModelType
    assert model_type in ['BiLSTM_CRF']
    if model_type == 'BiLSTM_CRF':
        dataset = BiLSTM_CRFDataset(opt)
        return dataset
