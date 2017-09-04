#!/usr/bin/env python
# -*- coding: utf-8 -*

# 高级特性：切片，迭代，列表生成器，迭代器
# 切片

L = ['Michael', 'Job', 'Marry', 'Bob', 'Sarah', 'Tracy']
# 取前三个元素？

# 笨方法
print L[0], L[1], L[2]

# 取n个元素，就是索引为0-(N-1)的元素，用循环
# 科普：range(a,b)默认从a到b(不包括b),
# range(5):代表0-4
r = []
n = 3
for i in range(n):
    r.append(L[i])

print '使用循环:'
print r

# 主角登场：切面（Slice）
print '使用切片的效果:'
print L[0:3]
print L[1:3]

# 创建一个0-99的数列
LL = list(range(100))
# 取出前十个数
print LL[:10]
# 前10个，每两个取一个
print LL[:10:2]

# 所有数，每5个取一个
print LL[::5]

# 复制一个list
LL[:]
#tuple也是一种list,唯一的区别是tuple不可变。
