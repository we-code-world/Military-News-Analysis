# coding=utf-8
"""
@author: Oscar
@license: (C) Copyright 2019-2022, ZJU.
@contact: 499616042@qq.com
@software: pycharm
@file: functions_utils.py
@time: 2020/9/3 11:14
"""
import os
import copy
from torch.utils.data import DataLoader
from utils.file.path import getPathListByName
from transformers import AdamW, get_linear_schedule_with_warmup
import torch
import random
import numpy as np
from tqdm import tqdm


def set_seed(seed):
    """
    设置随机种子
    :param seed:
    :return:
    """
    random.seed(seed)
    torch.manual_seed(seed)
    np.random.seed(seed)
    torch.cuda.manual_seed_all(seed)


#  下面几个函数均为字典，作为解码编码的字典使用
def getRole2id(role):
    role2id = {}
    assert role in ['Country', 'TimeLoc', 'Weapon', "tense", "polarity"]
    if role == 'Country':
        role2id = {
            "O": 0,
            "B-country": 1,
            "I-country": 2,
            "E-country": 3,
            "S-country": 4,
            "X": 5
        }
    if role == 'TimeLoc':
        role2id = {
            "O": 0,
            "B-time": 1,
            "B-loc": 2,
            "I-time": 3,
            "I-loc": 4,
            "E-time": 5,
            "E-loc": 6,
            "S-time": 7,
            "S-loc": 8,
            "X": 9
        }
    if role == 'Weapon':
        role2id = {
            "O": 0,
            "B-weapon": 1,
            "I-weapon": 2,
            "E-weapon": 3,
            "S-weapon": 4,
            "X": 5
        }
    if role == 'tense':
        role2id = {
            "过去": 0,
            "将来": 1,
            "其他": 2,
            "现在": 3
        }
    if role == 'polarity':
        role2id = {
            "肯定": 0,
            "可能": 1,
            "否定": 2
        }

    return role2id


def getId2role(role):
    id2role = {}
    assert role in ['Country', 'TimeLoc', 'Weapon', "tense", "polarity"]
    if role == 'Country':
        id2role = {
            0: "O",
            1: "B-country",
            2: "I-country",
            3: "E-country",
            4: "S-country",
            5: "X"
        }
    if role == 'TimeLoc':
        id2role = {
            0: "O",
            1: "B-time",
            2: "B-loc",
            3: "I-time",
            4: "I-loc",
            5: "E-time",
            6: "E-loc",
            7: "S-time",
            8: "S-loc",
            9: "X"
        }
    if role == 'Weapon':
        id2role = {
            0: "O",
            1: "B-weapon",
            2: "I-weapon",
            3: "E-weapon",
            4: "S-weapon",
            5: "X"
        }
    if role == 'tense':
        id2role = {
            0: "过去",
            1: "将来",
            2: "其他",
            3: "现在"
        }
    if role == 'polarity':
        id2role = {
            0: "肯定",
            1: "可能",
            2: "否定"
        }

    return id2role


def getLastTypeDict():
    rtn_dict = {
        "Weapon": "empty",
        "Country": "Weapon",
        "TimeLoc": "Country",
        "Trigger": "TimeLoc",
        "SubObj": "Trigger",
        "Attribution": "SubObj"
    }
    return rtn_dict


def fine_grade_tokenize(raw_text, tokenizer):
    """
    序列标注任务 BERT 分词器可能会导致标注偏移，
    用 char-level 来 tokenize
    """
    tokens = []

    for _ch in raw_text:
        if _ch in [' ', '\t', '\n']:
            tokens.append('[BLANK]')
        else:
            if not len(tokenizer.tokenize(_ch)):
                tokens.append('[INV]')
            else:
                tokens.append(_ch)

    return tokens


