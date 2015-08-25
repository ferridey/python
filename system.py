#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/25 22:09:25
#   FileName:   system.py
#   Desc    :   
#
import os

#os.curdir
os.system("ls -al > list.dat")


filename = r"list.dat"
if os.path.exists(filename):
    with open(filename) as f:
        f.read()
        print(f)
else:
    print("filename is not exists")
