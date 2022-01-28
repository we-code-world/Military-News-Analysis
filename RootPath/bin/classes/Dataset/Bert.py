# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: Dataset.py
@time: 2020/9/1 21:34
"""

import torch
from torch.utils.data import Dataset


class BertDataset(Dataset):
    def __init__(self, features, mode):
        self.nums = len(features)

        self.token_ids = [torch.tensor(example.token_ids).long() for example in features]
        self.attention_masks = [torch.tensor(example.attention_masks).float() for example in features]
        self.token_type_ids = [torch.tensor(example.token_type_ids).long() for example in features]

        self.labels = None
        if mode == 'train':
            self.labels = [torch.tensor(example.labels) for example in features]

    def __len__(self):
        return self.nums

    def __getitem__(self, index):
        data = {'token_ids': self.token_ids[index],
                'attention_masks': self.attention_masks[index],
                'token_type_ids': self.token_type_ids[index]}

        if self.labels is not None:
            data['labels'] = self.labels[index]

        return data

    def getOneData(self):
        for i in range(self.__len__()):
            yield self.__getitem__(i)

    def oneBatch(self, batch_size):
        dataset = []
        data_num = 1
        for data in self.getOneData():
            dataset.append(data)
            if data_num % batch_size == 0:
                yield dataset
                dataset = []
            data_num = data_num + 1
        if len(dataset) != 0:
            yield dataset


class BertTriggerDataset(BertDataset):
    def __init__(self,
                 features,
                 mode):
        super(BertTriggerDataset, self).__init__(features, mode)

        self.weapon_label = [torch.tensor(example.weapon_label).long() for example in features]
        self.average_distance = [torch.tensor(example.average_distance).long() for example in features]

    def __getitem__(self, index):
        data = super(BertTriggerDataset, self).__getitem__(index)
        data['weapon_label'] = self.weapon_label[index]
        if self.average_distance is not None:
            data['average_distance'] = self.average_distance[index]
        return data


class BertSubObjDataset(BertDataset):
    def __init__(self,
                 features,
                 mode):
        super(BertSubObjDataset, self).__init__(features, mode)

        self.trigger_label = [torch.tensor(example.trigger_loc).long() for example in features]
        self.trigger_distance = [torch.tensor(example.trigger_distance).long() for example in features]

    def __getitem__(self, index):
        data = super(BertSubObjDataset, self).__getitem__(index)
        data['trigger_index'] = self.trigger_label[index]
        if self.trigger_distance is not None:
            data['trigger_distance'] = self.trigger_distance[index]
        return data


class BertAttributionDataset(BertDataset):
    def __init__(self,
                 features,
                 mode):
        super(BertAttributionDataset, self).__init__(features, mode)
        self.trigger_label = [torch.tensor(example.trigger_loc).long() for example in features]

        self.pooling_masks = [torch.tensor(example.pooling_masks).float() for example in features]

    def __getitem__(self, index):
        data = super(BertAttributionDataset, self).__getitem__(index)
        data['trigger_index'] = self.trigger_label[index]
        data['pooling_masks'] = self.pooling_masks[index]
        return data

