# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: read.py
@time: 2021/6/28 8:59
"""
import os
from xlrd import open_workbook
from xlutils.copy import copy
import xlwt
"""
:param path:uncertain path
:return:not exist path
"""
sheet_index = []


def createXls(path, sheetNames, sheetTittle=None):
    workbook = xlwt.Workbook(path)
    for sheet_name in sheetNames:
        workbook.add_sheet(sheet_name)
        sheet_index.append(0)
    if sheetTittle is not None:
        for index, tittle in enumerate(sheetTittle):
            write_sheet = workbook.get_sheet(index)
            sheet_index[index] = 1
            for num, text in enumerate(tittle):
                write_sheet.write(0, num, text)
    workbook.save(path)


#  获取没有被使用的最低版本的路径
def writeXls(path, event_data, sheet, sheet_start=False, NameList=None):
    global sheet_index
    if not os.path.exists(path):
        if NameList is None:
            NameList = ["sheet1"]
        createXls(path, NameList)
    if sheet_start:
        sheet_index[sheet] = 0
    read_file = open_workbook(path)
    write_file = copy(read_file)
    write_sheet = write_file.get_sheet(sheet)
    for num, text in enumerate(event_data):
        write_sheet.write(sheet_index[sheet], num, text)
    sheet_index[sheet] += 1
    write_file.save(path)


if __name__ == '__main__':
    '''
    path = getFatherPath("E:/Rootpath/model/Bert_SubObj/Model_0_0_1/checkpoint-100000/model.pt")
    print(path)
    path = os.path.join(path, "eval.txt")
    print(path)
    write_file = open(path, 'a+', encoding='utf-8')
    write_file.write("hhh")
    write_file.close()
    rec = getRecentModelPath("E:\\Rootpath\\model\\Bert_SubObj\\Model")
    print(rec)
    path = getPathListByName(rec, "model.pt")
    print(path)
    '''
    nameList = ["事件元素抽取结果", "事件元素标准化结果", "事件元素权重结果", "事件信息融合结果", "装备事件元素整合"]
    tittles = [
        ["新闻编号", "时间", "地点", "武器", "国家", "触发词", "主体", "客体"],
        ["新闻编号", "时间", "地点", "武器", "国家"],
        ["新闻编号", "时间", "地点", "武器", "国家"],
        ["新闻编号", "时间", "地点", "武器", "国家"],
        ["新闻编号", "事件类别", "开始时间", "结束时间", "事件地点", "事件触发词", "相关武器", "客体国家", "主体国家",
         "事件状态", "事件极性"]
    ]
    createXls("E:/Rootpath/events.xls", nameList, tittles)
    writeXls("E:/Rootpath/events.xls", tittles, 0)
    writeXls("E:/Rootpath/events.xls", tittles, 0)

