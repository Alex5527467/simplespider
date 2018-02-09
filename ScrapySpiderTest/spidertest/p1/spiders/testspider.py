# -*- coding:utf-8 -*-
import scrapy
import os
from scrapy import Request
#from p1.items import WeatherItem

class WeatherSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains = ["sina.com.cn"]   
    start_urls = ['http://weather.sina.com.cn'] 

 
    def parse(self, response):
        # print(response, type(response))
        # from scrapy.http.response.html import HtmlResponse
        # print(response.body_as_unicode())

        #item = WeatherItem() #把WeatheItem()实例化成item对象
        #address = response.xpath('//*[@id="slider_ct_name"]/text()').extract()#//*：选取文档中的所有元素。@：选择属性 /：从节点选取 。extract():提取
        address = response.css('div.slider_w::attr(data-cityenname)').extract()
        #data = response.xpath('//*[@id="slider_ct_header"]/text()').extract()
        date1 = response.xpath('//*[@class="slider_ct_date"]/text()').extract()
        tenDay = response.xpath('//*[@id="blk_fc_c0_scroll"]');
        date = tenDay.css('p.wt_fc_c0_i_date::text').extract()
        #date = tenDay.css('p.slider_ct_date::text').extract()
        dayDesc = tenDay.css('img.icons0_wt::attr(title)').extract()
        dayTemp = tenDay.css('p.wt_fc_c0_i_temp::text').extract()
        print address[0],date[0],dayDesc[0],dayTemp[0],date1[0]
        #return item

