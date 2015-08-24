#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/06 19:09:24
#   FileName:   test1.py
#   Desc    :   
#
import pickle
class Person:
    pass
p = Person()
f = open('test','wb')
pickle.dump(p,f)
