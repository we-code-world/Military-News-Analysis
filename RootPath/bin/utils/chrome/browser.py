import os
import time
import sys
try:
  from selenium import webdriver
  from selenium.webdriver.ie.options import Options as IEOp
  from selenium.webdriver.chrome.options import Options as ChromeOp
  from selenium.webdriver.firefox.options import Options as FirefoxOp
except:
  os.system(r"pip install -i https://pypi.tuna.tsinghua.edu.cn/simple selenium")
  from selenium import webdriver
  from selenium.webdriver.ie.options import Options as IEOp
  from selenium.webdriver.chrome.options import Options as ChromeOp
  from selenium.webdriver.firefox.options import Options as FirefoxOp
try:
  from bs4 import BeautifulSoup
except:
  os.system(r"pip install -i https://pypi.tuna.tsinghua.edu.cn/simple bs4")
  from bs4 import BeautifulSoup
#只有显式选择浏览器为'firefox'或'ie'
#才能打开对应的浏览器
#否则，打开的浏览器默认为'Chrome'
def creat_browser(chromePath=os.path.join(os.path.expanduser("~"), 'Desktop'),*args):
    sys.path.append(chromePath)
    os.system(r"set path=%path%;"+chromePath)
    if (len(args)==1) :
        if (args[0] == 'firefox') :
            # 创建一个Firefox无头浏览器对象
            firefox_options = FirefoxOp()
            # 设置它为无框模式
            firefox_options.add_argument('--headless')
            # 如果在windows上运行需要加代码
            firefox_options.add_argument('--disable-gpu')
            #启动火狐浏览器
            browser = webdriver.Firefox(options=firefox_options)
            # 设置一个10秒的隐式等待
            browser.implicitly_wait(10)
            #返回浏览器
            return browser
        elif (args[0] == 'ie') :
            # 创建一个IE无头浏览器对象
            ie_options = IEOp()
            # 设置它为无框模式
            ie_options.add_argument('--headless')
            # 如果在windows上运行需要加代码
            ie_options.add_argument('--disable-gpu')
            #启动IE浏览器
            browser = webdriver.Ie(options=ie_options)
            # 设置一个10秒的隐式等待
            #browser.implicitly_wait(10)
            #返回浏览器
            return browser
        else:
            # 创建一个Chrome无头浏览器对象
            chrome_options = ChromeOp()
            # 设置它为无框模式
            chrome_options.add_argument('--headless')
            # 如果在windows上运行需要加代码
            chrome_options.add_argument('--disable-gpu')
            #启动Chrome浏览器
            browser = webdriver.Chrome(options=chrome_options)
            # 设置一个10秒的隐式等待
            browser.implicitly_wait(10)
            #返回浏览器
            return browser
    else:
        # 创建一个Chrome无头浏览器对象
        chrome_options = ChromeOp()
        # 设置它为无框模式
        chrome_options.add_argument('--headless')
        # 如果在windows上运行需要加代码
        chrome_options.add_argument('--disable-gpu')
        #启动Chrome浏览器
        browser = webdriver.Chrome(options=chrome_options)
        # 设置一个10秒的隐式等待
        browser.implicitly_wait(10)
        #返回浏览器
        return browser

def quit_browser(browser):
    #关闭浏览器
    browser.quit()



if __name__ == '__main__':
    browser=creat_browser()
    browser.get('https://mil.huanqiu.com/article/40noKOLRHtB')
    print(browser.page_source)
    quit_browser(browser)