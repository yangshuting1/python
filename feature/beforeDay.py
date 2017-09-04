#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime



def datetostr(date):
    return str(date)[0:10]

def getDaysByNum(num):
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    li=[]
    for i in range(0,num):
        #今天减一天，一天一天减
        today=today-oneday
        #把日期转换成字符串
        #result=datetostr(today)
        li.append(datetostr(today))
    return today


a = datetostr(getDaysByNum(18))+' 00:00:00'


