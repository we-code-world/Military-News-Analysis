# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: Model.py
@time: 2021/7/6 21:19
"""
from classes.Dataset.Bayes import *
from utils.file.path import getModelPath


class BayesClassifyModel:
    model_save_path = ''

    def __init__(self, opt):
        self.model_save_path = opt.Rootpath + "/model/Bayes/Classify"

    @staticmethod
    def preModel(opt):
        pass

    def train(self, dataset: BayesClassifyDataset):
        pass

    def save(self):
        save_path = getModelPath(self.model_save_path)
