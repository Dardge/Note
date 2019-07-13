# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'], item['star'], item['time'])
        print('*' * 50)
        return item


import pymongo
from .settings import *


# 新建管道类，数据库存入mongodb
class MaoyanMongoPipeline(object):
    # 爬虫项目启动时执行，只执行一次
    def open_spider(self, spider):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def process_item(self, item, spider):
        d = {
            'name': item['name'],
            'star': item['star'],
            'time': item['time']
        }
        self.myset.insert_one(d)
        print(d)
        return item

    def close_spider(self, spider):
        print('我是colse_spider函数')


import pymysql


class MaoyanMysqlPipeline(object):
    def open_spider(self, spider):
        self.db = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PWD, MYSQL_DB, charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into movie_info (name,star,time) values (%s,%s,%s)'
        d = [item['name'], item['star'], item['time']]
        self.cursor.execute(sql, d)
        self.db.commit()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
