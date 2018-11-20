# coding:utf-8
import urllib
import re
from bs4 import BeautifulSoup
'''

url = 'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=johnkey&oq=john&rsv_pq=88bbfd770000beed&rsv_t=be24xj7KYq9tbjeRa7Fu10sW1dFF0GNZI1%2FW31Bq8OsZWZIwSpuRZxdcfQo&rqlang=cn&rsv_enter=1&inputT=787&rsv_sug3=12&rsv_sug1=7&rsv_sug7=100&rsv_sug2=0&rsv_sug4=787'


request = urllib.Request(url)
request.add_header('User-Agent','Mozilla/5.0')
response = urllib.urlopen(request)


html = response.read()


soup = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
links = soup.find_all('div',id=re.compile(r'\d+'))
for link in links:
    print(link.name,link['id'],link.get_text())
'''
'''
str="123"
str2=str[2:0:-1].find('2')
print(str2)
'''
#print('\u2022')
#生成一个字典
d = {'name':{},'age':{},'sex':{}}
#打印返回值，其中d.keys()是列出字典所有的key
print('name' in d.keys())
#结果返回True