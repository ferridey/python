#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/06 18:20:35
#   FileName:   test.py
#   Desc    :   
#
#data = open('data.txt','a')
#data.write('this is a test!')
#data.close()
#out = open('data.txt')
for line in open('data.txt'):
    print(line,end = '\t')

out = open('data.txt','a')
while True:
    strings=input('Enter your text:')+'\n'   
    if strings[:-1]=='quit':
        break
    else:
        out.write(strings)
out.close()
