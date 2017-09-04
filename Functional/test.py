#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# yield关键字：一次迭代中你的函数会执行，从开始到达 yield 关键字，
# 返回 yield 后的值作为第一次迭代的返回值. 然后，每次执行这个函数都会继续执行你在函数内部定义的那个循环的下一次，再返回那个值，直到没有可以返回的。
def createGenerator():
    mylist=range(3)
    for i in mylist:
        yield i*i

mygenerator =createGenerator()
print mygenerator

for i in mygenerator:
    print ()

