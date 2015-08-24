#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/21 20:20:34
#   FileName:   spider1.py
#   Desc    :   
#http://blog.jobbole.com/77830/
import re
import os
import urllib.request
import urllib
#import time
import http.cookiejar

from collections import deque

queue = deque()
visited = set()

#head: dict of header
#构造一个浏览器opener
def makeMyOpener(head = {
    'Connetion':'Keep-Alive',
    'Accept':'text/html,application/xhtml+xml,*/*',
    'Accetp-Language':'en-Us,en;q=0.8,zh-Hans-cn;q=0.5,zh-Hans;q=0.3',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3;WOW64;Trident/7.0;rv:11.0)like Gecko'
    }):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

        
url = "http://www.liaoxuefeng.com/"

queue.append(url)
cnt = 0
log = open('date','w')


opener = makeMyOpener()

while queue:
    url = queue.popleft()
    visited |={url} #visited = visited | {url}

    print('already captured:'+str(cnt)+"capturing <----"+url)
    cnt+=1
    urlop = opener.open(url,timeout = 1000)
    try:
        if "html" not in urlop.getheader('Content-Type'):
            continue
        data = urlop.read().decode('utf-8')
    except:
        continue

#    time.sleep(2)
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('appending queue ---->'+x)
            log.write(x + os.linesep)

print('总计统计{}个地址。'.format(cnt))
