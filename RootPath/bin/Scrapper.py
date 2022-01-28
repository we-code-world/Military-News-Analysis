import os
import time
import sys
from utils.logger import *
from utils.lock import *
from utils.options import ScrapperArgs
from scrapper.url_scrapper import getUrls
from scrapper.article_scrapper import getArticles


def mainFunction():
    set_scrapper_logConfig()
    if process_lock("scrapper"):
        return 0

    args = ScrapperArgs().get_parser()

    assert args.operation in ['url', 'article'], 'Undefined operation in Scrapper'

    operation_func = args.operation  # 根据输入参数决定执行的操作

    if operation_func == 'url':
        getUrls(args, get_logger("url"))
    if operation_func == 'article':
        getArticles(args, get_logger("article"))

    return unlock("scrapper")


if __name__ == '__main__':
    mainFunction()
