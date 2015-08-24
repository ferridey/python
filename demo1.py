#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/17 13:52:53
#   FileName:   demo1.py
#   Desc    :   
#
from tkinter import *
root = Tk()
root.wm_title("Hello world!<F5>")
w1 = Label(root,text = "This is a sample!")
w1.pack()
l1 = Listbox(root)
l1.pack()
def tips():
    global root
    s = Label(root,text = "I love python!")
    s.pack()
b1 = Button(root,text = "Chuan huan",command = tips)
b1.pack()
root.mainloop()

