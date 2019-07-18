# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DaomuPipeline(object):
    def process_item(self, item, spider):
        print(item['juan_name'])
        print('*' * 80)
        # 把小说内容保存到本地
        filename = '/code/小说/{}-{}-{}.txt'.format(item['juan_name'], item['zh_num'], item['zh_name'])
        with open(filename, 'w')as f:
            f.write(item['content'])
        return item
