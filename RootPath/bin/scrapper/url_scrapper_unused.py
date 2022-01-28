import os
import time
from bs4 import BeautifulSoup
desktop=os.path.join(os.path.expanduser("~"), 'Desktop/Rootpath')
#写入文件
Rootpath=input()
year = input()
import sys
from datetime import datetime, timedelta
sys.path.append(Rootpath+"/Tools")
import MyTools

#启动Chrome浏览器
browser = MyTools.creat_browser()
#获取页面源代码
url = 'https://mil.huanqiu.com/world'
browser.get(url)
time.sleep(1)
for R0 in range(1000):
  js = "window.scrollTo(0,document.body.scrollHeight);"
  browser.execute_script(js)
  print("下拉第"+str(R0)+"次")
  time.sleep(1)
page=browser.page_source
#关闭Chrome浏览器
MyTools.quit_browser(browser)

#list=[['m-recommend-con'],['recommend']]
#dict={['all-con']:"div",['container']:"div",['b-container']:"div",['m-container']:"div",['m-recommend']:"div",['m-recommend-con']:"div",['recommend']:"ul"}
#page=MyTools.getPage(page,"div",['m-recommend-con'])
page=BeautifulSoup(page,"html.parser")
for item in page.find_all("div"): 
  try:
    if(item['class']==['m-recommend-con']):
      page=item
      print(page)
  except:
    continue
articles=[]
time_str=""
time_start=datetime.strptime(""+str(year)+"-01-01 00:00", '%Y-%m-%d  %H:%M')
time_end=datetime.strptime(""+str(int(year)+1)+"-01-01 00:00", '%Y-%m-%d  %H:%M')
time_article=datetime.today
for item in page.find_all("li"): 
  article=[]
  article.append(item.a["href"])
  for it in item.find_all("h4"):
    article.append(it.get_text())
  for it in item.find_all("span"):
    try:
      if(it['class']==['con-txt']):
        article.append(it.get_text())
      if(it['class']==['original']):
        article.append(it.get_text())
      if(it['class']==['time']):
        article.append(it.get_text())
        time_str=it.get_text()
        print(time_str)
      time_article=datetime.strptime(time_str, '%Y-%m-%d  %H:%M')
      print(article)
    except:
      continue
  if(time_article<time_end and time_article>=time_start):
    articles.append(article)
  elif(time_article<time_start):
    break
  else:
    continue
f=open(Rootpath+"/"+str(year)+"/world.txt", 'a',encoding='utf-8')
for article in articles:
  f.write(str(article)+"\n")
f.close()