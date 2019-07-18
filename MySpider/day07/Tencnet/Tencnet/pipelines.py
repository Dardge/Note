# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo, pymysql
from .settings import *


class TencnetPipeline(object):
    def process_item(self, item, spider):
        print(item['job_title'])
        return item


# class TencentMongoPipeline(object):
#
#     def open_spider(self, spider):
#         self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
#         self.db = self.conn[MONGO_DB]
#         self.myset = self.db[MONGO_SET]
#
#     def process_item(self, item, spider):
#         d = {
#             'job_title': item['job_title'],
#             'job_duty': item['job_duty'],
#             'job_requirement': item['job_requirement']
#         }
#         self.myset.insert_one(d)
#
#     def close_spider(self, spider):
#         print('-----------')
