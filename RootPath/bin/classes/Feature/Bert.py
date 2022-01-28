# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: buildModel.py
@time: 2021/7/11 20:00
"""


class BertFeature:
    """A single set of features of event."""

    def __init__(self,
                 token_ids,
                 attention_masks,
                 token_type_ids,
                 labels=None):
        self.token_ids = token_ids
        self.attention_masks = attention_masks
        self.token_type_ids = token_type_ids
        self.labels = labels


class BertTriggerFeature(BertFeature):

    def __init__(self,
                 token_ids,
                 attention_masks,
                 token_type_ids,
                 weapon_label,
                 average_distance=None,
                 labels=None):
        super(BertTriggerFeature, self).__init__(token_ids=token_ids,
                                                 attention_masks=attention_masks,
                                                 token_type_ids=token_type_ids,
                                                 labels=labels)
        self.weapon_label = weapon_label
        self.average_distance = average_distance


class BertSubObjFeature(BertFeature):

    def __init__(self,
                 token_ids,
                 attention_masks,
                 token_type_ids,
                 trigger_loc,
                 trigger_distance=None,
                 labels=None):
        super(BertSubObjFeature, self).__init__(token_ids=token_ids,
                                                attention_masks=attention_masks,
                                                token_type_ids=token_type_ids,
                                                labels=labels)
        self.trigger_distance = trigger_distance
        self.trigger_loc = trigger_loc


class BertAttributionFeature(BertFeature):

    def __init__(self,
                 token_ids,
                 attention_masks,
                 token_type_ids,
                 trigger_loc,
                 pooling_masks,
                 labels=None):
        super(BertAttributionFeature, self).__init__(token_ids=token_ids,
                                                     attention_masks=attention_masks,
                                                     token_type_ids=token_type_ids,
                                                     labels=labels)
        self.trigger_loc = trigger_loc
        self.pooling_masks = pooling_masks
