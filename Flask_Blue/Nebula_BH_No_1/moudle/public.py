# 这个文件用来存一些常用的方法
import time
def get_service_time():
    timedata = time.localtime()
    data = "{}年{}月{}日".format(timedata[0], timedata[1], timedata[2])
    return data


