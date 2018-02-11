# -*- coding:utf-8 -*-
import urllib    
import urllib2
import os
import scrapy
from scrapy import Request
from ..items import JdspiderItem
import json
import re


class JDSpider(scrapy.spiders.Spider):
    name = "jdspider"
    allowed_domains = ["jd.com","p.3.cn"]   
    start_urls = ['https://sale.jd.com/act/1faql4puTWQP6.html?cpdad=1DLSUE'] 
    
 
    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())
        

        comment = response.css('div.jDesc::attr(title)').extract()
        #price = response.css('span.jdNum d-jd-price::text').extract()
        jdID = response.xpath('//*[@class="jdNum d-jd-price"]/@jdprice').extract()
        imgfirst = response.xpath('//*[@class="jPic"]')
        imgurl = imgfirst.css('img.J_imgLazyload::attr(original)').extract()#xpath('//*[@class="jPic"]/[@class="J_imgLazyload"]/@original').extract()
        item = JdspiderItem()
        item['price']=[]
        
        #print type(item['product_id'])
        #print len(jdID)
        item['product_id']=jdID
        item['comment']= comment
        item['img_url']= imgurl
        for i in range(0,len(jdID)):
            url='https://p.3.cn/prices/mgets?skuIds=J_'+jdID[i]
            req = urllib2.Request(url)
            source_code = urllib2.urlopen(req).read()
            price = re.findall('"p":"(.*?)"}]',source_code,re.S)
            item['price'].append(price)
            #yield Request(url,meta={'item':item},callback=self.price_parse)
        yield item


    def price_parse(self,response):
        price = re.findall('"p":"(.*?)"}]',response.body,re.S)
        item = response.meta['item']
        print 'ok'
        item['price'].append(price)
        #print item['product_id']
        #return item
        
        

#scrapy startproject jdspider        
#scrapy crawl jdspider --nolog
