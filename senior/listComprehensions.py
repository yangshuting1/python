#!/usr/bin/env python
# -*- coding: utf-8 -*

# exp1:生成list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(range(1, 11))

# exp2:生成[1x1, 2x2, 3x3, ..., 10x10]，怎么办?
L = []
for x in range(1, 11):
    L.append(x * x)

# 更优：
[x * x for x in range(1, 11)]

# 筛选出偶数的平方
[x * x for x in range(1, 11) if x % 2 == 0]

# 使用两层循环，生成全排列('ABC'中的每个字母与'XYZ'中的每个字母进行拼接)
[m + n for m in 'ABC' for n in 'XYZ']

# exp3:列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

[d for d in os.listdir('.')]  # os.listdir可以列出文件和目录

# exp4:可以用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.items()]

# exp5:最后把一个list中所有字符变成小写
L = {'Hello', 'World', 'IBM', 'Apple'}
[s.lower() for s in L]

# exp6:使用内建的isinstance函数可以判断一个变量是不是字符串

x = 'abc'
y = 123
isinstance(x, str)  # True

# exp7:
L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]
