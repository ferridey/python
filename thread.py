#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/12 14:02:33
#   FileName:   thread.py
#   Desc    :   
#
import threading
import time

class MeThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
        self.create_time = time.time()

    def run(self):
        time.sleep(1)
        print('Thread',self.num,'Created!')
        print(time.time() - self.create_time)
        print('Thread',self.num,'over')
        
for item in range(8):
    t = MeThread(item)
    t.start()

input()
