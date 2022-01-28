# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: buildModel.py
@time: 2021/7/11 20:00
"""
import random

from classes.Feature.Bert import *
from utils.model.functionsUtils import fine_grade_tokenize, getRole2id


class BaseExample:
    """A single training/test example for simple sequence classification."""

    def __init__(self, text):
        self.text = text
        self.role2id = {
            "O": 0,
            "B-object": 1,
            "B-subject": 2,
            "B-time": 3,
            "B-loc": 4,
            "B-country": 5,
            "B-weapon": 6,
            "I-object": 7,
            "I-subject": 8,
            "I-time": 9,
            "I-loc": 10,
            "I-country": 11,
            "I-weapon": 12,
            "E-object": 13,
            "E-subject": 14,
            "E-time": 15,
            "E-country": 16,
            "E-weapon": 17,
            "E-loc": 18,
            "S-object": 19,
            "S-subject": 20,
            "S-time": 21,
            "S-loc": 22,
            "S-country": 23,
            "S-weapon": 24,
            "X": 25
        }


class BertTriggerExample(BaseExample):
    def __init__(self,
                 text,
                 weapon,
                 triggers):
        super(BertTriggerExample, self).__init__(text=text)
        self.weapon = weapon
        self.triggers = triggers

    def toTriggerFeature(self, tokenizer, logger, max_seq_len):
        """
        convert trigger examples to trigger features
        """
        tokens = fine_grade_tokenize(self.text, tokenizer)

        labels = [[0] * 2 for i in range(len(tokens))]  # start / end
        role_start = int(self.weapon['offset'])
        role_end = role_start + len(self.weapon['text'])
        weapon_start = role_start
        weapon_end = role_end

        weapon_label = [weapon_start, weapon_end]

        # tag labels
        if self.triggers is not None:
            for trigger in self.triggers:
                tmp_start = int(trigger['offset'])
                tmp_end = int(trigger['offset']) + int(trigger['length']) - 1

                labels[tmp_start][0] = 1
                labels[tmp_end][1] = 1

        if len(labels) > max_seq_len - 2:
            labels = labels[:max_seq_len - 2]

        pad_labels = [[0] * 2]
        labels = pad_labels + labels + pad_labels

        if len(labels) < max_seq_len:
            pad_length = max_seq_len - len(labels)

            labels = labels + pad_labels * pad_length

        average_distance = [511] * max_seq_len

        assert len(labels) == max_seq_len

        encode_dict = tokenizer.encode_plus(text=tokens,
                                            max_length=max_seq_len,
                                            pad_to_max_length=True,
                                            is_pretokenized=True,
                                            return_token_type_ids=True,
                                            return_attention_mask=True)

        token_ids = encode_dict['input_ids']
        attention_masks = encode_dict['attention_mask']
        token_type_ids = encode_dict['token_type_ids']
        for i in range(max_seq_len):
            tmp_distance = 0
            if i < weapon_start:
                tmp_distance = weapon_start - i
            elif i > weapon_end:
                tmp_distance = i - weapon_end
            average_distance[i] = tmp_distance
        for i in range(weapon_start, weapon_end + 1):
            token_type_ids[i] = 1

        feature = BertTriggerFeature(token_ids=token_ids,
                                     attention_masks=attention_masks,
                                     token_type_ids=token_type_ids,
                                     weapon_label=weapon_label,
                                     average_distance=average_distance,
                                     labels=labels)
        return feature


class BertRoleExample(BaseExample):
    def __init__(self,
                 text,
                 terms):
        super(BertRoleExample, self).__init__(text=text)
        self.terms = terms

    def toCountryFeature(self, mode, tokenizer, logger, max_seq_len):
        """
        将example通过Bert_tokenizer编码成对应的Feature
        """
        role2id = getRole2id("Country")
        tokens = fine_grade_tokenize(self.text, tokenizer)

        labels = [0] * len(tokens)  # time / loc

        # tag labels
        roles = self.terms['country']
        for role in roles:
            role_start = role['offset']
            role_end = role_start + len(role['text']) - 1

            if role_start == role_end:
                labels[role_start] = role2id['S-country']
            else:
                labels[role_start] = role2id['B-country']
                labels[role_end] = role2id['E-country']
                for i in range(role_start + 1, role_end):
                    labels[i] = role2id['I-country']

        # 负样本以一定概率剔除，保证类别均衡，增大后续召回率
        if mode == 'train' and len(roles) == 0 and random.random() > 0.3:
            return None

        if len(labels) > max_seq_len - 2:
            labels = labels[:max_seq_len - 2]

        pad_labels = [role2id['O']]
        labels = [role2id['X']] + labels + [role2id['X']]

        if len(labels) < max_seq_len:
            pad_length = max_seq_len - len(labels)
            labels = labels + pad_labels * pad_length

        assert len(labels) == max_seq_len

        encode_dict = tokenizer.encode_plus(text=tokens,
                                            max_length=max_seq_len,
                                            pad_to_max_length=True,
                                            is_pretokenized=True,
                                            return_token_type_ids=True,
                                            return_attention_mask=True)

        token_ids = encode_dict['input_ids']
        attention_masks = encode_dict['attention_mask']
        token_type_ids = encode_dict['token_type_ids']

        feature = BertFeature(token_ids=token_ids,
                              attention_masks=attention_masks,
                              token_type_ids=token_type_ids,
                              labels=labels)
        return feature

    def toSubObjFeature(self, mode, tokenizer, logger, max_seq_len):
        """
        将example通过Bert_tokenizer编码成对应的Feature
        """
        Subject = self.terms['subject']
        Object = self.terms['object']
        trigger = self.terms['trigger']
        if trigger == "":
            return None
        tmp_trigger_start = trigger['offset']
        tmp_trigger_end = trigger['offset'] + len(trigger['text']) - 1
        if (tmp_trigger_start < 0) or (tmp_trigger_end >= 320):
            logger.info('Skip this example where the tag is longer than max sequence length')
            return None
        trigger_loc = [tmp_trigger_start, tmp_trigger_end]

        if mode == 'train' and trigger_loc[0] > max_seq_len:
            logger.info('Skip this example where the tag is longer than max sequence length')
            return None

        tokens = fine_grade_tokenize(self.text, tokenizer)

        labels = [[0] * 4 for i in range(len(tokens))]  # sub / obj

        # tag labels
        if Object != "":
            role_start = Object['offset']
            role_end = role_start + len(Object['text']) - 1

            labels[role_start][0] = 1  # start 位置标注为 1
            labels[role_end][1] = 1  # end 位置标注为 1

        if Subject != "":
            role_start = Subject['offset']
            role_end = role_start + len(Subject['text']) - 1

            labels[role_start][2] = 1  # start 位置标注为 1
            labels[role_end][3] = 1  # end 位置标注为 1

        if mode == 'train' and (Object == "" or Subject == ""):
            return None

        if len(labels) > max_seq_len - 2:
            labels = labels[:max_seq_len - 2]

        pad_labels = [[0] * 4]
        labels = pad_labels + labels + pad_labels

        if len(labels) < max_seq_len:
            pad_length = max_seq_len - len(labels)
            labels = labels + pad_labels * pad_length

        # build trigger distance features
        trigger_distance = [511] * max_seq_len
        for i in range(max_seq_len):
            if trigger_loc[0] <= i <= trigger_loc[1]:
                trigger_distance[i] = 0
                continue
            elif i < trigger_loc[0]:
                trigger_distance[i] = trigger_loc[0] - i
            else:
                trigger_distance[i] = i - trigger_loc[1]

        assert len(labels) == max_seq_len

        encode_dict = tokenizer.encode_plus(text=tokens,
                                            max_length=max_seq_len,
                                            pad_to_max_length=True,
                                            is_pretokenized=True,
                                            return_token_type_ids=True,
                                            return_attention_mask=True)

        token_ids = encode_dict['input_ids']
        attention_masks = encode_dict['attention_mask']
        token_type_ids = encode_dict['token_type_ids']

        for i in range(trigger_loc[0], trigger_loc[1] + 1):
            token_type_ids[i] = 1

        feature = BertSubObjFeature(token_ids=token_ids,
                                    attention_masks=attention_masks,
                                    token_type_ids=token_type_ids,
                                    trigger_loc=trigger_loc,
                                    trigger_distance=trigger_distance,
                                    labels=labels)
        return feature

    def toTimeLocFeature(self, mode, tokenizer, logger, max_seq_len):
        """
        将example通过Bert_tokenizer编码成对应的Feature
        """
        role2id = getRole2id("TimeLoc")
        Times = self.terms['time']
        Locs = self.terms['loc']
        tokens = fine_grade_tokenize(self.text, tokenizer)

        labels = [0] * len(tokens)  # time / loc

        # tag labels
        for role in Times:

            role_start = role['offset']
            role_end = role_start + len(role['text']) - 1

            if role_start == role_end:
                labels[role_start] = role2id['S-time']
            else:
                labels[role_start] = role2id['B-time']
                labels[role_end] = role2id['E-time']
                for i in range(role_start + 1, role_end):
                    labels[i] = role2id['I-time']
        for role in Locs:

            role_start = role['offset']
            role_end = role_start + len(role['text']) - 1

            if role_start == role_end:
                labels[role_start] = role2id['S-loc']
            else:
                labels[role_start] = role2id['B-loc']
                labels[role_end] = role2id['E-loc']
                for i in range(role_start + 1, role_end):
                    labels[i] = role2id['I-loc']

        # 负样本以一定概率剔除，保证类别均衡，增大后续召回率
        if mode == 'train' and (len(Times) == 0 or len(Locs) == 0) and random.random() > 0.3:
            return None

        if len(labels) > max_seq_len - 2:
            labels = labels[:max_seq_len - 2]

        pad_labels = [role2id['O']]
        labels = [role2id['X']] + labels + [role2id['X']]

        if len(labels) < max_seq_len:
            pad_length = max_seq_len - len(labels)
            labels = labels + pad_labels * pad_length

        assert len(labels) == max_seq_len

        encode_dict = tokenizer.encode_plus(text=tokens,
                                            max_length=max_seq_len,
                                            pad_to_max_length=True,
                                            is_pretokenized=True,
                                            return_token_type_ids=True,
                                            return_attention_mask=True)

        token_ids = encode_dict['input_ids']
        attention_masks = encode_dict['attention_mask']
        token_type_ids = encode_dict['token_type_ids']

        feature = BertFeature(token_ids=token_ids,
                              attention_masks=attention_masks,
                              token_type_ids=token_type_ids,
                              labels=labels)
        return feature

    def toWeaponFeature(self, mode, tokenizer, logger, max_seq_len):
        """
        将example通过Bert_tokenizer编码成对应的Feature
        """
        role2id = getRole2id("Weapon")
        tokens = fine_grade_tokenize(self.text, tokenizer)

        labels = [0] * len(tokens)  # time / loc

        # tag labels
        roles = self.terms['weapon']
        for role in roles:
            role_start = role['offset']
            role_end = role_start + len(role['text']) - 1

            if role_start == role_end:
                labels[role_start] = role2id['S-weapon']
            else:
                labels[role_start] = role2id['B-weapon']
                labels[role_end] = role2id['E-weapon']
                for i in range(role_start + 1, role_end):
                    labels[i] = role2id['I-weapon']

        # 负样本以一定概率剔除，保证类别均衡，增大后续召回率
        if mode == 'train' and len(roles) == 0 and random.random() > 0.3:
            return None

        if len(labels) > max_seq_len - 2:
            labels = labels[:max_seq_len - 2]

        pad_labels = [role2id['O']]
        labels = [role2id['X']] + labels + [role2id['X']]

        if len(labels) < max_seq_len:
            pad_length = max_seq_len - len(labels)
            labels = labels + pad_labels * pad_length

        assert len(labels) == max_seq_len

        encode_dict = tokenizer.encode_plus(text=tokens,
                                            max_length=max_seq_len,
                                            pad_to_max_length=True,
                                            is_pretokenized=True,
                                            return_token_type_ids=True,
                                            return_attention_mask=True)

        token_ids = encode_dict['input_ids']
        attention_masks = encode_dict['attention_mask']
        token_type_ids = encode_dict['token_type_ids']

        feature = BertFeature(token_ids=token_ids,
                              attention_masks=attention_masks,
                              token_type_ids=token_type_ids,
                              labels=labels)
        return feature


class BertAttributionExample(BaseExample):
    def __init__(self,
                 text,
                 trigger,
                 label=None):
        super(BertAttributionExample, self).__init__(text=text)
        self.trigger = trigger
        self.label = label

    def toAttributionFeature(self, tokenizer, logger, max_seq_len):
        """
        将example通过Bert_tokenizer编码成对应的Feature
        """
        tense = self.label["tense"]
        polarity = self.label["polarity"]
        if self.trigger == "":
            return None
        trigger = self.trigger
        tokens = fine_grade_tokenize(self.text, tokenizer)
        tmp_trigger_start = trigger['offset']
        tmp_trigger_end = trigger['offset'] + len(trigger['text'])

        if (tmp_trigger_start < 0) or (tmp_trigger_end >= 320):
            logger.info('Skip this example where the tag is longer than max sequence length')
            return None

        trigger_loc = (tmp_trigger_start + 1, tmp_trigger_end)

        tense2id = getRole2id("tense")
        polarity2id = getRole2id("polarity")

        labels = [polarity2id[polarity], tense2id[tense]]

        encode_dict = tokenizer.encode_plus(text=tokens,
                                            max_length=max_seq_len,
                                            pad_to_max_length=True,
                                            is_pretokenized=True,
                                            return_token_type_ids=True,
                                            return_attention_mask=True)

        token_ids = encode_dict['input_ids']
        attention_masks = encode_dict['attention_mask']
        token_type_ids = encode_dict['token_type_ids']

        window_size = 20

        # 左右各取 20 的窗口作为 trigger 触发的语境
        pooling_masks_range = range(max(1, trigger_loc[0] - window_size),
                                    min(min(1 + len(self.text), max_seq_len - 1), trigger_loc[1] + window_size))

        pooling_masks = [0] * max_seq_len
        for i in pooling_masks_range:
            pooling_masks[i] = 1
        for i in range(trigger_loc[0], trigger_loc[1] + 1):
            pooling_masks[i] = 0

        feature = BertAttributionFeature(token_ids=token_ids,
                                         attention_masks=attention_masks,
                                         token_type_ids=token_type_ids,
                                         trigger_loc=trigger_loc,
                                         pooling_masks=pooling_masks,
                                         labels=labels)
        return feature