def search_label_index(tokens, label_tokens):
    """
    search label token indexes in all tokens
    :param tokens: tokens for raw text
    :param label_tokens: label which are split by the cjk extractor
    :return:
    """
    index_list = []  # 存放搜到的所有的index

    # 滑动窗口搜索 labels 在 token 中的位置
    for index in range(len(tokens) - len(label_tokens) + 1):
        if tokens[index: index + len(label_tokens)] == label_tokens:
            start_index = index
            end_index = start_index + len(label_tokens) - 1
            index_list.append((start_index, end_index))

    return index_list


# 将模型加载进gpu
def load_model_on_gpu(model, logger, gpu_ids="0"):
    """
    加载模型 & 放置到 GPU 中（单卡 / 多卡）
    """
    gpu_ids = gpu_ids.split(',')
    # set model to the first cuda
    device = torch.device("cuda:" + gpu_ids[0])
    model.to(device)
    if len(gpu_ids) > 1:
        logger.info(f'Use multi gpus in: {gpu_ids}')
        gpu_ids = [int(x) for x in gpu_ids]
        model = torch.nn.DataParallel(model, device_ids=gpu_ids)
    else:
        logger.info(f'Use single gpu in: {gpu_ids}')
    return model, device


# 将模型加载进cpu
def load_model_on_cpu(model, logger):
    """
    加载模型 & 放置到 GPU 中（单卡 / 多卡）
    """
    # set to device to cpu
    device = torch.device("cpu")
    model.to(device)
    logger.info(f'Load model on cpu')
    return model, device


def build_optimizer_and_scheduler(opt, model, t_total):
    module = (
        model.module if hasattr(model, "module") else model
    )

    # 差分学习率
    no_decay = ["bias", "LayerNorm.weight"]
    model_param = list(module.named_parameters())

    bert_param_optimizer = []
    other_param_optimizer = []

    for name, para in model_param:
        space = name.split('.')
        if space[0] == 'bert_module':
            bert_param_optimizer.append((name, para))
        else:
            other_param_optimizer.append((name, para))

    optimizer_grouped_parameters = [
        # bert other module
        {"params": [p for n, p in bert_param_optimizer if not any(nd in n for nd in no_decay)],
         "weight_decay": opt.weight_decay, 'lr': opt.learnRate},
        {"params": [p for n, p in bert_param_optimizer if any(nd in n for nd in no_decay)],
         "weight_decay": 0.0, 'lr': opt.learnRate},

        # 其他模块，差分学习率
        {"params": [p for n, p in other_param_optimizer if not any(nd in n for nd in no_decay)],
         "weight_decay": opt.weight_decay, 'lr': opt.otherLearnRate},
        {"params": [p for n, p in other_param_optimizer if any(nd in n for nd in no_decay)],
         "weight_decay": 0.0, 'lr': opt.otherLearnRate},
    ]

    optimizer = AdamW(optimizer_grouped_parameters, lr=opt.learnRate, eps=opt.adam_epsilon)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=int(opt.warmup_proportion * t_total), num_training_steps=t_total
    )

    return optimizer, scheduler


def getModelOut(model, loader, device, task_type):
    """
    每一个任务的 forward 都一样，封装起来
    """
    assert task_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution'], \
        f'{task_type} is not a supported task !'

    model.eval()

    with torch.no_grad():
        for idx, one_batch in enumerate(tqdm(loader, desc=f'Get {task_type} task predict encoded output')):

            for key in one_batch.keys():
                one_batch[key] = one_batch[key].to(device)

            out = model(**one_batch)

            yield out


