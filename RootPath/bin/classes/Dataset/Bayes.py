# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: Bayes.py
@time: 2021/7/11 21:54
"""


class BayesClassifyDataset:
    def __init__(self, opt):
        pass

    def oneBatch(self):
        pass


class BayesDataset:
    def __init__(self, data):
        pass

    def oneBatch(self):
        dataset = []
        data_num = 1
        for data in getOneData():
            dataset.append(data)
            if data_num%15 == 0:
                yield dataset
                dataset = []
            i = i + 1
        if len(dataset) != 0:
            yield dataset

    def BMM(sentence: str,dict_file:str = "dict.txt") -> list:
        #将分词词典中的词以字典形式进行存储
        f1 = open(dict_file, 'r', encoding='utf8')
        dic = {}
        while 1:
            line = f1.readline() #将词典中的数据按行读取
            if len(line) == 0:
                break
            term = line.strip()  #由于本算法根据词典中词的最大长度确定最大分词长度，因此去除换行符以获得准确长度。
            dic[term] = 1        #对分词词典中的词进行遍历
        f1.close()

        f3 = open('stoplis.txt', 'r', encoding='utf8')
        stoplist = {}
        while 1:
            line = f3.readline()
            if len(line) == 0:
                break
            term = line.strip()
            stoplist[term] = 1
        f3.close()

        #遍历分词词典和停用词词典，通过比较获得最大分词长度
        max_Dchars = 0
        for Dkey in dic:
            if len(Dkey) > max_Dchars:
                max_Dchars = len(Dkey)
        max_Schars = 0
        for Skey in stoplist:
            if len(Skey) > max_Schars:
                max_Schars = len(Skey)
        max_chars = 0
        if max_Dchars<max_Schars:
            max_chars=max_Schars

        else:
            max_chars=max_Dchars
        s = len(sentence)  # 句子剩余长度
        Bwords = []  # 临时列表
        while s:
            # 取最大分词长度和句子剩余长度中小的值作为当前最大匹配词长
            max_cut_length = min(s, max_chars)
            # 逐步减少最大匹配词长
            for i in range(max_cut_length, 0, -1):
                new_word = sentence[s - i:s]  # 逆向分词
                if new_word in dic:
                    Bwords.append(new_word)  # 切的词在字典中，则添加到临时列表里
                    s -= i  # 更新句子剩余长度
                    break  # 跳出当前循环
                elif i == 1:  # 词长等于1，直接切词
                    Bwords.append(new_word)
                    s -= 1

        word_list = []
        for word in Bwords:  # 遍历临时列表
                if word == ' ':  # 去掉空白词
                    continue
                if word not in stoplist:  # 把不在停词表中的词选出来
                    word_list.append(word)
        return word_list  # 返还最终分词结果

    def save_json(self,path):
        json_file = open(path+"/test.json")
        json.dump(self.dataset,json_file)
        json_file.close()
    def save_txt(self,path):
        txt_file = open(path+"/test.txt")
        txt_file.close()

