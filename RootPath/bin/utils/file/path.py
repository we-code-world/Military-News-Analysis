# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: read.py
@time: 2021/6/28 8:59
"""
import os

"""
:param path:uncertain path
:return:not exist path
"""


#  获取没有被使用的最低版本的路径
def getModelPath(basePath):
    for i in range(10):
        for j in range(10):
            for k in range(10):
                now_version_path = basePath + "_" + str(i) + "_" + str(j) + "_" + str(k)
                if not os.path.exists(now_version_path):
                    return now_version_path


# 获取最新一次训练结果的模型目录路径
def getRecentModelPath(basePath):
    last_path = basePath + "_0_0_0"
    for first in range(10):
        for second in range(10):
            for third in range(1, 10):
                current_path = basePath + "_" + str(first) + "_" + str(second) + "_" + str(third)
                if not os.path.exists(current_path):
                    return last_path
                last_path = current_path


def getPathListByName(basePath, fileName):
    """
    根据文件名获取对应路径下所有符合条件的绝对路径
    """
    file_lists = []

    for root, dirs, files in os.walk(basePath):
        for check_file in files:
            if fileName == check_file:
                file_lists.append(os.path.join(root, check_file).replace("\\", "/"))
    return file_lists


def getPathListBySuffix(basePath, suffix):
    """
    根据后缀获取所有对应文件的路径
    """
    file_lists = []

    for root, dirs, files in os.walk(basePath):
        for check_file in files:
            check_suffix = check_file.split(".")[-1]
            if suffix == check_suffix:
                file_lists.append(os.path.join(root, check_file).replace("\\", "/"))
    return file_lists


#  获取父路径
def getFatherPath(filePath):
    pathSliceList = filePath.replace("\\", "/").split("/")
    fatherPath = os.path.join(pathSliceList[0], "/")
    for pathSlice in pathSliceList[1:-1]:
        fatherPath = os.path.join(fatherPath, pathSlice)
    return fatherPath


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
    class_files = getPathListBySuffix("E:/Rootpath/resource" + "/format/trigger/classes", "txt")
    for class_file in class_files:
        print(class_file)
    # os.mkdir(path)