#  将模型预测结果预处理后返回，统一进行解码
def getPredict(opt, model, dataset, logger):
    loader = DataLoader(dataset=dataset,
                        batch_size=opt.batch_size,
                        shuffle=False,
                        num_workers=8)
    model, device = load_model_on_cpu(model, logger)

    predict_output = None
    model_type = opt.ModelType
    for tmp_predict in getModelOut(model, loader, device, opt.ModelType):
        assert model_type in ['Trigger', 'Country', 'TimeLoc', 'SubObj', 'Weapon', 'Attribution']
        if model_type == 'Trigger':
            tmp_predict = tmp_predict[0].cpu().numpy()

            if predict_output is None:
                predict_output = tmp_predict
            else:
                predict_output = np.append(predict_output, tmp_predict, axis=0)
        if model_type in ['Country', 'TimeLoc', 'Weapon']:
            if predict_output is None:
                predict_output = []
                predict_output.extend(tmp_predict[0])
            else:
                predict_output.extend(tmp_predict[0])
        if model_type == 'SubObj':
            tmp_predict = tmp_predict[0].cpu().numpy()

            if predict_output is None:
                predict_output = tmp_predict
            else:
                predict_output = np.append(predict_output, tmp_predict, axis=0)
        if model_type == 'Attribution':
            tmp_polarity_output, tmp_tense_output = tmp_predict

            tmp_polarity_output = tmp_polarity_output.cpu().numpy()
            tmp_tense_output = tmp_tense_output.cpu().numpy()

            if predict_output is None:
                predict_output = []
                for each_polarity, each_tense in zip(tmp_polarity_output, tmp_tense_output):
                    predict_output.append([each_polarity, each_tense])
            else:
                for each_polarity, each_tense in zip(tmp_polarity_output, tmp_tense_output):
                    predict_output.append([each_polarity, each_tense])
    return predict_output


#  crf解码，进行最严格的解码
def decodeCrf(tokens, text, id_label):
    """
    CRF 解码，用于解码 time loc weapon country的提取
    """
    predict_entities = {"time": [], "loc": [], "weapon": [], "country": []}
    token_type = ""
    tmp_entity = ""
    offset = 0
    length = 0

    for index in range(len(tokens)):

        token_label = id_label[tokens[index]]

        if token_label[0] in ["S", "B"]:
            token_type = token_label.split("-")[1]
            tmp_entity = text[index]
            offset = index
            length = 1
            if token_label[0] == "B":
                continue

        elif token_label[0] in ["I", "E"] and token_type == token_label.split("-")[1]:
            tmp_entity += text[index]
            length += 1
            if token_label[0] == "I":
                continue

        else:
            tmp_entity = ""
            offset = 0
            length = 0
            continue

        predict_entities[token_type].append({"text": tmp_entity, "offset": offset, "length": length})
        tmp_entity = ""
        offset = 0
        length = 0

    return predict_entities


#  解码触发词
def decodeTrigger(tokens, text, start_threshold=0.5, end_threshold=0.5):
    candidate_entities = []

    start_ids = np.argwhere(tokens[:, 0] > start_threshold)[:, 0]
    end_ids = np.argwhere(tokens[:, 1] > end_threshold)[:, 0]

    # 选长度小于5且相对最长的
    for start_id in start_ids:
        for end_id in end_ids:
            if 0 < (end_id - start_id) < 5:
                # (text, start, end)
                candidate_entities.append((text[start_id: end_id + 1], start_id, end_id,
                                           tokens[start_id][0] + tokens[end_id][1]))

    triggers = []
    entities = []

    #  找到最长的所有触发词，并且确保结果不会重叠
    if len(candidate_entities):
        candidate_entities = sorted(candidate_entities, key=lambda x: (x[2], x[1]), reverse=True)
        candidate_entities = sorted(candidate_entities, key=lambda x: x[3])
        for length in range(4, 0, -1):
            for entity in candidate_entities:
                if len(entity[0]) == length:
                    if len(entities) == 0:
                        entities.append(entity)
                    else:
                        for trigger in entities:
                            if trigger[2] <= entity[1] or trigger[2] <= entity[1]:
                                entities.append(entity)

        for trigger in entities:
            triggers.append({"text": trigger[0], "offset": int(trigger[1]), "length": len(trigger[0])})

    return triggers


