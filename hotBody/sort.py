#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 创建类
class Student:
    ' 类的帮助信息'
    # 类变量
    stuCount = 0


    def __init__(self,name, age):
        self.name = name
        self.age = age
        Student.stuCount += 1

    def displaySage(self):
        print "年龄:", self.age

    def displayName(self):
        print "名字是:", self.name


stu1 = Student("小明", 12)
stu2 = Student("小红", 14)
stu3 = Student("小黄", 13)
stu1.displaySage()
stu2.displayName()

studentList = [stu1, stu2, stu3]


def ageList(student):
   return student.age


list = sorted(studentList, key=ageList,reverse = True)


print list





