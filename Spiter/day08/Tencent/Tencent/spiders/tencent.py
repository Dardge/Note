# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    # start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557114143837&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def start_requests(self):
        for page_index in range(1,51):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1557114143837&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn' % str(page_index)
            yield scrapy.Request(
                url=url,
                callback=self.parse_one_page
            )
    # 一级页面解析
    def parse_one_page(self,response):
        html = json.loads(response.text)

        for h in html['Data']['Posts']:
            item = TencentItem()

            item['zh_name'] = h['RecruitPostName']
            item['zh_type'] = h['LocationName']
            # 一级页面获取PostId,详情页URL需要此参数
            item['post_id'] = h['PostId']
            # 想办法获取到职位要求和职责,F12抓包,抓到地址
            two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1557122746678&postId=%s&language=zh-cn' % item['post_id']

            yield scrapy.Request(
                url=two_url,
                meta={'item':item},
                callback=self.parse_two_page
            )
    def parse_two_page(self,response):
        item = response.meta['item']
        html = json.loads(response.text)
        # 职责
        item['duty'] = html['Data']['Responsibility']
        # 要求
        item['require'] = html['Data']['Requirement']

        yield item

# 导入item类,创建对象
# items.py中定义数据结构
# pipelines.py打印一下
# settings.py中添加pipeline











