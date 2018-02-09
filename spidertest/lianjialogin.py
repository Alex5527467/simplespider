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



home_url = 'https://user.lianjia.com/'
auth_url = 'https://upassport.lianjia.com/login?service=https%3A%2F%2Fwww.lianjia.com%2Fuser%2Fchecklogin%3Fredirect%3Dhttp%253A%252F%252Fdl.lianjia.com%252F'
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Connection': 'keep-alive',
    'Host': 'upassport.lianjia.com:443',
    }

# data



session = requests.Session()


#post_data=urllib.urlencode(data)


f = session.get(auth_url,headers=headers)#,verify=False)


pattern = re.compile(r'<input type="hidden" name="execution" value="(.*?)" />')
execution = pattern.findall(str(f.content))[0]
print execution


data = {
    'username': '15004240771', #替换为自己账户的用户名
    'password': 'Cx55274675527467', #替换为自己账户的密码
    'lt': '',
    'execution': execution,
    '_eventId': 'submit',
}
f=session.post(auth_url,data = data,headers = headers)#,verify=False)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Connection': 'keep-alive',
    #'Host': 'upassport.lianjia.com:443',
    }
 
f = session.get(home_url,headers=headers)#,verify=False)


pattern = re.compile(r'<div class="user-name">(.*?)</div>')
execution = pattern.findall(str(f.content))[0].decode('utf-8','ignore').encode("gbk", 'ignore')
print execution











