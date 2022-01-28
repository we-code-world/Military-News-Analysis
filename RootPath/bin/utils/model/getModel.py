# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: getModel.py
@time: 2021/7/11 19:47
"""
from classes.Model.Bayes import *
from classes.Model.Bert import *
from classes.Model.Cnn import *


def getBayesModel(opt):
    model_type = opt.ModelType
    assert model_type in ['Classify']
    if model_type == 'Classify':
        model = BayesClassifyModel.preModel(opt)
        return model


def getBertModel(opt, model_path):
    model_type = opt.ModelType
    assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
    if model_type == 'Trigger':
        model = BertTriggerModel.preModel(opt, model_path)
        return model
    if model_type == 'Country':
        model = BertCountryModel.preModel(opt, model_path)
        return model
    if model_type == 'TimeLoc':
        model = BertTimeLocModel.preModel(opt, model_path)
        return model
    if model_type == 'SubObj':
        model = BertSubObjModel.preModel(opt, model_path)
        return model
    if model_type == 'Weapon':
        model = BertWeaponModel.preModel(opt, model_path)
        return model
    if model_type == 'Attribution':
        model = BertAttributionModel.preModel(opt, model_path)
        return model


def getCnnModel(opt):
    model_type = opt.ModelType
    assert model_type in ['BiLSTM_CRF']
    if model_type == 'BiLSTM_CRF':
        model = BiLSTM_CRFModel.preModel(opt)
        return model
