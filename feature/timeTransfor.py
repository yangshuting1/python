#!/usr/bin/env python
# -*- coding: utf-8 -*


aa = ['2428655',
      '233',
      '61234']


for a in aa:
    if len(a) > 6:
        tail = a[-6:]
        top = a[:-6]
        minDuration = top + ',' + tail
        print minDuration + 's'

    elif len(a) > 3:
        tail = a[-3:]
        top = a[:-3]
        minDuration = top + ',' + tail
        print minDuration + 'ms'

    else:
        print a+'μs'



