import os
import json
import time
from bs4 import BeautifulSoup
import sys
from datetime import date, datetime, timedelta
from utils.chrome.browser import *


def getUrls(opt, logger):
    # 启动Chrome浏览器
    browser = creat_browser()
    # 获取页面源代码
    url = 'https://mil.huanqiu.com/api/list?node=%22/e3pmh1dm8/e3pmt7hva%22,%22/e3pmh1dm8/e3pmtdr2r%22,%22/e3pmh1dm8/e3pn62l96%22,%22/e3pmh1dm8/e3pn6f3oh%22&offset=' + opt.offset + '&limit=' + opt.limit
    browser.get(url)
    page = browser.page_source
    # 关闭Chrome浏览器
    quit_browser(browser)
    page = BeautifulSoup(page, "html.parser")
    json_str = ""
    for body in page.find_all("body"):
        json_str += body.get_text()
    json_dict = json.loads(json_str)
    articles = []
    time_start = datetime.strptime(opt.year + "-01-01 00:00", '%Y-%m-%d  %H:%M')
    time_end = datetime.strptime(str(int(opt.year) + 1) + "-01-01 00:00", '%Y-%m-%d  %H:%M')
    time_article = datetime(2020, 1, 1)
    for json_inner_dict in json_dict["list"]:
        try:
            time_str = json_inner_dict["xtime"]
        except:
            continue
        time_int = int(time_str)
        if len(time_str) == 10:
            time_article = time_article.fromtimestamp(time_int)
        else:
            time_article = time_article.fromtimestamp(time_int / 1000)
        # time_article=datetime.strptime(json_inner_dict["xtime"], '%Y-%m-%d  %H:%M')
        if time_article < time_end and time_article >= time_start:
            print(json_inner_dict["title"])
            article = ["/article/" + json_inner_dict["aid"], json_inner_dict["title"],
                       json_inner_dict["source"]["name"], time_article.strftime('%Y-%m-%d  %H:%M')]
            articles.append(article)
        elif time_article < time_start:
            continue
    # 写入文件
    f = open(opt.RootPath + "/event/" + str(opt.year) + "/world.txt", 'a', encoding='utf-8')
    for article in articles:
        f.write(str(article) + "\n")
    f.close()
