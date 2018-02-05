import urllib    
import urllib2
import string
import re
import os
import traceback
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

url1 = 'http://movie.douban.com/top250'
pages = [0,25,50,75,100,125,150,175,200,225]
allmovie = []
allurl=[]
#import pdb
#pdb.set_trace()

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36"}


def get(url):
    try:
        req = urllib2.Request(url)
        for key in headers:
            req.add_header(key,headers[key])
        source_code = urllib2.urlopen(req).read().decode('utf-8','ignore').encode("gbk", 'ignore')
        plain_text=str(source_code)
    except:
        f=open("c:log.txt",'a')  
        traceback.print_exc(file=f)  
        f.flush()  
        f.close()
    return plain_text
def spider_context(url):      
	code = get(url)
	info = re.findall('<ol class="grid_view">(.*?)</ol>',code,re.S)
	mov_url = re.findall('<a href="(.*?)"',info[0],re.S)
	movie = re.findall('alt="(.*?)" src',info[0],re.S)
	#star = re.findall('><em>(.*?)</em></span>',info[0],re.S)
	return movie,mov_url

for page in pages: 
    address = 'http://movie.douban.com/top250?start=' + str(page) + '&filter=&type='
    movie,mov_url=spider_context(address)
    allmovie.extend(movie)
    allurl.extend(mov_url)

#i = 0 
#for mov in movie:
#    allmovie.append((mov,mov_url[i]))
#    i=i+1

fileObject = open('All_Movies.txt', 'w')
for i in range(0,len(allmovie)):
    fileObject.write(str(i)+' '+str(allmovie[i])+' '+str(allurl[i]))
    fileObject.write('\n')

fileObject.close()

