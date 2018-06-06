# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Chengdu58Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    last_update=scrapy.Field()

class Chengdu58ItemXiaoQu(scrapy.Item):
    id=scrapy.Field()
    name=scrapy.Field()
    reference_price=scrapy.Field()
    address=scrapy.Field()
    times=scrapy.Field()

class Chengdu58ItemXiaoQuChuZu(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    zu_price = scrapy.Field()
    type = scrapy.Field()
    mianji = scrapy.Field()
    chuzu_price_pre = scrapy.Field()
    url = scrapy.Field()
    price_pre = scrapy.Field()