# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        print(item['star'])
        print(item['time'])
        print('*'*50)
        return item

import pymongo
from .settings import *

# 新建管道类,数据存入mongodb
class MaoyanMongoPipeline(object):
    # 爬虫项目启动时执行,只执行一次
    def open_spider(self,spider):
        print('我是open_spider函数')
        self.conn = pymongo.MongoClient(
            MONGO_HOST,MONGO_PORT
        )
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self,item,spider):
        d = {
            '电影名称':item['name'],
            '电影主演':item['star'],
            '上映时间':item['time']
        }
        self.myset.insert_one(d)
        return item

    # 爬虫项目结束时执行一次
    def close_spider(self,spider):
        print('我是close_spider函数')

import pymysql
# 新建mysql管道类
class MaoyanMysqlPipeline(object):
    def open_spider(self,spider):
        pass

    def process_item(self,item,spider):
        return item

    def close_spider(self,spider):
        pass







