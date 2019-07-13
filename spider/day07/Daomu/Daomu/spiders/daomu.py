# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # 一级页面的解析函数，提取盗墓笔记1-8链接，发给调度器入队列
    def parse(self, response):
        one_link_list = response.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        # 把请求发给调度器
        for one_link in one_link_list:
            yield scrapy.Request(one_link, callback=self.parse_two_link)
            # print(one_link)

    # 解析二级页面
    def parse_two_link(self, response):
        article_list = response.xpath('/html/body/section/div[2]/div/article')
        for article in article_list:
            info = article.xpath('./a/text()').extract_first().strip().split(' ')
            print(info)
            item = DaomuItem()
            # 卷名
            item['juan_name'] = info[0]
            # 章节数
            item['zh_num'] = info[1]
            # 章节名
            if len(info) < 3:
                item['zh_name'] = ' '
            else:
                item['zh_name'] = info[2]
            # 章节链接
            item['link'] = article.xpath('./a/@href').get()
            print(item['juan_name'], item['zh_num'], item['zh_name'], item['link'])

            yield scrapy.Request(
                url=item['link'],
                callback=self.parse_three_link,
                # meta再不同函数之间传递一些参数，meta->调度器->下载器->
                # 作为response一个属性传递给下一个解析函数
                meta={'item': item}
            )

    # 解析三级页面
    def parse_three_link(self, response):
        item = response.meta['item']
        note_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        # note_list:['段落1','段落2','段落3',...]
        item['content'] = '\n'.join(note_list)

        # 交给管道(一定要把所有的数据获取完成后再yield item)
        yield item
