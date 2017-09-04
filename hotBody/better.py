#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import time
import datetime


# 创建一个类
class Port:
    ' 类的帮助信息'

    # 类变量
    def __init__(self, traceId, duration):
        self.traceId = traceId
        self.duration = duration


class Text:
    '创建类'

    def __init__(self, id, duration, parentId):
        self.id = id
        if parentId != None:
            self.parentId = parentId
        if duration != None:
            self.duration = duration


def date_to_str(date):
    return str(date)[0:10]


def before_days(num):
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    li = []
    for i in range(0, num):
        # 今天减一天，一天一天减
        today = today - oneday
        # 把日期转换成字符串
        li.append(date_to_str(today))
    return today


def get_time(times):
    timearray = time.strptime(times, "%Y-%m-%d %H:%M:%S")
    timestamp = int(time.mktime(timearray))
    return int(round(timestamp * 1000))


def get_duration(inter):
    return inter.duration


def display_duration(duration):
    if len(duration) > 6:
        tail = duration[-6:-3]
        top = duration[:-6]
        if int(duration[-3:-2]) > 5:
            tail = int(tail)
            tail = tail + 1
        return top + '.' + str(tail) + ' s'

    elif len(duration) > 3:
        tail = duration[-3:]
        top = duration[:-3]
        return top + '.' + tail + ' ms'

    else:
        return duration + ' μs'


start = time.clock()

projectList = ['galaxy', 'yolar', 'evans', 'farmer', 'dna', 'sophon', 'careservice', 'civilization', 'cms',
               'curvaturedrive', 'dagon', 'difoil']

# 往前推一周，7天
startDate = date_to_str(before_days(7))
buildStartTime = startDate + ' 00:00:00'
startTime = get_time(buildStartTime)

# 当前时间
endTime = int(round(time.time()) * 1000)

# 最多显示条数
limit = 100000

# 最低运行时间（微秒单位）
# 科普:1秒=1000毫秒=1000000微秒
minDuration = 1000000

lockBack = endTime - startTime

# 循环
for project in projectList:

    values = {'serviceName': project, 'spanName': 'all', 'endTs': endTime,
              minDuration: minDuration, 'limit': limit, 'lookback': lockBack, 'annotationQuery': '',
              }

    r = requests.get("http://10.0.0.1:9411/api/v1/traces", params=values)

    if r.status_code == requests.codes.ok:
        text = r.content

        d_text = json.loads(text)
        dicts = {}
        if len(d_text) != 0:
            print project + '中'
            portList = []
            # 把每个id拿出来 ，组装成list
            for key in d_text:
                # 把每个接口组装成key_value形式 key:traceId ,value :key，key是个list
                dicts[key[0]["traceId"]] = key

        # 把list中的key=id value=object
        for i in dicts:
            traceDicts = {}
            # 将list打开获取object
            for t in dicts[i]:
                traceDicts[t['id']] = t

            for trace in dicts[i]:
                addDuration = 0;
                if not hasattr(trace, 'parentId') or traceDicts.get(trace['duraparentIdtion']) == None:
                    if hasattr(trace, 'duration'):
                        addDuration = addDuration + int(trace['duration'])

            if addDuration == 0:
                addDuration = dicts[i][0]['duration']

                port = Port(key[0]["traceId"], addDuration)
                portList.append(port)

        list = sorted(portList, key=get_duration, reverse=True)

        for re in list:
            strDuration = str(re.duration)
            minDuration = display_duration(strDuration)
            print 'traceId: ' + re.traceId + ' duration:' + str(minDuration)

end = time.clock()

consume = end - start

print '耗时' + str(consume) + 's'
