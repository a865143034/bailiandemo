#-------------------------------------------------------------------------------
# Name:        抓取url类
#-------------------------------------------------------------------------------
import urlparse
import os
import string
import urllib
import htmllib
import formatter
import cStringIO
import sys
class retriever(object) :
    #初始化
    def __init__(self,url):
        self.url=url
        self.file=self.filename(url) #解析并计算文件路径
    #解析url，创建目录，返回保存路径
    def filename(self,url):
        parserurl=urlparse.urlparse(url,"http:",0)
        path=parserurl[1]+parserurl[2] #文件路径，域名和脚本的组合
        ext=os.path.splitext(path) #截取路径后缀
        if ext[1] == "" : #如果没有后缀，则添加index.html作为默认文件名
            if path[-1] == "/" :#路径是否以/结尾，否则添加结尾
                path+="index.html"
            else:
                path+="/index.html"

        ldir=os.path.dirname(path) #得到目录名
        if os.sep != "/" : #判断当前环境路径分隔符是否为/，否则替换掉
            ldir=string.replace(ldir,"/",os.sep)
        if not os.path.isdir(ldir) :#判断目录不存在的话则创建
            try:
                os.makedirs(ldir) #递归的创建所有目录
            except Exception,e:
                print "mkdir failed,ldir:%s url:%s error:%s" %(ldir,url,e)

        return path #将文件路径返回
    #下载动作
    def download(self):
        try:
            retval=urllib.urlretrieve(self.url,self.file)
        except IOError :
            retval="*"
        return retval #返回结果
    def parseandgetlinks(self) :
        self.parser=htmllib.HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
        self.parser.feed(open(self.file).read()) #将已下载的页面内容读取出字符串，赋给feed进行解析
        self.parser.close() #关闭HTMLParser类
        return self.parser.anchorlist #返回解析到的链接列表


def main():
    pass

if __name__ == '__main__':
    main()
