# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import *


class TencentSpider(scrapy.Spider):
    name = 'tencent'

    allowed_domains = ['www.tencent.com']

    def start_requests(self):
        for page in range(1, 21):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?&pageIndex={}&pageSize=10'.format(page)
            yield scrapy.Request(url=url, callback=self.parse_one_page)

    def parse_one_page(self, response):
        html = json.loads(response.text)
        for item in html['Data']['Posts']:
            post_id = item['PostId']
            two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?&postId={}'.format(post_id)
            yield scrapy.Request(url=two_url, callback=self.parse_two_page, dont_filter=True)

    def parse_two_page(self, response):
        item = TencnetItem()
        html = json.loads(response.text)
        item['job_title'] = html['Data']['RecruitPostName']
        item['job_duty'] = html['Data']['Responsibility']
        item['job_requirement'] = html['Data']['Requirement']
        return item
