#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/06 10:09:07
#   FileName:   class.py
#   Desc    :   
#
class SchoolMeber:
    '''Reprent any school member'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialize SchoolMeber:{0})'.format(self.name))

    def tell(self):
        '''Tell my details.'''
        print('Name:"{0}" Age:"{1}"'.format(self.name,self.age),end =' ')

class Teacher(SchoolMeber):
    def __init__(self,name,age,salary):
        SchoolMeber.__init__(self,name,age)
        self.salary = salary
        print('(Initialized Teacher:{0})'.format(self.name))

    def tell(self):
        SchoolMeber.tell(self)
        print('Salary:"{0:d}"'.format(self.salary))

class Student(SchoolMeber):
    '''Represets student'''
    def __init__(self,name,age,marks):
        SchoolMeber.__init__(self,name,age)
        self.marks = marks
        print('(Initialized Student:{0})'.format(self.name))

    def tell(self):
        SchoolMeber.tell(self)
        print('Marks:"{0:d}"'.format(self.marks))

t = Teacher('Mrs.shividya',30,30000)
s = Student('swaroop',25,75)

print()

members=[t,s]
for member in members:
    member.tell()

