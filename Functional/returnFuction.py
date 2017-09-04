#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 函数做为返回值
# exp1:可变参数的求和
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 如果不直接求和，而是在后面的代码中，根据需求计算

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 当我们lazy_sum时，返回的并不是求和结果，而是求和函数
f = lazy_sum(1, 3, 5, 7, 9)

# 此时f代表就是函数吗，必须调用才能输出结果
print f()

### 函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
###  相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。