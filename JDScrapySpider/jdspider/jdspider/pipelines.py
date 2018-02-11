# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# encoding=utf8  
import sys    
reload(sys)  
sys.setdefaultencoding('utf8')  
import json
import codecs
import os
import urllib
import requests
from PIL import Image
from io import BytesIO





class JdspiderPipeline:
        # 初始化时指定要操作的文件
        def __init__(self):
                self.file = codecs.open('questions.json', 'w', encoding='utf-8')

        # 存储数据，将 Item 实例作为 json 数据写入到文件中
        def process_item(self, item, spider):
                print len(item['price'])
                fileObject = open('jd.txt', 'w')
                for i in range(0,len(item['price'])):
                        a=item['price'][i]
                        b=item['comment'][i]
                        c=item['product_id'][i]
                        d=item['img_url'][i]
                        if(a<>'' and b<>'' and c<>'' and d<>''):
                                fileObject.write(str(a)+' '+str(b)+' '+str(c)+' '+str(d))
                                fileObject.write('\n')
                lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
                self.file.write(lines)
                if 'img_url' in item:#如何‘图片地址’在项目中
                        head='https:'
                        dir_path='a'
                        if not os.path.exists(dir_path):
                                os.makedirs(dir_path)
                        for i in range(0,len(item['img_url'])):
                                file_name = item['comment'][i]+'.png'
                                file_path = '%s/%s'%(dir_path,file_name)
                                image_url=item['img_url'][i]
                                if os.path.exists(file_name):
                                        continue
                                try:
                                        with open(file_path,'wb') as file_writer:
                                                conn = urllib.urlopen(head+image_url)#下载图片
                                                file_writer.write(conn.read())
                                except:
                                        print "get error"
                                file_writer.close()
                                #name=item['comment'][i]
                                #image_url=item['img_url'][i]
                                #try:
                                #        response = requests.get(head+image_url, stream=True)
                                #        image = Image.open(BytesIO(response.content))
                                #        image.save(name+".png")
                                #except:
                                #        print 'get error'

                return item
            # 处理结束后关闭 文件 IO 流
        def close_spider(self, spider):
                self.file.close()
