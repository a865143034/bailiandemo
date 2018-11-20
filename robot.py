import urlparse
import os
import string
import urllib
import urllib2
import htmllib
import crawler #导入爬虫模块
def main():
    url=raw_input("Enter a url:")
    if not url :
        return
    robot=crawler.crawler(url) #实例化一个爬虫类
    robot.go() #启动爬虫
    print("all done")

if __name__ == '__main__' :
    main()
