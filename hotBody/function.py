#!/usr/bin/env python
# -*- coding: utf-8 -*

#Num1:调用函数

# 求绝对值
print abs(100)
print abs(-12.34)

# 求最大值
print max(1, 2, 100)

# 类型转换
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print bool(1)

# 定义
def first(x):
    if x >= 0:
        return x
    else:
        return -x

print first(111)

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print fact(3)

# 位置参数:对于power(x)函数来说，x就是一个位置参数，当调用时，必须传入有且仅有一个参数x
def power(x):
    return x * x

# 三阶函数
def power(x,n):
    s=1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(4, 3)

# 默认参数
def power1(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s

# 把参数的默认值设定后，传参的时候就不用传,降低了函数调用的难度
print power1(4)

# practice:一年级小学生注册的函数，需要传入name和gender两个参数，城市
def enroll(name,gender):
    print ('name:', name)
    print ('gender:', gender)

enroll('cc', 'F')
# 还要传入年龄、城市，但大多数学生注册时不需要提供年龄和
def enrolls(name,gender,age=9,city='Henan'):
    print ('name:', name)
    print ('gender:', gender)
    print ('age:', age)
    print ('city:', city)

enrolls('sugar', 'F')

#可变参数命名:
# 给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
# 个数不确定，所以想到可以把a，b，c……作为一个list或tuple传进来，函数定义如下：
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 调用时，组装list或tuple
print calc([1, 2, 3])


# 把参数变成可变参数 *numbers
def calc1(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 仅在number加一个*号，在函数内部，参数numbers接收到的是一个tuple
print calc1(1, 2, 3)

# 如果已经有一个list，或tuple
nums = [1, 2, 3]
print calc1(*nums)


# 关键字参数:扩展函数的功能
# 允许你传入0个或任意个含-参数名-的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', '18', city='Beijing')
person('Amy', '22', city='Beijing', gender='F')

# 组装dict
extra = {'city': 'Beijing', 'gender': 'A'}
person('Jack', '25', city=extra['city'],gender=extra['gender'])
# 简化
person('jack', '25', **extra)

# 命名关键字参数
# 在函数内部通过kw检查关键字参数
def person1(name,age,**kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        pass
    print ('name:', name, 'age:', age, 'other:', kw)

person1('Jack', '25', city=extra['city'], gender=extra['gender'])















