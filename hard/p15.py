#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/26 20:38:51
#   FileName:   p15.py
#   Desc    :   
#
from sys import argv

script,filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = input(">")

txt_again = open(file_again)

print(txt_again.read())



