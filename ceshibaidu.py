#coding:utf-8
import requests
from bs4 import BeautifulSoup
import bs4
import re
headers = {
    'User-Agent':'Chrome/68.0.3440.106'
}

def getHTMLText(url):
    try:
        r=requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        print(r.text)
    except:
        return ''




href="http://www.baidu.com/link?url=zz_bUdP4btMhRGIZVhYaxZDu6YJOVWeQH61v6nYTT1z2TlWjc40h-BEqPGXLzj_mkQYQqDJKVPocWWi8NqF7Ra"
getHTMLText(href)
