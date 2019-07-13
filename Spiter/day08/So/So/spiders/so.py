# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['images.so.com']
    url = 'http://images.so.com/zj?ch=beauty&sn={}&listtype=new&temp=1'

    # 重写start_requests()方法
    def start_requests(self):
        # 生成多个url地址,交给调度器入队列
        for page in range(3):
            sn = page * 30
            url = self.url.format(str(sn))

            yield scrapy.Request(
                url=url,
                callback=self.parse_img
            )

    # 定义解析函数
    def parse_img(self,response):
        html = json.loads(response.text)
        # for遍历每张图片信息的字典
        for img in html['list']:
            # 创建item对象
            item = SoItem()
            item['img_link'] = img['qhimg_url']

            # 把链接交给管道文件
            yield item










