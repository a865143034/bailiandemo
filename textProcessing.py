#coding:utf-8
import re
from aip import AipNlp

APP_ID = '*'
API_KEY = '*'
SECRET_KEY = '*'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

def textprocess(text):
    #text="明略数据金融事业部解决方案专家杨昀"
    #text="欧链科技联合创始人谭智勇对本报记者解释道"
    ans=client.lexerCustom(text)
    #print(ans)
    str=""
    try:
        for i in ans['items']:
            if i['ne']:
                str+=i['item']+'/'+i['ne']+" "
            else:
                str+=i['item']+'/'+i['pos']+" "
        str=str.replace('TITLE','ti').replace('PER','nr').replace('ORG','nt')
    except:
         return ""
    return str



#textprocess("1")