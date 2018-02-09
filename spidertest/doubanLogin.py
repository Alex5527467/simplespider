# -*- coding: utf-8 -*-


import urllib
import urllib2
import json
import cookielib
import re
import zlib
import os
import requests
from PIL import Image
from io import BytesIO


import ssl
ssl._create_default_https_context = ssl._create_unverified_context



filename = 'cookie_douban.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)


home_url = 'https://www.douban.com'
auth_url = 'https://www.douban.com/accounts/login'



headers = {
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/64.0.3282.140 Mobile/13B143 Safari/601.1.46',
    'Content-Length': '134',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'https://www.douban.com/accounts/login',
    'Origin': 'https://www.douban.com',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
    'Host': 'accounts.douban.com',
    }




# data
data = {
    'form_email':'xinchen296@163.com',
    'form_password':'Cx55274675527467',
    'redir':'https://www.douban.com',
    'login':'登陆',
    'source':'None',
    'remember':'',
}

post_data=urllib.urlencode(data)


print post_data

req = urllib2.Request(auth_url,data=post_data)


try:

    for key in headers:
            req.add_header(key,headers[key])
    result = opener.open(req)


except urllib2.HTTPError, e:
    print e.getcode()  
    print e.reason  
    print e.geturl()  
    print e.info()
    req = urllib2.Request(e.geturl())
    result = opener.open(req)



#print result.read()
#print result.getSession().getId()


html_content = result.read()
pattern = re.compile(r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>')
imgurl = pattern.findall(str(html_content))
print imgurl
#im_data = urllib2.urlopen(imgurl[0])


response = requests.get(imgurl[0])
image = Image.open(BytesIO(response.content))
image.save('Code.png')







for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value
    
cookie.save(ignore_discard=True, ignore_expires=True)






#cookie.load(filename, ignore_discard=True, ignore_expires=True)
#req = urllib2.Request(auth_url,headers=headers)
#opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
content = response.read()


pattern = re.compile(r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>')
imgurl = pattern.findall(str(content))
print imgurl
#im_data = urllib2.urlopen(imgurl[0])


response = requests.get(imgurl[0])
image = Image.open(BytesIO(response.content))
image.save('Code1.png')


#loginNum = re.findall('<span>(.*?)</span><span class="arrow"></span>',str(content),re.S)
#print loginNum[0]

headers = {
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/64.0.3282.140 Mobile/13B143 Safari/601.1.46',
    'Connection': 'keep-alive',
    'Host': 'www.douban.com',
    'Referer': 'https://www.douban.com/accounts/login',
    'Upgrade-Insecure-Requests': '1',
    
    }


