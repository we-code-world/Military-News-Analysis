# coding=utf-8
"""
@author: Oscar
@license: (C) Copyright 2019-2022, ZJU.
@contact: 499616042@qq.com
@software: pycharm
@file: test.py
@time: 2020/7/30 16:23
"""
from transformers import BertTokenizer
from utils.model.getModel import *
from utils.dataset.getDataset import *
from utils.model.evaluate.evaluator import evaluate
from utils.file.path import getPathListByName, getRecentModelPath
from utils.file.read import getWordList


def evaluateModel(opt, logger):
    logger.info("start evaluate!")
    model_type = opt.BaseModel

    assert model_type in ['Bayes', 'Bert', 'Cnn'], 'This model type is not supported!'

    if model_type == 'Bayes':
        model = getBayesModel(opt)
        dataset = getBayesDataset(opt)
        evaluate(opt, model, dataset, logger)

    if model_type == 'Bert':
        tokenizer = BertTokenizer.from_pretrained(opt.BaseModelPath)
        dataset, _dataset_ = getBertDataset(opt, tokenizer, logger, 320)
        model_path_list = getPathListByName(getRecentModelPath(opt.ModelPath+"/Model"), "model.pt")
        model_path_list = sorted(model_path_list, key=lambda x: (int(x.split('/')[-2].split('-')[-1])))
        standard = getWordList(opt.ResPath + "/" + opt.ModelType + ".txt")
        for idx, model_path in enumerate(model_path_list):
            logger.info(f"now model path is {model_path}")
            model = getBertModel(opt, model_path)
            evaluate(opt, model, model_path, dataset, _dataset_, standard, logger)

    if model_type == 'Cnn':
        model = getCnnModel(opt)
        dataset = getCnnDataset(opt)
        evaluate(opt, model, dataset, logger)
