#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re#正则表达式库
r=requests.get('http://python123.io/ws/demo.html')
demo=r.text
soup=BeautifulSoup(demo,'html.parser')
soup.prettify()#
#for link in soup.find_all('a'):
for link in soup('a'):
    print(link.get('href'))

print(soup.a.next_siblings)