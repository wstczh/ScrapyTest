# -*- coding: utf-8 -*-
import scrapy
from pyquery import PyQuery
from ..items import City58Item
from scrapy.http import Request

class City58TestSpider(scrapy.Spider):
    name = 'city58_test'
    allowed_domains = ['58.com']
    start_urls = ['http://hz.58.com/chuzu/']

    def parse(self, response):
        jpy=PyQuery(response.text)
        #copy selector,一定要记得带上items()
        li_list=jpy('body > div.mainbox > div.main > div.content > div.listBox > ul > li').items()
        #遍历每个li标签
        for it in li_list:
            a_tag=it('div.des > h2 > a')
            item= City58Item()
            item['name']=a_tag.text()
            item['url']=a_tag.attr('href')
            item['price']=it(' div.listliright > div.money > b').text()
            yield item #把Item返回给引擎
