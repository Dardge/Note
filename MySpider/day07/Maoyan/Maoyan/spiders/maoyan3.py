# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem


class MaoyanSpider(scrapy.Spider):
    # 爬虫名'maoyan3'
    name = 'maoyan3'
    allowed_domains = ['maoyan.com']

    # 去掉了start_urls
    # 重写了Spider类的start_request()方法
    def start_requests(self):
        # 生成所有的URL地址，统一扔给调度器入队列
        for offset in range(0, 91, 10):
            url = 'https://maoyan.com/board/4?offset=' + str(offset)
            # 把请求url交给调度器入队列
            # 指定解析函数callback=self.parse_html
            yield scrapy.Request(url, callback=self.parse_html)

    def parse_html(self, response):
        # 基准xpath,匹配每个电影节点对象列表
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')

        for dd in dd_list:
            # 创建item对象
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').get()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()[3:]
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()[5:15]

            # 把数据交给管道文件(pipelines.py)去处理
            yield item
