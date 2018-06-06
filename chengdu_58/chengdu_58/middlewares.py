# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
from scrapy import log
import time

class ProxyMiddleware(object):
    def process_request(self,request,spider):
        #http://0.0.0.0:3030
        # request.meta['proxy']='http://115.229.55.76:9000'
        proxy=self.get_random_proxy()
        print("this is request ip "+proxy)
        request.meta['proxy']=proxy

    def process_response(self, request, response, spider):  # 对response进行拦截
        if response.status!=200:
            proxy=self.get_random_proxy()
            print("this is response ip "+proxy)
            #对当前request加上代理
            request.meta['proxy']=proxy
        return response

    def process_exception(self, request, exception, spider):
        pass

    def get_random_proxy(self):
        #随即从文件中读取proxy
        while 1:
            with open('D:\\python learning\\ScrapyTest\\chengdu_58\\chengdu_58\\ip.txt','r') as f:
                proxies=f.readlines()
            if proxies:
                break
            else:
                time.sleep(1)
        proxy=random.choice(proxies).strip()
        return proxy

# ua_list = [
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
#     "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
#     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
#     "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
#     "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
#     "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
#     "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
#     "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
#     "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
#     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
#     "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
#     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
#     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
# ]
#
#
# def process_request(self, request, spider):  # 对request进行拦截
#     ua = random.choices(self.ua_list)  # 使用random模块，随机在ua_list中选取User-Agent
#     request.headers['User-Agent'] = ua  # 把选取出来的User-Agent赋给request
#     print(request.url)  # 打印出request的url
#     print(request.headers['User-Agent'])  # 打印出request的headers
#
#
# def process_response(self, request, response, spider):  # 对response进行拦截
#     return response
#
#
# def process_exception(self, request, exception, spider):
#     pass

    # user_agent_list = [
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    #     "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    #     "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    #     "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    #     "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    #     "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    #     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    #     "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    #     "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    #     "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    #     "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    #     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    #     "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
    #     "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    #     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
    #     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    #     "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
    #     "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    # ]
    #
    #
    # def process_request(self, request, spider):
    #     ua = random.choice(self.user_agent_list)
    #     if ua:
    #     # 显示当前使用的useragent
    #         print("********Current UserAgent:%s************" % ua)
    #         # 记录
    #         log.msg('Current UserAgent: ' + ua)
    #         request.headers.setdefault('User-Agent', ua)