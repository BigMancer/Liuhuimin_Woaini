# 这个文件用来存一些常用的方法
import time

import random


def get_service_time():
    timedata = time.localtime()
    data = "{}年{}月{}日".format(timedata[0], timedata[1], timedata[2])
    return data


def get_one_ID(app_ID):
    # 以时间戳生成唯一性ID
    # ID格式:1640659283
    # 随机数(10)+应用编号(10)+时间戳+随机数(10)
    time_flag = str(time.time()).replace('.', '')
    random_text1 = ""
    random_text2 = ""
    for i in range(10):
        random_text1 = random_text1+str(random.randint(0, 9))
    for i in range(10):
        random_text2 = random_text2+str(random.randint(0, 9))
    ID = "{}{}{}{}".format(random_text2, app_ID, time_flag, random_text2)
    return ID
