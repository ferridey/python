#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/21 08:40:11
#   FileName:   dirwalks.py
#   Desc    :   
#
import os
import time

begin = time.clock() #record begin time
# add start path
root = r"E:\ferridey\Calibre Library"
save = open(r"d:\python\save.dat","w")
count = 0
pdf = 0
mobi = 0
epub = 0
for dirpath,dirnames,filenames in os.walk(root):
    for names in filenames:
        count += 1
        if names[-4:] == ".pdf":
            pdf += 1
        elif names[-5:] == ".mobi":
            mobi += 1
        elif names[-5:] == ".epub":
            epub += 1
        save.write(dirpath+"\\"+names+os.linesep)
print("总计扫描到{0}个文件".format(count))
print("其中PDF文件{0}个，MOBI文件{1}个,EPUB文件{2}个".format(pdf,mobi,epub))
print("总计耗时：{0}秒".format(time.clock()-begin))
print("done!")
