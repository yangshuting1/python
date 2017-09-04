#!/usr/bin/env python
# -*- coding: utf-8 -*

# 迭代:给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# python 中含有六种内建序列类：list, tuple, string, unicode, buffer, xrange

# exp1:遍历list
students = ['Amy', 'Candy', 'Shary']

for student in students:
    print student

# exp2:遍历dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key

# 默认的遍历出来的是dict的key,要遍历value：
for value in d.values():
    print value

# 字符串迭代
for ch in 'ABC':
    print ch

#Que1:如何判别一个对象是不是可迭代对象？

from collections import Iterable
isinstance('abc',Iterable) # str是否是可以迭代的 True

#Que2:如何对list实现类似java的下标循环？
for i, value in enumerate(['A', 'B', 'C']):
    print (i, value)
