# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: buildModel.py
@time: 2021/7/11 20:01
"""
from classes.Dataset.Cnn import *
from utils.file.path import getModelPath


class BiLSTM_CRFModel:
    model_save_path = ''

    def __init__(self, opt):
        self.model_save_path = opt.Rootpath + "/model/Cnn/BiLSTM_CRF"

    @staticmethod
    def preModel(opt):
        pass

    def train(self, dataset: BiLSTM_CRFDataset):
        pass

    def save(self):
        save_path = getModelPath(self.model_save_path)
