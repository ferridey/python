#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/06 20:23:22
#   FileName:   p8.py
#   Desc    :   
#
formatter = "%r %r %r %r"

print(formatter % (1,2,3,4))
print(formatter % ("one","two","three","four"))
print(formatter %(True,False,False,True))
print(formatter % (formatter,formatter,formatter,formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right",
    "But is didn't sing.",
    "So I said goodnight."
    ))

