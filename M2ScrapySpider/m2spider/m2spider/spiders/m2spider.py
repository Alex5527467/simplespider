# -*- coding:utf-8 -*-
import urllib    
import urllib2
import os
import scrapy
from scrapy import Request
#from ..items import m2spiderItem
import json
import re

import requests
from PIL import Image
from io import BytesIO


class M2Spider(scrapy.spiders.Spider):
    name = "m2spider"
    allowed_domains = ["mm2mm.com"]   
    start_urls = ['http://www.mm2mm.com/rentiyishu/'] 
    
 
    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())
        

        
        imgtemp1 = response.xpath('//*[@class="img_inner_wrapper_tag"]')
        imgtemp2 = imgtemp1.xpath('//*[@class="title"]')
        imgurl = imgtemp2.css('a::attr(href)').extract()
        comment = imgtemp2.css('a::text').extract()
        url_head = 'http://www.mm2mm.com'
        for i in range(0,len(imgurl)):
            url=url_head+imgurl[i]
            #print url
            yield Request(url,meta={'urlfirst':imgurl[i]},callback=self.deep_parse)


    def deep_parse(self, response):
        url_head = 'http://www.mm2mm.com'
        urlfirst = response.meta['urlfirst']
        imgtemp3 = response.xpath('//*[@class="pages"]')
        imgurl = imgtemp3.xpath('a/@href').extract()
        imgurl.pop()
        del imgurl[0]
        imgurl[0]=urlfirst
        #print imgurl
        for i in range(0,len(imgurl)):
            url=url_head+imgurl[i]
            yield Request(url,meta={'num':i},callback=self.read_parse)
        

    def read_parse(self,response):
        num = response.meta['num']
        print num
        imgtemp4 = response.xpath('//*[@class="srcPic"]')
        imgurl = imgtemp4.css('img::attr(src)').extract()
        imgname = imgtemp4.css('img::attr(title)').extract()

        dir_path='rentiyisu'
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            
        file_name = imgname[0]+str(num)+'.png'
        file_path = '%s/%s'%(dir_path,file_name)
        image_url=imgurl[0]
        #if os.path.exists(file_name):
        try:
            with open(file_path,'wb') as file_writer:
                conn = urllib.urlopen(image_url)#下载图片
                file_writer.write(conn.read())
        except:
            print "get error"
        
        #print imgurl,imgname

        

#scrapy startproject jdspider        
#scrapy crawl jdspider --nolog
