import urllib.request
f = urllib.request.urlopen('http://www.python.org/')
print(f.read().decode('utf-8'))
input()
