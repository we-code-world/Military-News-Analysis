# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: read.py
@time: 2021/6/28 8:59
"""


#  读取对应文件内所有词语，返回词语列表
def getWordList(path):
    word_list = []
    with open(path, "r", encoding="utf-8") as read_file:
        words = read_file.readlines()
        for word in words:
            if word not in word_list:
                real_word = word.strip()
                word_list.append(real_word)
    return word_list


#  读取配置文件
def readConfTXT(path):
    """
    :param path:the path of config file
    :return:list of (argsName,argsValue,helps)
    """
    with open(path + "/context.txt", "r", encoding="utf-8") as confTXT:
        rtn_args = []
        helps = ''
        lines = confTXT.readlines()
        for line in lines:
            args_help = line.split('#')
            args = args_help[0]
            if len(args_help) > 1:
                helps = args_help[-1].strip()
            args = args.strip()
            if args == '':
                continue
            else:
                argsName, argsValue = args.split('=')
                argsName = argsName.strip()
                rtn_args.append((argsName, argsValue, helps))
                helps = ''
    return rtn_args


#  将新闻文本分割为句子
def readNews2Seq(file):
    def getTexts(text):
        mark_point = 0
        cut_point = 0
        mark_char = ["【", "】", "（", "）"]
        inner_char = ["？", "！", "。", "······", "#"]
        mark_list = []
        rtn_texts = []
        rtn_row_text = []
        for idx, char in enumerate(text):
            if char in mark_char:
                mark_list.append((char, idx))
        if len(mark_list) == 0:
            return [(0, text)]
        sum = 0
        for char, idx in mark_list:
            if char in ["【", "（"]:
                if sum == 0:
                    if text[cut_point:idx] != "":
                        rtn_texts.append((0, text[cut_point:idx]))
                        mark_point = idx
                sum += 1
            else:
                if sum == 1:
                    rtn_texts.append((1, text[mark_point:idx + 1]))
                    cut_point = idx + 1
                sum -= 1
        if text[cut_point:] != "":
            rtn_texts.append((0, text[cut_point:]))
        reverse_texts = rtn_texts[::-1]
        last_seq = ""
        end_id = 0
        take_texts = []
        for reverse_id, reverse_seq in enumerate(reverse_texts):
            if last_seq == "":
                sign = reverse_seq[0]
                if sign == 1:
                    take_texts.append((1, reverse_seq[1]))
                    last_seq = ""
                else:
                    end_id = len(rtn_texts) - reverse_id + 1
                    break
        rtn_texts = rtn_texts[:end_id]
        rtn_texts.append((0, "end"))
        last_seq = ""
        addNum = 0
        sign = 0
        for seq_id, take_text in enumerate(rtn_texts):
            # print(seq)
            if last_seq == "":
                sign = take_text[0]
                if sign == 1:
                    rtn_row_text.append((1, take_text[1]))
                    last_seq = ""
                else:
                    last_seq = take_text[1]
                continue
            if take_text[1] == "end":
                rtn_row_text.append((sign, last_seq))
                break
            if take_text[0] == 1:
                div_sign = False
                for char in inner_char:
                    if char in take_text[1]:
                        div_sign = True
                        break
                if div_sign:
                    rtn_row_text.append((sign, last_seq))
                    last_seq = ""
                else:
                    last_seq = last_seq + take_text[1]
                    addNum = 1
            else:
                if addNum > 0:
                    last_seq = last_seq + take_text[1]
                    addNum -= 1
                else:
                    last_seq = take_text
                sign = 0
        for _take_text_ in take_texts:
            rtn_row_text.append(_take_text_)
        return rtn_row_text

    def getSeqs(article):
        seqs = []
        cut_char = ["？", "！", "。", "······"]
        mark_cut_char = ["，"]
        for sign, text in getTexts(article):
            if sign == 1:
                seqs.append(text)
                continue
            last_cut_point = 0
            last_mark_point = 0
            for idx, char in enumerate(text):
                if idx - last_cut_point > 512:
                    if last_cut_point != last_mark_point:
                        seq = text[last_cut_point:last_mark_point + 1]
                        last_cut_point = last_mark_point + 1
                        seqs.append(seq)
                    else:
                        raise ValueError(
                            'can not divide this article, because %s too long' % text[last_cut_point:idx + 1])
                elif char in cut_char:
                    seq = text[last_cut_point:idx + 1]
                    last_cut_point = idx + 1
                    last_mark_point = idx
                    seqs.append(seq)
                elif char in mark_cut_char:
                    last_mark_point = idx
            if last_cut_point < len(text):
                seqs.append(text[last_cut_point:])
        return seqs

    with open(file, "r", encoding="utf-8") as news:
        rtn_seqs = []
        tittle = []
        lines = news.readlines()
        for idx, line in enumerate(lines):
            line = line.strip()
            if idx < 4:
                if idx == 1:
                    tittle = getSeqs(line)
                continue
            div_seqs = getSeqs(line)
            for div_seq in div_seqs:
                rtn_seqs.append(div_seq)
    return tittle, rtn_seqs


#  从新闻文本构建分句文件
def createNews2Seq(read_file, out_file):
    art_list, seq_list = readNews2Seq(read_file)
    write_line = [str(len(art_list))]
    for article in art_list:
        write_line.append(article)
    for sentence in seq_list:
        write_line.append(sentence)
    with open(out_file, "w+", encoding="utf-8") as write_file:
        for each in write_line:
            write_file.write(each + "\n")
    write_file.close()


if __name__ == '__main__':
    func = input()
    if func == "readNews2Seq":
        file = input()
        arts, seqs = readNews2Seq(file)
        print(len(arts))
        for art in arts:
            print(art)
        for seq in seqs:
            print(seq)
    elif func == "createNews2Seq":
        readfile = input()
        outfile = input()
        createNews2Seq(readfile, outfile)
