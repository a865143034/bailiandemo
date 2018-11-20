#coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import re
import json
import datetime
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'accept-language':'zh-CN,zh;q=0.9',
    'Referer': 'http://www.baidu.com/',
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
    for node in soup.find_all('div', {'class': 'g'}):
        time_node=node.find('span',{'class':'f'})
        if not time_node: continue
        tmp_node = node.find('h3',{'class':'r'})
        if not tmp_node:continue
        cite_node=tmp_node.find('a')
        if not cite_node:continue
        cite=cite_node['href']
        abstract_node = node.find('span', {'class': 'st'})
        abstract=abstract_node.text
        abstract=abstract.replace('\xa0','')
        abstract=abstract.replace(' - ',',')
        time=time_node.text
        time=time.replace('\xa0','')
        time=time.replace(' - ','')
        ulist.append([abstract,time,cite])

def getDate():
    i=datetime.datetime.now()
    #now_time=i.strftime('%m/%d/%Y')
    p1_year=i.year-1
    p2_year=i.year-2
    p3_year=i.year-3
    str0 = "{}/{}/{}".format(i.month, i.day, i.year)
    str1="{}/{}/{}".format(i.month,i.day,p1_year)
    str2 = "{}/{}/{}".format(i.month, i.day, p2_year)
    str3 = "{}/{}/{}".format(i.month, i.day, p3_year)
    return [str0,str1,str2,str3]


def getGoogleList(org,title):
    uinfo=[]
    keyword=org+" "+title
    #tmpurl = "https://www.google.com.hk/search?q=" +keyword
    datelist=getDate()
    #print(datelist)
    for i in range(3):
        tmpurl=f"https://www.google.com.hk/search?q={keyword}%26safe=strict%26hl=zh-CN%26lr=lang_zh-CN%26tbs=cdr:1,cd_min:{datelist[i+1]},cd_max:{datelist[i]}"+"%26pws:pws=0%26filter:1%26tbm="
        url = "https://crawler.bailian-ai.com/v1/get_page?sign=123456789&url="+tmpurl+"&region=us"
        r = requests.get(url)
        html = eval(r.text).get('data')
        fillList(uinfo,html)
    return uinfo
'''
def getGoogleList1(org,title):
    uinfo=[]
    keyword="\""+org+"\" \""+title+"\""
    tmpurl=f"https://www.google.com.hk/search?q={keyword}"
    #print(tmpurl)
    url = "https://crawler.bailian-ai.com/v1/get_page?sign=123456789&url="+tmpurl+"&region=us"
    r = requests.get(url)
    html = eval(r.text).get('data')
    fillList(uinfo,html)
    return uinfo
'''
ans=getGoogleList("明略数据","CTO")
print(len(ans))
for i in ans:
    print(i[1])
