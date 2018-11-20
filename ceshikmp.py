#coding:utf-8

# def CountChar(sText):
#     if not isinstance(sText, unicode):
#     sText=sText.decode("utf-8")
#     return len(sText)
import re
test_str=u"我是12"
test_str_unicode = test_str.encode('utf-8')
#print(len(test_str_unicode))
'''
str1="我是123"
pa=re.compile()
str2="23"
#print(str1.findall(str2,pa))

pattern = re.compile('123')
list1 = pattern.findall('我是123我是123')
print(list1)
'''
p = re.compile('1')
print(p.findall('one1two1three1four1'))