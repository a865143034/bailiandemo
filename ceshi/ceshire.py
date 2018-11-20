#coding:utf-8
import re
#search、match、finditer返回的是match对象
#函数式用法
#匹配ip地址

#findall捕获的是括号
str=r'(?:(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}(?:[1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])'
str1=r'(([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])\.){3}([1-9]?\d|1\d{2}|2[0-4]\d|25[0-5])'
p=re.compile(str)
#print(p.match('127.0.0.1'))
# ans=p.search('127.0.0.1')

'''
res=re.search(str1,'127.0.0.1/255.255.255.255')
print(res.group(0))
# print(ans.group(0))
ans=p.findall('127.0.0.1/255.255.255.255')
print(ans)

ans=re.findall(str,'127.0.0.1/255.255.255.255')
print(ans)
'''
#match=re.search('')
'''
match=re.match(r'[1-9]\d{5}','100081 BIT')
if match:
    print(match.group(0))
'''
#findall方法返回的是一个list
# ls=re.findall(r'[1-9]\d{5}','BIT100081 TSU100084')
# print(ls)

# ans=re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
# print(ans)
# #finditer返回的是一个match对象的迭代器，迭代器使用for循环来获得
# # for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
# #     if m:
# #         print(m.group(0))
for m in p.finditer('127.0.0.1/255.255.255.255'):
    if m:
        print(m.group(0))
'''
res=re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
print(res)
'''
#group(0)是返回所有匹配结果


#面向对象用法：编译后的多次操作
#regex=re.compile(pattern)
#search返回的是第一个结果
# m=re.search(r'[1-9]\d{5}','BIT100081 TSU100084')
# print(m.string)
# print(m.re)
# print(m.pos)
# print(m.endpos)
# print(m.group(0))
