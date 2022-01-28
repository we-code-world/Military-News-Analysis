# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: buildModel.py
@time: 2021/7/11 19:46
"""

from classes.Model.Bayes import *
from classes.Model.Bert import *
from classes.Model.Cnn import *


def buildBayesModel(opt):
    model_type = opt.ModelType
    assert model_type in ['Classify']
    if model_type == 'Classify':
        model = BayesClassifyModel(opt)
        return model


def buildBertModel(opt):
    model_type = opt.ModelType
    assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
    if model_type == 'Trigger':
        model = BertTriggerModel(opt)
        return model
    if model_type == 'Country':
        model = BertCountryModel(opt)
        return model
    if model_type == 'TimeLoc':
        model = BertTimeLocModel(opt)
        return model
    if model_type == 'SubObj':
        model = BertSubObjModel(opt)
        return model
    if model_type == 'Weapon':
        model = BertWeaponModel(opt)
        return model
    if model_type == 'Attribution':
        model = BertAttributionModel(opt)
        return model


def buildCnnModel(opt):
    model_type = opt.ModelType
    assert model_type in ['BiLSTM_CRF']
    if model_type == 'BiLSTM_CRF':
        model = BiLSTM_CRFModel(opt)
        return model
