#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# filter()用于过滤序列
# filter()接受一个函数一个参数。

# exp1:删除偶数，保留奇数
def is_odd(n):
    return n % 2 == 1


list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# [1,3,5,7,9]

# exp2:把序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


list(filter(not_empty, ['A', 'B', None, '', 'C']))


# ['A','B','C']


# exp3:求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 这是一个生成器，并且是一个无限序列


# 定义一个奇数序列,这是一个生成器，并且是一个无限循环序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


# 定义一个筛选函数:
def _not_divisible(n):
    return lambda x: x % n > 0


# 最后定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():
    if n < 1000:
        print(n)
    else:
        break
