# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: options.py
@time: 2021/6/28 8:59
"""
import argparse
from utils.file.read import readConfTXT


class GlobalArgs:
    def __init__(self):
        self.conf_path = ''

    def set_conf(self, conf_path):
        self.conf_path = conf_path

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser()
        return parser

    @staticmethod
    def initialize(parser: argparse.ArgumentParser):
        # args for path

        parser.add_argument('--ConfPath', default='', type=str,
                            help='the config file path of this project')

        parser.add_argument('--RootPath', default='', type=str,
                            help='the root path of this project')

        parser.add_argument('--DataPath', default='', type=str,
                            help='all the original event store path')

        parser.add_argument('--ExamplePath', default='', type=str,
                            help='all the train/test/predict event store path')

        parser.add_argument('--ArticleFolder', default='', type=str)

        parser.add_argument('--EventFolder', default='', type=str)

        parser.add_argument('--KeySentence', default='', type=str)

        parser.add_argument('--ScriptPath', default='', type=str,
                            help='the script path')

        parser.add_argument('--PyPath', default='', type=str,
                            help='the python program path')

        parser.add_argument('--ChromePath', default='', type=str,
                            help='the chrome program path')

        parser.add_argument('--ImgPath', default='', type=str,
                            help='the image path used and store')

        parser.add_argument('--TempPath', default='', type=str,
                            help='the path to create temp file')

        parser.add_argument('--ResPath', default='', type=str,
                            help='the resource file , such as contries\' and places\' messages')

        parser.add_argument('--BaiduAK', default='', type=str,
                            help='the baidu AK code')

        parser.add_argument('--GoogleAK', default='', type=str,
                            help='the google AK code')

        return parser

    @staticmethod
    def final_init(parser: argparse.ArgumentParser):
        # args for path
        args = parser.parse_args()

        if args.RootPath == '':
            parser.set_defaults(RootPath='E:/Rootpath')

        root_path_ = parser.parse_args().RootPath

        if args.DataPath == '':
            parser.set_defaults(DataPath=root_path_ + '/event')

        if args.ExamplePath == '':
            parser.set_defaults(ExamplePath=root_path_ + '/dataset')

        if args.ArticleFolder == '':
            parser.set_defaults(ArticleFolder='Article')

        if args.EventFolder == '':
            parser.set_defaults(EventFolder='Event')

        if args.KeySentence == '':
            parser.set_defaults(KeySentence='KeySentence')

        if args.PyPath == '':
            parser.set_defaults(PyPath=root_path_ + '/bin')

        if args.ScriptPath == '':
            parser.set_defaults(ScriptPath=root_path_ + '/bin/script')

        if args.ChromePath == '':
            parser.set_defaults(ChromePath=root_path_ + '/Tools/chrome')

        if args.ImgPath == '':
            parser.set_defaults(ImgPath='D:/intelliJ/SpatiotemporalEvolution/src/main/webapp/img')

        if args.TempPath == '':
            parser.set_defaults(TempPath=root_path_ + '/Temp')

        if args.ResPath == '':
            parser.set_defaults(ResPath=root_path_ + '/resource')

        if args.BaiduAK == '':
            parser.set_defaults(BaiduAK='wUixKXpRjjTuNebaEib9FfGxvjDuoPjG')

        if args.GoogleAK == '':
            parser.set_defaults(GoogleAK='AIzaSyAQ-LCGlyvahNSP6-VezsWyEsupKAMr-sc')

        return parser

    @staticmethod
    def conf_add_argument(parser: argparse.ArgumentParser, args):
        input_args = parser.parse_args()
        root_path = input_args.RootPath
        for argsName, argsValue, helps in args:
            argsValue = argsValue.replace("%RootPath%", root_path).strip()
            parser.add_argument('--' + argsName, default=argsValue, help=helps)
        return parser

    @staticmethod
    def conf_init(parser: argparse.ArgumentParser, args):
        less_args = []
        input_args = parser.parse_args()
        root_path = input_args.RootPath
        for argsName, argsValue, helps in args:
            if argsName == 'RootPath':
                if input_args.RootPath == '':
                    parser.set_defaults(RootPath=argsValue)
                    root_path = argsValue
                continue
            argsValue = argsValue.replace("%RootPath%", root_path).strip()
            if argsName == 'DataPath':
                if input_args.DataPath == '':
                    parser.set_defaults(DataPath=argsValue)
            elif argsName == 'ExamplePath':
                if input_args.ExamplePath == '':
                    parser.set_defaults(ExamplePath=argsValue)
            elif argsName == 'ArticleFolder':
                if input_args.ArticleFolder == '':
                    parser.set_defaults(ArticleFolder=argsValue)
            elif argsName == 'EventFolder':
                if input_args.EventFolder == '':
                    parser.set_defaults(EventFolder=argsValue)
            elif argsName == 'KeySentence':
                if input_args.KeySentence == '':
                    parser.set_defaults(KeySentence=argsValue)
            elif argsName == 'PyPath':
                if input_args.PyPath == '':
                    parser.set_defaults(PyPath=argsValue)
            elif argsName == 'ScriptPath':
                if input_args.ScriptPath == '':
                    parser.set_defaults(ScriptPath=argsValue)
            elif argsName == 'ChromePath':
                if input_args.ChromePath == '':
                    parser.set_defaults(ChromePath=argsValue)
            elif argsName == 'ImgPath':
                if input_args.ImgPath == '':
                    parser.set_defaults(ImgPath=argsValue)
            elif argsName == 'TempPath':
                if input_args.TempPath == '':
                    parser.set_defaults(TempPath=argsValue)
            elif argsName == 'ResPath':
                if input_args.ResPath == '':
                    parser.set_defaults(ResPath=argsValue)
            elif argsName == 'BaiduAK':
                if input_args.BaiduAK == '':
                    parser.set_defaults(BaiduAK=argsValue)
            elif argsName == 'GoogleAK':
                if input_args.GoogleAK == '':
                    parser.set_defaults(GoogleAK=argsValue)
            else:
                less_args.append((argsName, argsValue, helps))
        return parser, less_args

    def get_parser(self):

        parser = self.parse()
        parser = self.initialize(parser)

        input_args = parser.parse_args()

        if input_args.ConfPath == '':
            parser.set_defaults(ConfPath=self.conf_path)

        input_args = parser.parse_args()
        if input_args.ConfPath != '':
            parser, args = self.conf_init(parser, readConfTXT(input_args.ConfPath))
            parser = self.conf_add_argument(parser, args)

        parser = self.final_init(parser)
        return parser.parse_args()


class ModelArgs(GlobalArgs):
    @staticmethod
    def initialize(parser: argparse.ArgumentParser):
        parser = GlobalArgs.initialize(parser)

        parser.add_argument('--version', default='', type=str,
                            help='submit version')

        parser.add_argument('--operation', required=True, type=str)

        parser.add_argument('--GPU', default='', type=str)

        parser.add_argument('--learnRate', default=0.0, type=float)

        parser.add_argument('--otherLearnRate', default=0.0, type=float)

        parser.add_argument('--newModel', default='', type=str)

        parser.add_argument('--BaseModel', default='', type=str)

        parser.add_argument('--BaseModelPath', default='', type=str)

        parser.add_argument('--ModelType', default='', type=str)

        parser.add_argument('--ModelPath', default='', type=str)

        parser.add_argument('--dependWeapons', default=True, action='store_true')

        # 添加原始参数
        parser.add_argument('--max_seq_len', default=256, type=int)

        parser.add_argument('--start_threshold', default=0.5, type=float)

        parser.add_argument('--end_threshold', default=0.5, type=float)

        parser.add_argument('--swa_start', default=1, type=int,
                            help='the epoch when swa start')

        parser.add_argument('--train_epochs', default=6, type=int,
                            help='Max training epoch')

        parser.add_argument('--dropout_prob', default=0.1, type=float,
                            help='drop out probability')

        parser.add_argument('--max_grad_norm', default=1.0, type=float,
                            help='max grad clip')

        parser.add_argument('--warmup_proportion', default=0.1, type=float)

        parser.add_argument('--weight_decay', default=0., type=float)

        parser.add_argument('--adam_epsilon', default=1e-8, type=float)

        parser.add_argument('--train_batch_size', default=32, type=int)

        parser.add_argument('--batch_size', default=16, type=int)

        parser.add_argument('--eval_model', default=False, action='store_true',
                            help='whether to eval model after training')

        parser.add_argument('--attack_train', default='fgm', type=str,
                            help='fgm / pgd attack train when training')

        return parser

    @staticmethod
    def conf_init(parser: argparse.ArgumentParser, args):
        parser, args = GlobalArgs.conf_init(parser, args)
        less_args = []
        input_args = parser.parse_args()
        root_path = input_args.RootPath
        for argsName, argsValue, helps in args:
            argsValue = argsValue.replace("%RootPath%", root_path).strip()
            if argsName == 'version':
                if input_args.version == '':
                    parser.set_defaults(version=argsValue)
            elif argsName == 'learnRate':
                if input_args.learnRate == 0.0:
                    parser.set_defaults(learnRate=float(argsValue))
            elif argsName == 'GPU':
                if input_args.GPU == '':
                    parser.set_defaults(GPU=argsValue)
            elif argsName == 'otherLearnRate':
                if input_args.otherLearnRate == 0.0:
                    parser.set_defaults(otherLearnRate=float(argsValue))
            elif argsName == 'newModel':
                if input_args.newModel == '':
                    parser.set_defaults(newModel=argsValue)
            elif argsName == 'BaseModel':
                if input_args.BaseModel == '':
                    parser.set_defaults(BaseModel=argsValue)
            elif argsName == 'BaseModelPath':
                if input_args.BaseModelPath == '':
                    parser.set_defaults(BaseModelPath=argsValue)
            elif argsName == 'ModelType':
                if input_args.ModelType == '':
                    parser.set_defaults(ModelType=argsValue)
            elif argsName == 'ModelPath':
                if input_args.ModelPath == '':
                    parser.set_defaults(ModelPath=argsValue)
            else:
                less_args.append((argsName, argsValue, helps))
        return parser, less_args

    @staticmethod
    def final_init(parser: argparse.ArgumentParser):

        parser = GlobalArgs.final_init(parser)

        # args for path
        args = parser.parse_args()

        root_path_ = args.RootPath

        if args.version == '':
            parser.set_defaults(version='v0')

        if args.GPU == '':
            parser.set_defaults(GPU='0')

        if args.learnRate == 0.0:
            parser.set_defaults(learnRate=2e-5)

        if args.otherLearnRate == 0.0:
            parser.set_defaults(otherLearnRate=2e-5)

        if args.newModel == '':
            parser.set_defaults(newModel='True')

        if args.BaseModel == '':
            parser.set_defaults(BaseModel='Bert')

        if args.BaseModelPath == '':
            parser.set_defaults(BaseModelPath=root_path_ + '/model/Bert')

        if args.ModelType == '':
            parser.set_defaults(ModelType='Trigger')

        if args.ModelPath == '':
            parser.set_defaults(ModelPath=root_path_ + '/model/Bert_' + parser.parse_args().ModelType)

        return parser


class ScrapperArgs(GlobalArgs):
    @staticmethod
    def initialize(parser: argparse.ArgumentParser):
        parser = GlobalArgs.initialize(parser)

        parser.add_argument('--version', default='', type=str,
                            help='submit version')

        parser.add_argument('--operation', required=True, type=str)

        parser.add_argument('--startTime', default='', type=str)

        parser.add_argument('--endTime', default='', type=str)

        parser.add_argument('--year', default='', type=str)

        return parser

    @staticmethod
    def conf_init(parser: argparse.ArgumentParser, args):
        parser, args = GlobalArgs.conf_init(parser, args)
        less_args = []
        input_args = parser.parse_args()
        root_path = input_args.rootPath
        for argsName, argsValue, helps in args:
            argsValue = argsValue.replace("%rootPath%", root_path).strip()
            if argsName == 'version':
                if input_args.version == '':
                    parser.set_defaults(version=argsValue)
            elif argsName == 'startTime':
                if input_args.startTime == '':
                    parser.set_defaults(startTime=argsValue)
            elif argsName == 'endTime':
                if input_args.endTime == '':
                    parser.set_defaults(endTime=argsValue)
            elif argsName == 'year':
                if input_args.year == '':
                    parser.set_defaults(year=argsValue)
            else:
                less_args.append((argsName, argsValue, helps))
        return parser, less_args

    @staticmethod
    def final_init(parser: argparse.ArgumentParser):

        parser = GlobalArgs.final_init(parser)

        # args for path
        args = parser.parse_args()

        root_path_ = args.rootPath

        if args.version == '':
            parser.set_defaults(version='v0')

        if args.startTime == '':
            parser.set_defaults(startTime='2020-01-01')

        if args.endTime == '':
            parser.set_defaults(endTime='2021-01-01')

        if args.year == '':
            parser.set_defaults(year='2020')

        return parser


class EventArgs(GlobalArgs):
    @staticmethod
    def initialize(parser: argparse.ArgumentParser):
        parser = GlobalArgs.initialize(parser)

        parser.add_argument('--version', default='', type=str,
                            help='submit version')

        parser.add_argument('--operation', required=True, type=str)

        parser.add_argument('--sourcePath', default='', type=str)

        return parser

    @staticmethod
    def conf_init(parser: argparse.ArgumentParser, args):
        parser, args = GlobalArgs.conf_init(parser, args)
        less_args = []
        input_args = parser.parse_args()
        root_path = input_args.rootPath
        for argsName, argsValue, helps in args:
            argsValue = argsValue.replace("%rootPath%", root_path).strip()
            if argsName == 'version':
                if input_args.version == '':
                    parser.set_defaults(version=argsValue)
            elif argsName == 'sourcePath':
                if input_args.sourcePath == '':
                    parser.set_defaults(sourcePath=argsValue)
            else:
                less_args.append((argsName, argsValue, helps))
        return parser, less_args

    @staticmethod
    def final_init(parser: argparse.ArgumentParser):

        parser = GlobalArgs.final_init(parser)

        # args for path
        args = parser.parse_args()

        example_path = args.ExamplePath

        if args.version == '':
            parser.set_defaults(version='v0')

        if args.sourcePath == '':
            parser.set_defaults(sourcePath=example_path + '/predict/Attribution')

        return parser
