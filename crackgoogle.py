#coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import re
import json
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'accept-language':'zh-CN,zh;q=0.9',
}

'''
headers = {'Accept': '*/*',
           'Accept-Language': 'en-US,en;q=0.8',
           'Cache-Control': 'max-age=0',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
           'Connection': 'keep-alive',
           'Referer': 'http://www.baidu.com/'
           }
'''

def getHTMLText(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''


def fillList(ulist,html):
    soup=BeautifulSoup(html,'lxml')
    #print(soup.prettify())
    #print(soup.head)
    #print(html)
    for node in soup.find_all('div', {'class': 'g'}):
        time_node=node.find('span',{'class':'f'})
        if not time_node: continue
        cite_node = node.find('h3',{'class':'r'}).find('a')
        cite=cite_node['href']
        abstract_node = node.find('span', {'class': 'st'})
        abstract=abstract_node.text
        abstract=abstract.replace('\xa0','')
        abstract=abstract.replace(' - ',',')
        time=time_node.text
        time=time.replace('\xa0','')
        time=time.replace(' - ','')
        ulist.append([time,abstract,cite])

uinfo=[]
url="https://www.google.com.hk/search?q="+"明略数据 CTO"
url1="https://crawler.bailian-ai.com/v1/get_page?sign=123456789&url=https://www.google.com/search?q=明略数据/&region=us"
r=requests.get(url1)
print(r.text)
html=eval(r.text).get('data')
#setting=json.load(r.text)
#print(setting)
# html=getHTMLText(url)
fillList(uinfo,html)
print(uinfo)
print(len(uinfo))


