# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    offset = 0
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def parse(self, response):
        # 基准xpath, 匹配每个电影信息节点对象列表
        dd_list = response.xpath(
            '//dl[@class="board-wrapper"]/dd'
        )
        for dd in dd_list:
            # 创建item对象
            item = MaoyanItem()
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()

            # 把数据交给管道文件(pipelines.py)去处理
            yield item

        # 想办法生成下一页的URL地址
        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset=' \
                                    + str(self.offset)
            # 交给调度器入队列
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )









