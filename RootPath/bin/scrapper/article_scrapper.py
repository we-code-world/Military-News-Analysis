import urllib.request
import sys  # 引用sys模块进来，并不是进行sys的第一次加载
import os
import time
import gzip
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)     Chrome/67.0.3396.99 Safari/537.36'
headers = {
    'User-Agent': user_agent
}
g = sys.getdefaultencoding()  ##调用setdefaultencoding函数


def article_scraper(opt, url, name, logger):
    strl = 'https://mil.huanqiu.com' + url
    request = urllib.request.Request(strl)
    request.add_header('Accept-encoding', 'gzip')  # 添加头信息
    response = urllib.request.urlopen(request)
    if response.info().get('Content-Encoding') == 'gzip':
        data = gzip.decompress(response.read())
        html = data.decode('utf-8')
    bs = BeautifulSoup(html, "html.parser")
    text_f = open(opt.RootPath + "/event/" + opt.year + "/Articles/" + name + ".txt", 'a', encoding='utf-8')
    for item in bs.find_all("article"):
        for its in item.find_all("p"):
            t = text_f.write(its.get_text() + "\n")
    text_f.close()
    logger.info("写入第" + name + "篇文章内容完成！！")


def getArticles(opt, logger):
    article_f = open(opt.RootPath + "/event/" + opt.year + "/world.txt", 'r', encoding='utf-8')
    lines = article_f.readlines()
    article_id = 1
    for line in lines:
        article = eval(line.strip("\n"))
        url = article[0]
        name = str(article_id)
        article_f = open(opt.RootPath + "/" + opt.year + "/Articles/" + name + ".txt", 'a', encoding='utf-8')
        article_f.write('https://mil.huanqiu.com' + url + "\n")
        article_f.write(article[1] + "\n")
        article_f.write("来源：" + article[2] + "\n")
        article_f.write(article[3] + "\n")
        article_f.close()
        article_scraper(opt, logger, url, name)
        article_id += 1
