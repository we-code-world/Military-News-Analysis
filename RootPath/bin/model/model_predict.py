# coding=utf-8
"""
@author: Oscar
@license: (C) Copyright 2019-2022, ZJU.
@contact: 499616042@qq.com
@software: pycharm
@file: ensemble_predict.py
@time: 2020/9/18 20:04
"""
from transformers import BertTokenizer
from utils.model.getModel import *
from utils.dataset.buildDataset import *
from utils.model.predict.predicter import predict
from utils.file.path import getPathListByName, getRecentModelPath, getPathListBySuffix
from utils.model.functionsUtils import getLastTypeDict


def startRecognize(opt, logger):
    logger.info("start runing!")
    model_type = opt.BaseModel

    assert model_type in ['Bayes', 'Bert', 'Cnn'], 'This model type is not supported!'

    if model_type == 'Bayes':
        model = getBayesModel(opt)
        dataset = buildBayesDataset(opt)
        predict(opt, model, dataset, logger)

    if model_type == 'Bert':
        tokenizer = BertTokenizer.from_pretrained(opt.BaseModelPath)
        all_model_base_path = opt.RootPath + "/model/Bert_"
        lastType_dict = getLastTypeDict()
        for model_for in ['Weapon', 'Country', 'TimeLoc', 'Trigger', 'SubObj', 'Attribution']:
            opt.ModelType = model_for
            read_path = opt.ExamplePath + f"/{opt.operation}/{lastType_dict[model_for]}"
            model = getBertModel(opt, all_model_base_path + model_for + "/model.pt")
            pathList = getPathListBySuffix(read_path, "json")
            years = []
            pathListOfYear = {}  # 将相对路径按年份分开存储
            for each_path in pathList:
                path_pieces = each_path.split("/")  # 路径为绝对路径，最后部分为 /{year}/json/{id}.json
                year = path_pieces[-3]
                if year not in years:
                    years.append(year)
                    pathListOfYear[year] = []
                pathListOfYear[year].append((path_pieces[-2], path_pieces[-1].split(".")[0]))
            for yearFolder in years:
                for folder, fileName in pathListOfYear[yearFolder]:
                    out_path = opt.ExamplePath + f"/{opt.operation}/{model_for}/{yearFolder}/{folder}"
                    if not os.path.exists(out_path):
                        os.makedirs(out_path, exist_ok=True)
                    out_file = out_path + f"/{fileName}.json"
                    read_file = f"{read_path}/{yearFolder}/{folder}/{fileName}.json"
                    dataset, examples, all_examples = buildBertDataset(opt, tokenizer, model_for, read_file, logger, 320)
                    predict(opt, model, dataset, examples, all_examples, out_file, logger)
                    os.remove(read_file)

    if model_type == 'Cnn':
        model = getCnnModel(opt)
        dataset = buildCnnDataset(opt)
        predict(opt, model, dataset, logger)

