#!/usr/bin/env python
# -*- coding: utf-8 -*

# 在python中，一边循环一边计算的机制，称为生成器

# 把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]

g = (x * x for x in range(10))

# L和g的区别在于:外层[]和(),L是个list，g是个generator
# 获取生成器的返回值
print next(g)

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 使用for循环进行输出
for n in g:
    print (n)


# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n > max:
        print (b)
        a, b = b, a + b
    return 'done'
