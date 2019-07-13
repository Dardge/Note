# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo, pymysql
from .settings import *


class TencnetPipeline(object):
    def process_item(self, item, spider):
        print(item)
        return item


class TencentMongoPipeline(object):
    def open_spider(self, spider):
        conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        db = conn[MONGO_DB]
        self.myset = db[MONGO_SET]

    def process_item(self, item, spider):
        print(item)
        print(dict(item))
        self.myset.insert_one(dict(item))
        return item

    def close_spider(self, spider):
        print('-----------')
