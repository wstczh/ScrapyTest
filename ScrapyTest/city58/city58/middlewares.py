# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import scrapy.downloadermiddlewares.retry

class UAMiddleware(object):
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 ',
        '(KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    ]

    def process_request(self,request,spider):#对request进行拦截
        ua=random.choices(self.ua_list)  #使用random模块，随机在ua_list中选取User-Agent
        request.headers['User-Agent']=ua #把选取出来的User-Agent赋给request
        print(request.url)      #打印出request的url
        print(request.headers['User-Agent']) #打印出request的headers

    def process_response(self,request,response):#对response进行拦截
        return response

    def process_exception(self,request,exception,spider):
        pass