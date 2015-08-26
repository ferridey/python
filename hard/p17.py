#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/26 21:09:10
#   FileName:   p17.py
#   Desc    :   
#
from sys import argv
from os.path import exists

script,from_file,to_file = argv

print("Copying from %s to %s" % (from_file,to_file))

# we could do these two on one line to ,how ?
indata = open(from_file).read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready,hit RETURN to continue,CTRL-C to abort.")
input()

output = open(to_file,'w').write(indata)

print("Alright,all done.")

#output.close()
#indata.close()
