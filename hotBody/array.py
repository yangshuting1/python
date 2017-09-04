#!/usr/bin/env python
# -*- coding: utf-8 -*

#Num1: study dict and set

names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]

# 类似于key-value
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print d['Michael']

#查询是否存在
'Michael' in d
print True or False

d.get('Michael')
print None or 'value'

#删除
d.pop('Bob')
print 'I delete Bob after:' + str(d)



#Num2: Set:一组key的集合，但不存储value,而且是有序的
s = set([1,2,3])
ss = set([1, 2, 3,3])
print ss

# 添加重复的，但是不会有效果
ss.add(4)
print ss
ss.add(4)
print ss

# 删除
ss.remove(4)
print ss

#无序&无重复元素的集合，做交集，并集处理
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print 's1和s2的交集'+str(s1 & s2)

print 's1和s2的并集'+str(s1| s2)

#Conclusion:set和dict的唯一区别在于：没有存储对应的value值。

#Num3：不可变对象
# list是可变的）
list1 = ['c', 'b', 'a']
list1.sort()
print list1

#（str是不可变的，
num1 = 'abc'
num1.replace('a', 'A')
print num1

# 修改
num2 = num1.replace('a', 'A')
print num2

#Conclusion:num1是变量，而'abc'是字符串对象

