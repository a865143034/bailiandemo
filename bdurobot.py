#coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import re
import string
import time
#from getParticiple import getNearestPer2
from aip import AipNlp

APP_ID = '*'
API_KEY = '*'
SECRET_KEY = '*'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)


headers = {
    'User-Agent':'Chrome/68.0.3440.106'
}

def getHTMLText(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ''

def bdurlCode(url):
    res = requests.get(url, allow_redirects=False)
    Real_url = res.headers['location']
    return Real_url

def fillList(ulist,html):
    soup=BeautifulSoup(html,'lxml')
    #print(soup.prettify())
    for node in soup.find_all('div', {'class': 'result c-container '}):
        abstract_node = node.find('div',{'class':'c-abstract'})
        cite_node = node.find('a', {'class': 'c-showurl'})
        time_node=node.find('span',{'class':' newTimeFactor_before_abs m'})
        if not time_node:continue
        if not cite_node:continue
        if not abstract_node:continue
        url=cite_node['href']
        url=bdurlCode(url)
        abstract=abstract_node.text
        time=time_node.text
        ulist.append([abstract,time,url])
    for i in ulist:
        i[0] = i[0].replace('\xa0-\xa0',',')
        i[1] = i[1].replace('\xa0-\xa0','')

def getBaidudate():
    n1=int(time.time())
    n2=n1-31536000
    n3=n2-31536000
    n4=n3-31536000
    listdemo=[n1,n2,n3,n4]
    # for i in listdemo:
    #     print(i)
    return listdemo

def getBaiduList(org,title):
    datelist=getBaidudate()
    uinfo=[]
    keyword="\""+org+"\" \""+title+"\""
    for i in range(3):
        for j in range(10):
            tmpurl=f"%26gpc=stf={datelist[i+1]},{datelist[i]}|stftype=2%26tfflag=1%26pn={j*10}"
            url1="http://www.baidu.com/s?wd="+keyword+tmpurl
            url="https://crawler.bailian-ai.com/v1/get_page?sign=123456789&url="+url1+"&region=cn"
            #html=getHTMLText(url1)
            #fillList(uinfo,html)
            r = requests.get(url)
            html = eval(r.text).get('data')
            fillList(uinfo,html)
    return uinfo


def checkBaidudemo(org,title,per):
    uinfo=[]
    keyword="\""+org+"\" \""+title+"\""
    url1="http://www.baidu.com/s?wd="+keyword
    url="https://crawler.bailian-ai.com/v1/get_page?sign=123456789&url="+url1+"&region=cn"
    #html=getHTMLText(url1)
    #fillList(uinfo,html)
    r = requests.get(url)
    html = eval(r.text).get('data')
    fillList(uinfo,html)
    for i in uinfo:
        client.lexerCustom(i[0])
        getNearestPer2(uinfo,org,title)
    #for i in llist:


    return uinfo

ans=getBaiduList("腾讯","CTO")
print(ans)
print(len(ans))
#print(int(time.time()))
#str1="http://www.baidu.com/s?wd=明略数据 CTO&gpc=stf=1435180806.424494,1535180806.424494|stftype=2&tfflag=1"

#getBaidudate()