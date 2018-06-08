# -*- coding: utf-8 -*-
import scrapy
from ..items import TsItem
from scrapy.http import Request

class LessonSpider(scrapy.Spider):
    name = 'lesson'
    allowed_domains = ['hellobi.com']
    start_urls = ['http://hellobi.com/']

    def parse(self, response):
        item=TsItem()
        item["title"]=response.xpath("//ol[@class='breadcrumb']/li[@class='active']/text()").extract()
        item["link"]=response.xpath("//ul[@class='nav nav-tabs']/li[@class='active']/a/@href").extract()
        item["stu"]=response.xpath("//span[@class='course-view']/text()").extract()
        #将结果返回至pipeline中
        yield item
        for i in range(1,100):
            url="https://edu.hellobi.com/course/"+str(i)
            #循环爬取
            yield Request(url,callback=self.parse)
