#name:crawler
import retriever  #导入页面下载类
import string
import urlparse
import threading
import time
class mythread(threading.Thread) :
    def __init__(self,func,args="",name=''):
        threading.Thread.__init__(self)
        self.func=func
        self.args=args
        self.name=name
    def run(self) :
        apply(self.func,self.args)
class crawler(object):
    count = 0 #静态变量，已下载页面计数
    def __init__(self,url):
        self.q=[url]
        self.seen=[]
        self.domain=urlparse.urlparse(url)[1] #获取目标站域名

    #下载url的页面
    def getPage(self,url):
        r=retriever.retriever(url) #实例化一个下载类
        retval=r.download() #下载该url
        if retval=="*":
            print '%s catched failed' % url
            return

        crawler.count+=1 #成功下载一个页面，计数器+1
        print "(%d)%s=>%s" % (crawler.count,url,retval[0])
        self.seen.append(url)
        links=r.parseandgetlinks()#解析当前页面包含的链接列表
        for eachlink in links :
            if eachlink[:4]!='http' and string.find(eachlink,'://')==-1 :#判断是否下级页面
                eachlink=urlparse.urljoin(url,eachlink)#将相对路径补全为绝对路径,好方便哈哈
            if eachlink[:4]!='http' : #过滤非http链接
                continue
            #print "*",eachlink

            if eachlink not in self.seen :
                if string.find(eachlink,self.domain) != -1 :
                    if eachlink not in self.q :
                        self.q.append(eachlink)
            else :
                #print u'……已经在队列中'
                pass

    #蜘蛛启动
    def go(self):
        while self.q:
            url=self.q.pop()
            self.getPage(url)




def main():
    pass

if __name__ == '__main__':
    main()
