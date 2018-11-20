#coding:utf-8
import re
import datetime
str="我是/123/456,789. 100...111。222..."
str=re.split("\.\.\.|。|\. |；",str)
print(str)
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
    # print(str0)
    # print(str1)
    # print(str2)
    # print(str3)
    return [str3,str2,str1,str0]


print(getDate())