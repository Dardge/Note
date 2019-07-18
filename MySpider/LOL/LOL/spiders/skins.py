# -*- coding: utf-8 -*-
import scrapy, re, json
from ..items import *


class SkinsSpider(scrapy.Spider):
    name = 'skins'
    allowed_domains = ['lol.qq.com']
    start_urls = ['https://lol.qq.com/biz/hero/champion.js']  # 可写多个url返回的response给parse方法

    def parse(self, response):
        r = '"keys":(.*?),"data"'
        hero_id_dict = eval(re.findall(r, response.text)[0])  # 将类字典字符串转换为字典
        for hero_id in hero_id_dict.values():
            hreo_js = 'https://lol.qq.com/biz/hero/{}.js'.format(hero_id)
            yield scrapy.Request(url=hreo_js, callback=self.parse_hero_skin_id)

    # 解析某一个英雄的js文件，获取该英雄名字、该英雄所有皮肤的id及皮肤名字
    def parse_hero_skin_id(self, response):
        r = '"skins":(.*?),"info"'
        hero_skin_id_list = re.findall(r, response.text)[0]  # 存放英雄皮肤信息的列表
        hero_name = re.findall('"data":.*?"name":(.*?),', response.text)[0]  # 英雄名字
        # print(json.loads(hero_name))
        # print(hero_skin_id_list)
        r2 = '"id":"(.*?)".*?"name":(.*?),'
        id_and_skinname_list = re.findall(r2, hero_skin_id_list)  # 英雄皮肤id、皮肤名字的列表
        # print(id_list)
        for it in id_and_skinname_list:
            # item = LolItem()
            # print(item,item[0],item[1])
            skin_id = it[0]
            if it[1] == '"default"':
                skin_name = json.loads(hero_name)
                # item['skin_name'] = json.loads(hero_name)
            elif '/' in json.loads(it[1]):
                skin_name = json.loads(it[1]).replace('/', '')
                # item['skin_name'] = json.loads(it[1]).replace('/', '')
            else:
                skin_name = json.loads(it[1])
                # item['skin_name'] = json.loads(it[1])
            # print(skin_name)
            img_url = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg'.format(skin_id)
            # item['img_url'] = 'http://ossweb-img.qq.com/images/lol/web201310/skin/big{}.jpg'.format(skin_id)
            yield scrapy.Request(url=img_url, callback=self.save_images, meta={'name': skin_name}, dont_filter=True)
            # yield item

    def save_images(self, response):
        filename = response.meta['name'] + '.jpg'
        image = response.body  # 将将请求到图片解码为二进制
        with open('E:\LOLimages\{}'.format(filename), 'wb') as f:
            f.write(image)
        print('{}下载完成'.format(filename))
