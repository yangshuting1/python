#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# map：将传入的参数依次作用到函数中，作为函数的参数
def f(x):
    return x*x

r= map(f,[1,2,3,4,5])
print r

#把列表中的每个数改成string类型
strs=map(str,[1,2,3,4,5])

print strs

# reduce:把一个函数定义在一个序列上，这个函数必须接收两个参数，reduce把加过继续和序列的下一个参数做累加操作
def add(x, y):
    return x + y

a = reduce(add, [1, 3, 5, 7, 9])

print a


# filter:把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n % 2 == 1


b=list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7]))
print b


#返回函数
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum


#当调用sum()方法时，返回的不是求和结果，而是函数。


#我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
f = lazy_sum(1,3,5,7,9)
print f
print f()