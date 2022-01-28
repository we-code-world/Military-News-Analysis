# coding=utf-8
"""
@author: Michael
@license: (C) Copyright 2021-2022, NJUST.
@contact: 1289580847@qq.com
@file: TimeFormat.py
@time: 2021/7/6 21:18
"""

import lancher
from datetime import datetime, timedelta

quantum = {"至", "到", "、", "-", "期间", "前后"}

start = {"自", "从", "开始"}

festival = {"春节", "元宵", "清明", "端午", "中秋", "重阳", "腊八", "除夕", "大年三十",
            "元旦", "妇女", "劳动", "青年", "国庆"
            }
week = {"周一", "周二", "周三", "周四", "周五", "周六", "周末", "周日",
        "本周一", "本周二", "本周三", "本周四", "本周五", "本周六", "本周末", "本周日",
        "上周一", "上周二", "上周三", "上周四", "上周五", "上周六""上周末", "上周日"
        }
special = {"今年", "去年", "明年", "本月", "上月", "下月", "近日", "今天", "昨日", "昨天", "日前", "上旬", "中旬", "下旬"}

specialYear = {"年底", "年初", "年末"}

specialMonth = {"月底", "月初", "月末"}

specialWords = {"底", "初", "末"}

morning = {"上午", "早上", "凌晨"}

afternoon = {"下午", "傍晚", "晚上"}


def cut_off(timeStr, label):
    timeStr.replace("期间", "")
    timeStr.replace("持续", "")
    if label in ["至", "到", "、", "-"]:
        time_list = timeStr.split(label)
        return time_list[0], time_list[1]
    else:
        return timeStr, ""


def remove_unused(timeStr):
    timeStr.replace("自", "")
    timeStr.replace("从", "")
    timeStr.replace("开始", "")
    return timeStr, ""


def lunar2format(date, newsTime):
    dates = lancher.get_solar_date(date[0], date[1], date[2])
    formatTime = dates[0]
    for dt in dates:
        if dt < newsTime:
            formatTime = dt
    return formatTime


def solar2format(date):
    return datetime(date[0], date[1], date[2])


def special2format(newsTime):
    txt_dict = {}
    yearStr = newsTime.strftime('%Y')
    lastYearStr = str(int(yearStr) - 1) + "年"
    nextYearStr = str(int(yearStr) + 1) + "年"
    txt_dict["今年"] = yearStr + "年"
    txt_dict["去年"] = lastYearStr
    txt_dict["明年"] = nextYearStr
    monthStr = newsTime.strftime('%m')
    for_lastMonth = datetime(int(yearStr), int(monthStr), 1)
    for_nextMonth = datetime(int(yearStr), int(monthStr), 28)
    lastMonth = for_lastMonth - timedelta(days=1)
    nextMonth = for_nextMonth + timedelta(days=5)
    lastMonthStr = lastMonth.strftime("%m") + "月"
    nextMonthStr = nextMonth.strftime("%m") + "月"
    txt_dict["本月"] = monthStr + "月"
    txt_dict["上月"] = lastMonthStr
    txt_dict["下月"] = nextMonthStr
    dayStr = newsTime.strftime('%d') + "日"
    txt_dict["今天"] = dayStr
    yesterdayStr = (newsTime - timedelta(days=1)).strftime('%d') + "日"
    txt_dict["近日"] = (newsTime - timedelta(days=3)).strftime('%d') + "日"
    txt_dict["昨日"] = yesterdayStr
    txt_dict["昨天"] = yesterdayStr
    txt_dict["日前"] = yesterdayStr
    txt_dict["上旬"] = "01日"
    txt_dict["中旬"] = "10日"
    txt_dict["下旬"] = "20日"
    return txt_dict


def specialYear2format(yearStr):
    nextYear = datetime(int(yearStr), 1, 1)
    yearStr = nextYear - timedelta(days=1)
    return yearStr.strftime('%m'), yearStr.strftime('%d')


def specialMonth2format(yearStr, monthStr):
    nextMonth = datetime(int(yearStr),
                         int(monthStr) + 1, 1
                         )
    return (nextMonth - timedelta(days=1)).strftime('%d')


def week2format(timeStr, newsTime):  # 本周六 周六 上周六
    week_dict = {
        "周一": "+0", "周二": "+1", "周三": "+2", "周四": "+3",
        "周五": "+4", "周六": "+5", "周末": "+6", "周日": "+6",
        "本周一": "+0", "本周二": "+1", "本周三": "+2", "本周四": "+3",
        "本周五": "+4", "本周六": "+5", "本周末": "+6", "本周日": "+7",
        "上周一": "-7", "上周二": "-6", "上周三": "-5", "上周四": "-4",
        "上周五": "-3", "上周六": "-2", "上周末": "-1", "上周日": "-1"
    }
    newsTimeStr = newsTime.strftime('%Y-%m-%d')
    time = datetime.strptime(newsTimeStr, '%Y-%m-%d')
    if int(newsTime.strftime('%w')) == 0:
        time = time - timedelta(days=6)
    else:
        time = time - timedelta(days=int(newsTime.strftime('%w')) - 1)
    times = week_dict[timeStr]
    d = int(times[1])
    if times[0] == '+':
        time = time + timedelta(days=d)
    else:
        time = time - timedelta(days=d)
    rtnStr = time.strftime('%Y') + "年"
    rtnStr = rtnStr + time.strftime('%m') + "月"
    rtnStr = rtnStr + time.strftime('%d') + "日"
    return rtnStr


