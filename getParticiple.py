#coding:utf-8
import re
from bdurobot import getBaiduList
from getExcel import getCompany
from getExcel import getTitle
from crackerdemo import getGoogleList
from collections import defaultdict
from textProcessing import textprocess
from rules import getRels

from aip import AipNlp

APP_ID = '*'
API_KEY = '*'
SECRET_KEY = '*'
client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

'''
def getNearestPer(ulist):
    mlist={}
    ansstr=""
    for i in ulist['items']:
        minloc=1000000000
        minstr=i['item']
        if i['ne']=='PER' or i['pos']=='nr':
            loc=i['byte_offset']
            for j in ulist['items']:
                if j['ne']=='TITLE' or j['ne']=='ORG':
                    tmploc=abs(loc-j['byte_offset'])
                    tmpsymbol=loc-j['byte_offset']
                    if tmploc<minloc:
                        minloc=tmploc
        if minloc!=1000000000:
            mlist[minstr]=[minloc]
    minsum=1000000000
    minid=-1
    for key,value in mlist.items():
        if value<minsum:
            minid=key
            minsum=value
    if minid!=-1:
        ansstr=minid
    return [minid!=-1,ansstr]
'''


#返回[是否存在一个人，人名，提取到的摘要部分]，以及最近的title或org在person的左和右，
def getNearestPer2(ulist,org,title):
    minlist={}
    ansstr=""
    zhaiyao=""
    tmplist=[]
    sumstr=ulist['text']

    #更新tmplist，找到所有的org和title的offset
    if sumstr.find(org)==-1 or sumstr.find(title)==-1:return [False,0,0]
    a1=sumstr.find(org)
    while a1!=-1 and a1<len(sumstr):
        tmplist.append(a1)
        a1 =sumstr.find(org,a1+1)
    a1=sumstr.find(title)
    while a1!=-1 and a1<len(sumstr):
        tmplist.append(a1)
        a1 =sumstr.find(title,a1+1)

    for i in ulist['items']:
        minloc=1000000000
        minstr=i['item']
        tmpsymbol=0
        loc=0
        aloc=0
        if i['ne'] == 'PER' or i['pos'] == 'nr':
            loc=sumstr.find(i['item'])
            for j in tmplist:
                if abs(loc-j)<minloc:
                    minloc=abs(loc-j)
                    if loc-j>0:
                        tmpsymbol=-1
                        aloc=loc+len(i['item'])-1
                    elif loc-j<0:
                        tmpsymbol=1
                        aloc=loc
                    else:
                        tmpsymbol=0
                        aloc=loc
        if minloc!=1000000000:
            minlist[minstr]=[minloc,tmpsymbol,aloc]
        else:
            continue
    minsum=1000000000
    minid=-1
    minsymbol=0
    minlocation=0
    for key,value in minlist.items():
        if value[0]<minsum:
            minid=key
            minsum=value[0]
            minsymbol=value[1]
            minlocation=value[2]
    if minsum>10:
        return [False,0,0]
    if minid!=-1:
        ansstr=minid
        if minsymbol==1:
            st=minlocation
            tt=sumstr[minlocation:].find(title)
            en=-1
            if tt!=-1:
                en=minlocation+tt+len(title)
            else:
                return [False,0,0]
            zhaiyao=sumstr[st:en]
        elif minsymbol==-1:
            st=minlocation
            tt=sumstr[minlocation::-1].find(org[::-1])
            en=-1
            if tt!=-1:
                en=minlocation-tt-len(org)
            else:
                return [False, 0, 0]
            zhaiyao=sumstr[st:en:-1][::-1]
        else:zhaiyao=""
    else: return [False,0,0]
    return [minid!=-1,ansstr,zhaiyao]



#将摘要分段分句，分词，并得到[]
def getAns(anslist,ulist,org,title):
    for i in ulist:
        i[0]=i[0].encode('gb2312', 'ignore').decode('gb2312').encode('gbk', 'ignore').decode('gbk')
        str = re.split("\.\.\.|。|\. |；", i[0])
        for j in str:
            if j.strip()=="":continue
            tmp=client.lexerCustom(j)
            while 'error_msg' in tmp.keys():
                tmp = client.lexerCustom(j)
            ans=getNearestPer2(tmp,org,title)
            if ans[0]==False:
                continue
            else:
                anslist.append([ans[1],i[1],ans[2]])

#work主函数
def workdemo():
    f = open("/Users/wangkun/Desktop/comdata/text953.txt", 'w')
    titlelist=getTitle()
    #print(titlelist)
    comlist=getCompany()
    #print(comlist)
    for i in comlist:
        #print(i)
        for j in titlelist:
            str=i[0]+"-"+j+":\n"
            f.write(str)
            f.flush()
            anslist=[]
            datalist=defaultdict(list)
            for t in i:
                ulist1=getBaiduList(t,j)
                getAns(anslist,ulist1,t,j)
                #print(anslist)
                #ulist2=getGoogleList(t,j)
                #getAns(anslist,ulist2,t,j)

            # ###去噪音
            # a=defaultdict(int)
            # for k in anslist:
            #     a[k[0]]+=1
            # for key,value in a.items():
            #      if value==1:

            #
            # ###TODO 用祥哥的接口，但目前有问题，需要考虑
            # for k in anslist:
            #     if k[2]:
            #         try:
            #             str=textprocess(k[2])
            #             tt=getRels(str)
            #             for rr in tt:print(rr,end=" ")
            #             for r in tt:
            #                 k[2]=r[1]+r[2]+" "
            #             datalist[k[0]].append([k[1], k[2]])
            #         except:
            #             continue


            for k in anslist:
                if k[2]:
                    try:
                        datalist[k[0]].append([k[1], k[2]])
                    except:
                        continue
            for key, value in datalist.items():
                # print(key)
                f.write(key + "\n")
                for k in value:
                    # print(k[0]+"  "+k[1])
                    f.write(k[0] + "  " + k[1] + "\n")
                    f.flush()
            #f.flush()
    f.close()

###输出格式按要求
'''
def workdemo2():
    f = open("/Users/wangkun/Desktop/text935.txt", 'a+')
    titlelist=getTitle()
    comlist=getCompany()
    for i in comlist:
        for j in titlelist:
            datalist=defaultdict(list)
            str=i+"-"+j+":\n"
            f.write(str)
            #print(i+"-"+j+":")
            ulist=getBaiduList()
            ans=getAns(ulist,i,j)
            for k in ans:
                if k[2]:
                    datalist[k[0]].append([k[1],k[2]])
            for key,value in datalist.items():
                #print(key)
                f.write(key+"\n")
                for k in value:
                    #print(k[0]+"  "+k[1])
                    f.write(k[0]+"  "+k[1]+"\n")
            f.flush()
    f.close()
'''

def checkutility():
    pass
'''
123
'''
workdemo()

