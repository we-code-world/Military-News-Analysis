# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: predictor.py
@time: 2021/7/6 21:20
"""
import json
from copy import deepcopy

from utils.model.functionsUtils import *


#  将识别结果添加到事件集合当中
def addTriggers(events: list, triggers):
    empty = {"text": "", "offset": 0, "length": 0}
    for trigger in triggers:
        addSign = True
        for event in events:
            old_trigger = event["trigger"]
            if (old_trigger["text"] == trigger["text"]) \
                    and (old_trigger["offset"] == trigger["offset"]) \
                    and (old_trigger["length"] == trigger["length"]):
                addSign = False
        if addSign:
            events.append({"trigger": trigger, "object": empty, "subject": empty})
    return events


#  将识别结果添加到原始数据集中
def addArguments(arguments, addArguments):
    rtn_arguments = {}
    times = arguments["time"]
    locs = arguments["loc"]
    countrys = arguments["country"]
    weapons = arguments["weapon"]
    addTimes = addArguments["time"]
    addLocs = addArguments["loc"]
    addCountrys = addArguments["country"]
    addWeapons = addArguments["weapon"]
    for addRole in addTimes:
        sign = True
        for role in times:
            if (role["text"] == addRole["text"]) \
                    and (role["offset"] == addRole["offset"]) \
                    and (role["length"] == addRole["length"]):
                sign = False
                break
        if sign:
            times.append(addRole)
    rtn_arguments["time"] = times
    for addRole in addLocs:
        sign = True
        for role in locs:
            if (role["text"] == addRole["text"]) \
                    and (role["offset"] == addRole["offset"]) \
                    and (role["length"] == addRole["length"]):
                sign = False
                break
        if sign:
            locs.append(addRole)
    rtn_arguments["loc"] = locs
    for addRole in addCountrys:
        sign = True
        for role in countrys:
            if (role["text"] == addRole["text"]) \
                    and (role["offset"] == addRole["offset"]) \
                    and (role["length"] == addRole["length"]):
                sign = False
                break
        if sign:
            countrys.append(addRole)
    rtn_arguments["country"] = countrys
    for addRole in addWeapons:
        sign = True
        for role in weapons:
            if (role["text"] == addRole["text"]) \
                    and (role["offset"] == addRole["offset"]) \
                    and (role["length"] == addRole["length"]):
                sign = False
                break
        if sign:
            weapons.append(addRole)
    rtn_arguments["weapon"] = weapons
    return rtn_arguments


#  对预测结果选择不同函数进行解码
def decodePredict(opt, tokens, example):
    predict_example = deepcopy(example)
    text = example["sentence"]
    model_type = opt.ModelType
    assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
    if model_type == 'Trigger':
        tokens = tokens[1:1 + len(text)]
        predict_triggers = decodeTrigger(tokens, text, opt.start_threshold, opt.end_threshold)
        predict_events = addTriggers(example["events"], predict_triggers)
        predict_example["events"] = predict_events
    if model_type in ['TimeLoc', 'Country', 'Weapon']:
        tokens = tokens[1:1 + len(text)]
        predict_arguments = decodeCrf(tokens, text, getId2role(model_type))
        predict_arguments = addArguments(example["arguments"], predict_arguments)
        predict_example["arguments"] = predict_arguments
    if model_type == 'SubObj':
        events = example["events"]
        predict_events = []
        tokens = tokens[1:1 + len(text)]
        for event in events:
            predict_event = decodeSubObj(tokens, text, event["trigger"], opt.start_threshold, opt.end_threshold)
            predict_events.append(predict_event)
        predict_example["events"] = predict_events
    if model_type == 'Attribution':
        events = example["events"]
        predict_events = []
        for event in events:
            predict_event = deepcopy(event)
            predict_label = decodeAttribution(tokens, getId2role("polarity"), getId2role("tense"))
            predict_event["labels"] = predict_label
            predict_events.append(predict_event)
        predict_example["events"] = predict_events
    return predict_example


#  预测函数，并将结果写入对应路径
def predict(opt, model, predict_dataset, examples, all_examples, out_path, logger):
    predict_output = getPredict(opt, model, predict_dataset, logger)
    predict_examples = []
    if predict_output is not None:
        #  解码预测结果，并将其与原始数据集融合
        for tmp_example, tmp_predict in zip(examples, predict_output):
            predict_example = decodePredict(opt, tmp_predict, tmp_example)
            predict_examples.append(predict_example)
    index = 0
    result_examples = []

    #  添加所有数据集，通过原始句子集进行补充，确保不会丢弃无结果句子
    examples_number = len(predict_examples)
    for all_example in all_examples:
        if index < examples_number:
            now_example = predict_examples[index]
            if all_example["sentence"] == now_example["sentence"]:
                result_examples.append(now_example)
                index += 1
                continue
        result_examples.append(all_example)
    out_file = open(out_path, "w+", encoding="utf-8")
    json.dump(result_examples, out_file)
    out_file.close()
