#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   ferridey
#   E-mail  :   ferridey@gmail.com
#   Date    :   15/08/10 18:58:14
#   FileName:   request.py
#   Desc    :   
#
import urllib.request
import urllib

data = {}
data['word'] = 'Jecvay Notes'

url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
full_url = url + url_values

data = urllib.request.urlopen(full_url).read()
data = data.decode('UTF-8')
print(data)

print(full_url)


#print(help(data))

