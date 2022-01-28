# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: evaluator.py
@time: 2021/7/6 21:20
"""
from utils.file.path import getFatherPath
from utils.model.functionsUtils import *


#  根据标注结果与预测结果计算tp, fp, fn,添加了标准集，作为辅助
def calculate_metric(gt, predict, standard=None):
    """
    计算 tp fp fn
    """
    tp, fp, fn = 0, 0, 0
    for entity_predict in predict:
        flag = 0
        for entity_gt in gt:
            if entity_predict in entity_gt or entity_gt in entity_predict:
                flag = 1
                tp += 1
                break
        if flag == 0:
            for entity_standard in standard:
                if entity_predict == entity_standard:
                    flag = 1
                    tp += 1
                    break
        if flag == 0:
            fp += 1

    if len(gt) > tp:
        fn = len(gt) - tp

    return np.array([tp, fp, fn])


def get_P_R_F1(tp, fp, fn):
    p = tp / (tp + fp) if tp + fp != 0 else 0
    r = tp / (tp + fn) if tp + fn != 0 else 0
    f1 = 2 * p * r / (p + r) if p + r != 0 else 0
    return np.array([p, r, f1])


#  根据类型选择不同的解码函数，并将解码结果和原始标注结果返回
def decodePredict(opt, tokens, example):
    predict_items = []
    gt_items = []
    text = example["sentence"]
    tokens = tokens[1:1 + len(text)]
    model_type = opt.ModelType
    assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
    if model_type == 'Trigger':
        events = example["events"]
        triggers = []
        for event in events:
            triggers.append(event["trigger"])
        for item in triggers:
            if item["text"] != "":
                gt_items.append(item["text"])
        triggers = decodeTrigger(tokens, text, opt.start_threshold, opt.end_threshold)
        for item in triggers:
            if item["text"] != "":
                predict_items.append(item["text"])
    if model_type == 'TimeLoc':
        arguments = example["arguments"]
        times = arguments["time"]
        locs = arguments["loc"]
        for item in times:
            if item["text"] != "":
                gt_items.append(item["text"])
        for item in locs:
            if item["text"] != "":
                gt_items.append(item["text"])
        arguments = decodeCrf(tokens, text, getId2role(model_type))
        times = arguments["time"]
        locs = arguments["loc"]
        for item in times:
            if item["text"] != "":
                predict_items.append(item["text"])
        for item in locs:
            if item["text"] != "":
                predict_items.append(item["text"])
    if model_type == 'Country':
        arguments = example["arguments"]
        countrys = arguments["country"]
        for item in countrys:
            if item["text"] != "":
                gt_items.append(item["text"])
        arguments = decodeCrf(tokens, text, getId2role(model_type))
        countrys = arguments["country"]
        for item in countrys:
            if item["text"] != "":
                predict_items.append(item["text"])
    if model_type == 'Weapon':
        arguments = example["arguments"]
        weapons = arguments["weapon"]
        for item in weapons:
            if item["text"] != "":
                gt_items.append(item["text"])
        arguments = decodeCrf(tokens, text, getId2role(model_type))
        weapons = arguments["weapon"]
        for item in weapons:
            if item["text"] != "":
                predict_items.append(item["text"])
    if model_type == 'SubObj':
        events = example["events"]
        for event in events:
            my_subject = event["subject"]
            my_object = event["object"]
            if my_subject["text"] != "":
                gt_items.append(my_subject["text"])
            if my_object["text"] != "":
                gt_items.append(my_object["text"])
            event = decodeSubObj(tokens, text, event["trigger"], opt.start_threshold, opt.end_threshold)
            my_subject = event["subject"]
            my_object = event["object"]
            if my_subject["text"] != "":
                predict_items.append(my_subject["text"])
            if my_object["text"] != "":
                predict_items.append(my_object["text"])
    if model_type == 'Attribution':
        events = example["events"]
        for event in events:
            label = event["label"]
            tense = label["tense"]
            polarity = label["polarity"]
            if tense != "":
                gt_items.append(tense)
            if polarity != "":
                gt_items.append(polarity)
            label = decodeAttribution(tokens, getId2role("tense"), getId2role("polarity"))
            tense = label["tense"]
            polarity = label["polarity"]
            if tense != "":
                predict_items.append(tense)
            if polarity != "":
                predict_items.append(polarity)
    my_write_file = open("/home/guest/Rootpath/bin/log/" + model_type + ".txt", "a+", encoding="utf-8")
    my_write_file.write("源文本：" + text + "\n")
    my_write_file.write("标注内容：" + str(gt_items) + "\n")
    my_write_file.write("预测内容：" + str(predict_items) + "\n")
    return predict_items, gt_items


#  获取模型预测结果，并计算相应的
def evaluate(opt, model, model_path, eval_dataset, examples, standard, logger):
    write_file = open(os.path.join(getFatherPath(model_path), "eval.txt"), 'a+', encoding='utf-8')
    model_type = opt.ModelType

    predict_output = getPredict(opt, model, eval_dataset, logger)
    zero_predict = 0
    tp, fp, fn = 0, 0, 0

    #  将预测结果与原始数据集合并，一一对应
    for tmp_predict, tmp_example in zip(predict_output, examples):

        predict_items, gt_items = decodePredict(opt, tmp_predict, tmp_example)

        if not len(predict_items):
            zero_predict += 1

        tmp_tp, tmp_fp, tmp_fn = calculate_metric(gt_items, predict_items, standard)

        tp += tmp_tp
        fp += tmp_fp
        fn += tmp_fn

    #  计算precision  recall  f1
    p, r, f1 = get_P_R_F1(tp, fp, fn)
    logger.info(f'{model_type}-model({model_path}): TP: {tp}  FP: {fp}  FN: {fn}')

    #  保存评估结果
    write_file.write(f'In start threshold: {opt.start_threshold}; end threshold: {opt.end_threshold}\n')
    write_file.write(f'[MIRCO] precision: {p:.4f}, recall: {r:.4f}, f1: {f1:.4f}\n')
    write_file.write(f'Zero pred nums: {zero_predict}')
    logger.info(f'{model_type}-model({model_path}): In start threshold: {opt.start_threshold}; end threshold: {opt.end_threshold}\n')
    logger.info(f'{model_type}-model({model_path}): [MIRCO] precision: {p:.4f}, recall: {r:.4f}, f1: {f1:.4f}\n')
    logger.info(f'{model_type}-model({model_path}): Zero pred nums: {zero_predict}')
    write_file.close()
