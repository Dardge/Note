# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencnetItem(scrapy.Item):
    # define the fields for your item here like:
    job_title = scrapy.Field()
    job_duty = scrapy.Field()
    job_requirement = scrapy.Field()
