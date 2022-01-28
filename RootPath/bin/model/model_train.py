# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022,NJUST.
@contact: 1289580847@qq.com
@file: model_train.py
@time: 2021/6/28 8:37
"""
from transformers import BertTokenizer

from utils.model.buildModel import *
from utils.model.getModel import *
from utils.dataset.getDataset import *
from utils.model.functionsUtils import save_model
from utils.model.train.trainer import train


def trainModel(opt, logger):
    logger.info("start training!")
    model_type = opt.BaseModel

    assert model_type in ['Bayes', 'Bert', 'Cnn'], 'This model type is not supported!'

    if model_type == 'Bayes':
        assert opt.newModel in ['True', 'False'], 'Illegal input newModel parameter!'
        if opt.newModel == 'True':
            model = buildBayesModel(opt)
            dataset = getBayesDataset(opt)
            train(opt, model, dataset, logger)
            save_model(model, logger)
        elif opt.newModel == 'False':
            model = getBayesModel(opt)
            dataset = getBayesDataset(opt)
            train(opt, model, dataset, logger)
            save_model(model, logger)

    if model_type == 'Bert':
        assert opt.newModel in ['True', 'False'], 'Illegal input newModel parameter!'
        tokenizer = BertTokenizer.from_pretrained(opt.BaseModelPath)
        if opt.newModel == 'True':
            model = buildBertModel(opt)
            dataset, _dataset_ = getBertDataset(opt, tokenizer, logger, 320)
            train(opt, model, dataset, logger)
        elif opt.newModel == 'False':
            model = getBertModel(opt, opt.ModelPath)
            dataset, _dataset_ = getBertDataset(opt, tokenizer, logger, 320)
            train(opt, model, dataset, logger)

    if model_type == 'Cnn':
        assert opt.newModel in ['True', 'False'], 'Illegal input newModel parameter!'
        if opt.newModel == 'True':
            model = buildCnnModel(opt)
            dataset = getCnnDataset(opt)
            train(opt, model, dataset, logger)
            save_model(model, logger)
        elif opt.newModel == 'False':
            model = getCnnModel(opt)
            dataset = getCnnDataset(opt)
            train(opt, model, dataset, logger)
            save_model(model, logger)