def festival2format(timeStr, year, newsTime):
    dict1 = {
        "春节": [2020, 1, 1], "元宵": [2020, 1, 1], "清明": [2020, 1, 1],
        "端午": [2020, 9, 9], "中秋": [2020, 9, 9], "重阳": [2020, 9, 9],
        "腊八": [2020, 12, 8]
    }
    dict2 = {
        "元旦": [2020, 1, 1], "妇女": [2020, 3, 8], "劳动": [2020, 5, 1],
        "青年": [2020, 5, 4], "国庆": [2020, 10, 1]
    }
    solar = 1
    if timeStr == "除夕" or timeStr == "大年三十":
        date = [2020, 1, 1]
        date[0] = year + 1
        time = lunar2format(date, newsTime) - timedelta(days=1)
        return solar, time.strftime('%m'), time.strftime('%d')
    try:
        timeStr = timeStr.replace("期间", "")
        timeStr = timeStr.replace("节", "")
        timeStr = timeStr.replace("春", "春节")
        date = dict1[timeStr]
        date[0] = year
        time = lunar2format(date, newsTime)
    except:
        timeStr = timeStr.replace("五四青年", "青年")
        timeStr = timeStr.replace("五四", "青年")
        timeStr = timeStr.replace("三八妇女", "妇女")
        timeStr = timeStr.replace("五一", "劳动")
        timeStr = timeStr.replace("五一劳动", "劳动")
        date = dict2[timeStr]
        date[0] = year
        time = solar2format(date)
        solar = 0
    return solar, time.strftime('%m'), time.strftime('%d')


def txt2num(timeStr):  # 二零一二
    number_dict = {
        "零": '0', "一": '1', "二": '2', "三": '3', "四": '4',
        "五": '5', "六": '6', "七": '7', "八": '8', "九": '9',
        "十": '10', "十一": '11', "十二": '12', "十三": '13', "十四": '14',
        "十五": '15', "十六": '16', "十七": '17', "十八": '18', "十九": '19',
        "二十": '20', "二十一": '21', "二十二": '22', "二十三": '23', "二十四": '24',
        "二十五": '25', "二十六": '26', "二十七": '27', "二十八": '28', "二十九": '29',
        "三十": '30', "三十一": '31',

        "正": "1", "腊": "12",
        "初一": "1", "初二": "2", "初三": "3", "初四": "4", "初五": "5",
        "初六": "6", "初七": "7", "初八": "8", "初九": "9", "初十": "10"
    }
    try:
        numstr = number_dict[timeStr]
        return numstr
    except:
        numstr = ""
    i = 1
    while i <= len(timeStr):
        try:
            numstr = numstr + number_dict[timeStr[0:-i]]
            timeStr = timeStr[-i:]
            i = 1
        except:
            i = i + 1
            continue
    try:
        numstr = numstr + number_dict[str]
    except:
        print("无法将" + timeStr + "转化为阿拉伯数字")
    return numstr