def decodeSubObj(tokens, text, trigger, start_threshold=0.5, end_threshold=0.5):
    """
    :param trigger:     触发词，只有包含触发词的句子才能解码主客体
    :param tokens:      sub / obj 最后输出的 tokens，第一行为 start 第二行为 end
    :param text:        原始文本
    :param start_threshold: tokens start 位置大于阈值即可解码
    :param end_threshold:   tokens end 位置大于阈值即可解码
    :return:
    [{"subject:"{text, offset, length},"trigger:"{text, offset, length},"object:"{text, offset, length}},...]
    """
    end_min = trigger["offset"]
    start_max = trigger["offset"] + trigger["length"]

    # 选距离触发词最近的、最长的作为输出
    def getRole(start_ids, end_ids):
        my_role = {}
        left = []
        right = []
        term = (0, 0)

        for start_id in start_ids:
            for end_id in end_ids:
                if end_min > end_id > start_id:
                    left.append((start_id, end_id))
                elif end_id > start_id > start_max:
                    right.append((start_id, end_id))

        if len(left) == 0 and len(right) == 0:
            my_role["text"] = ""
            my_role["offset"] = 0
            my_role["length"] = 0
        else:
            if len(left) == 0:
                sorted(right, key=lambda x: (0 - x[1], x[0]))
                term = right[0]
            elif len(right) == 0:
                sorted(left, key=lambda x: (0 - x[0], x[1]))
                term = left[0]
            else:
                sorted(left, key=lambda x: (0 - x[0], x[1]))
                sorted(right, key=lambda x: (0 - x[1], x[0]))
                if end_min - left[0][1] > right[0][0] - start_max:
                    term = right[0]
                else:
                    term = left[0]
            my_role["text"] = text[term[0]: term[1] + 1]
            my_role["offset"] = int(term[0])
            my_role["length"] = len(my_role["text"])
        return my_role

    label = {"trigger": trigger}

    get_start_ids = np.argwhere(tokens[:, 0] > start_threshold)[:, 0]
    get_end_ids = np.argwhere(tokens[:, 1] > end_threshold)[:, 0]
    label["object"] = getRole(get_start_ids, get_end_ids)
    get_start_ids = np.argwhere(tokens[:, 2] > start_threshold)[:, 0]
    get_end_ids = np.argwhere(tokens[:, 3] > end_threshold)[:, 0]
    label["subject"] = getRole(get_start_ids, get_end_ids)

    return label


def decodeAttribution(tokens, id2polarity, id2tense):
    label = {}
    predict_polarity = tokens[0]
    predict_tense = tokens[1]
    predict_polarity = id2polarity[np.argmax(predict_polarity)]
    predict_tense = id2tense[np.argmax(predict_tense)]
    label["tense"] = predict_tense
    label["polarity"] = predict_polarity
    return label


def save_model(model, global_step, logger):
    output_dir = os.path.join(model.model_save_path, 'checkpoint-{}'.format(global_step))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    model_to_save = (
        model.module if hasattr(model, "module") else model
    )
    logger.info(f'Saving checkpoint of  model to {output_dir}')
    torch.save(model_to_save.state_dict(), os.path.join(output_dir, 'model.pt'))


def swa(model, logger, swa_start=1):
    """
    swa 滑动平均模型，一般在训练平稳阶段再使用 SWA
    """
    model_path_list = getPathListByName(model.model_save_path, "model.pt")

    swa_model = copy.deepcopy(model)
    swa_n = 0.

    with torch.no_grad():
        for _ckpt in model_path_list[swa_start:]:
            logger.info(f'Load model from {_ckpt}')
            model.load_state_dict(torch.load(_ckpt, map_location=torch.device('cpu')))
            tmp_para_dict = dict(model.named_parameters())

            alpha = 1. / (swa_n + 1.)

            for name, para in swa_model.named_parameters():
                para.copy_(tmp_para_dict[name].data.clone() * alpha + para.data.clone() * (1. - alpha))

            swa_n += 1

    # use 100000 to represent swa to avoid clash
    swa_model_dir = os.path.join(model.model_save_path, f'checkpoint-100000')
    if not os.path.exists(swa_model_dir):
        os.mkdir(swa_model_dir)

    logger.info(f'Save swa model in: {swa_model_dir}')

    swa_model_path = os.path.join(swa_model_dir, 'model.pt')

    torch.save(swa_model.state_dict(), swa_model_path)

    return swa_model
