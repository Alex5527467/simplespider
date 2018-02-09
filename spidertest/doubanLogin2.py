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



home_url = 'https://www.douban.com'
auth_url = 'https://www.douban.com/accounts/login'
 
headers = {
    'Cache-Control': 'max-age=0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    #'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko) CriOS/64.0.3282.140 Mobile/13B143 Safari/601.1.46',
    'Upgrade-Insecure-Requests': '1',
    'Connection': 'keep-alive',
    'Host': 'www.douban.com',
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

session = requests.Session()
f = session.get(auth_url,headers=headers,verify=False)
#print f.content


pattern = re.compile(r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>')
imgurl = pattern.findall(str(f.content))
print imgurl


 
f=session.post(auth_url,data = post_data,headers = headers,verify=False)
pattern = re.compile(r'<img id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"/>')
imgurl = pattern.findall(str(f.content))
print imgurl
 
#f = session.get('http://www.v2ex.com/settings',headers=header)
#print(f.content.decode())
