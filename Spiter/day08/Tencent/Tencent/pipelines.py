# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from .settings import *

class TencentPipeline(object):
    def process_item(self, item, spider):
        return item


class TencentMongoPipeline(object):
    def open_spider(self,spider):
        conn = pymongo.MongoClient(
            MONGO_HOST,
            MONGO_PORT
        )
        db = conn[MONGO_DB]
        self.myset = db[MONGO_SET]

    def process_item(self,item,spider):
        self.myset.insert_one(dict(item))
        return item