def time_format(timeStr, newsTimeStr):  # 2020-11-08 18:51
    newsTime = datetime.strptime(newsTimeStr, '%Y-%m-%d  %H:%M')
    sorl, i, j, k, l, sign, dsign, halfday = 0, 0, 0, 0, 0, 0, 1, 0
    if timeStr[:2] == "农历":
        sorl = 1
    timeStr = timeStr.replace("星期", "周")
    timeStr = timeStr.replace("礼拜", "周")
    timeStr = timeStr.replace("周天", "周日")
    timeStr = timeStr.replace("年年", "年")
    timeStr = timeStr.replace("财年", "年")
    timeStr = timeStr.replace("月月", "月")
    timeStr = timeStr.replace("上个月", "上月")
    timeStr = timeStr.replace("下个月", "下月")
    timeStr = timeStr.replace("约", "")
    specialDict = special2format(newsTime)
    strlen = len(timeStr)
    realTimeStr = timeStr
    for stri in range(strlen - 1):
        str2 = realTimeStr[stri:stri + 2]
        str3 = realTimeStr[stri:stri + 3]
        if str2 in special:
            realTimeStr = realTimeStr[:stri] + specialDict[str2] + realTimeStr[stri + 2:]
        elif str2 in week:
            realTimeStr = realTimeStr[:stri] + week2format(str2, newsTime) + realTimeStr[stri + 2:]
        elif stri < strlen - 2 and str3 in week:
            realTimeStr = realTimeStr[:stri] + week2format(str3, newsTime) + realTimeStr[stri + 3:]
        if str2 == "时间":
            realTimeStr = timeStr[stri + 2:]
    yearStr = newsTime.strftime('%Y')
    monthStr = newsTime.strftime('%m')
    dayStr = newsTime.strftime('%d')
    hourStr = "0"
    year, month, day, hour = int(yearStr), int(monthStr), int(dayStr), 0
    realTimeStrLen = len(realTimeStr)
    for i in range(realTimeStrLen):
        if realTimeStr[i] == '年' and realTimeStr[i - 1] != '青':
            yearStr = realTimeStr[:i]
            monthStr = "01"
            dayStr = "01"
            j = i + 1
            sign = 1
        elif realTimeStr[i] == '月' or realTimeStr[i] == '·':
            monthStr = realTimeStr[j:i]
            dayStr = "01"
            k = i + 1
            sign = 1
        elif realTimeStr[i] == '日' or realTimeStr[i] == '号':
            dayStr = realTimeStr[k:i]
            l = i + 1
            sign, dsign = 1, 0
        elif realTimeStr[i] == '时' or realTimeStr[i] == '点':
            if realTimeStr[l:l + 2] in morning:
                halfday = 0
                l = l + 2
            elif realTimeStr[l:l + 2] in afternoon:
                halfday = 12
                l = l + 2
            hourStr = realTimeStr[l:i]
            sign, dsign = 1, 0
    try:
        year = int(yearStr)
    except:
        year = int(txt2num(yearStr))
    for stri in range(realTimeStrLen - 1):
        str2 = realTimeStr[stri:stri + 2]
        if str2 in festival:
            sorl, monthStr, dayStr = festival2format(str2, year, newsTime)
        elif (stri < realTimeStrLen - 3) and realTimeStr[stri:stri + 4] == "大年三十":
            sorl, monthStr, dayStr = festival2format("大年三十", year, newsTime)
    if (timeStr[-1] in specialWords) and j != 0 and k == 0:
        if timeStr[-1] == "初":
            monthStr, dayStr = "1", "1"
        else:
            monthStr, dayStr = specialYear2format(year)
    try:
        month = int(monthStr)
    except:
        month = int(txt2num(monthStr))
    if (timeStr[-1] in specialWords) and k != 0:
        if timeStr[-1] == "初":
            dayStr = "1"
        else:
            dayStr = specialMonth2format(year, month)
    try:
        day = int(dayStr)
    except:
        day = int(txt2num(dayStr))
        if day > 31:
            month = day / 10
            day = day % 10
    try:
        hour = int(hourStr) % 12 + halfday
    except:
        hour = int(txt2num(hourStr)) % 12 + halfday
    time = newsTime
    date = [year, month, day]
    for si in range(len(timeStr) - 1):
        if timeStr[si] == '初' or timeStr[si] == '腊' or timeStr[si] == '正':
            sorl = 1
    if sorl == 1:
        time = lunar2format(date, newsTime)
    elif sorl == 0:
        time = solar2format(date)
    time = time + timedelta(hours=hour)
    return time.strftime("%Y-%m-%d  %H:%M")


def doTimeFormat(timeStr, newsTimeStr):
    startTime, endTime = "", ""
    startTimeStr, endTimeStr = timeStr, ""
    for label in quantum:
        if label in timeStr:
            startTimeStr, endTimeStr = cut_off(timeStr, label)
            break
    for label in start:
        if label in timeStr:
            startTimeStr, endTimeStr = remove_unused(timeStr)
            break
    try:
        if startTimeStr != "":
            startTime = time_format(startTimeStr, newsTimeStr)
    except:
        print("无法识别的格式：" + timeStr)
        print("可以转换的格式：")
        print("    [当地时间/本地时间/北京时间/xx时间...][年][月][日][时][分]")
        print("    [当地时间/本地时间/北京时间/xx时间.../本/上]周/星期/礼拜x")
        print("    [今年/去年/xx年]春节/国庆[节]")
        print("    昨天/昨日/日前/近日/近几天/本月初/本月末/本月底/今年年初/今年年末/今年初/今年末/今年底")
        print("    [农历[时间]]正月/腊月初x")
    try:
        if endTimeStr != "":
            if startTime != "":
                endTime = time_format(endTimeStr, startTime)
            else:
                endTime = time_format(endTimeStr, newsTimeStr)
    except:
        print("无法识别的格式：" + timeStr)
        print("可以转换的格式：")
        print("    [当地时间/本地时间/北京时间/xx时间...][年][月][日][时][分]")
        print("    [当地时间/本地时间/北京时间/xx时间.../本/上]周/星期/礼拜x")
        print("    [今年/去年/xx年]春节/国庆[节]")
        print("    昨天/昨日/日前/近日/近几天/本月初/本月末/本月底/今年年初/今年年末/今年初/今年末/今年底")
        print("    [农历[时间]]正月/腊月初x")
    return startTime.split(" ")[0], endTime.split(" ")[0]


if __name__ == '__main__':
    timeStr = input("请输入需要规格化的时间：")
    newsTimeStr = input("请输入新闻时间：")
    time = time_format(timeStr, newsTimeStr)
    print(doTimeFormat(timeStr, newsTimeStr))
