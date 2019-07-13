# -*- coding: utf-8 -*-
import scrapy, json
from ..items import *


class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['images.so.com']
    url = 'http://images.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'

    def start_requests(self):
        for page in range(3):
            url = self.url.format(page * 30)
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        html = json.loads(response.text)
        for i in html['list']:
            item = SoItem()
            item['name'] = i['title']
            item['img_link'] = i['qhimg_url']
            print(item['img_link'],item['name'])
            yield item
