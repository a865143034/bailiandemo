#导入用于打开URL的扩展库模块
import urllib.request
#导入正则表达式模块
import re

def OpenUrl(url):
    #将Request类实例化并传入url为初始值，然后赋值给req
    OperateUrl = urllib.request.Request(url)
    #伪装成Chrome浏览器
    OperateUrl.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
    #访问url，并将页面的二进制数据赋值给page
    page = urllib.request.urlopen(url)
    #将page中的内容转换为utf-8编码
    html = page.read().decode('utf-8')
    return html

def GetImg(html):
    # [^"]+\.jpg 匹配除"以外的所有字符多次,后面跟上转义的.和jpg
    adress = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    #返回正则表达式在字符串中所有匹配结果的列表
    imglist = re.findall(adress, html)
    #循环列表的每一个值
    for each in imglist:
        #以/为分隔符，-1返回最后一个值
        filename = each.split('/')[-1]
        #urlretrieve()远程下载imglist中的每一个元素，命名为filename
        urllib.request.urlretrieve(each, filename)

#该模块既可以导入到别的模块中使用，另外该模块也可自我执行
if __name__ == '__main__':
    for i in range(54):
        #定义url，用正则表达式表达不同页面
        url = (r'https://tieba.baidu.com/p/4364768066?see_lz=1&pn=%d'%i)
        #将url作为open_url()的参数，然后将open_url()的返回值作为参数赋给get_img()
        GetImg(OpenUrl(url))