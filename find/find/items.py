# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


class FindItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GameItem(scrapy.Item):
    title = scrapy.Field()
    language = scrapy.Field()
    type = scrapy.Field()
    form = scrapy.Field()
    sellingtime = scrapy.Field()
    updatetime = scrapy.Field()
    img = scrapy.Field()