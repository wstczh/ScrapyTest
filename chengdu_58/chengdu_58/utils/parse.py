from pyquery import PyQuery

def parse(response):
    """
    抓取小区列表页面：http://cd.58.com/xiaoqu/
    返回列表页所有的小区url
    :param response:
    :return:
    """
    jpy=PyQuery(response.text)
    tr_list=jpy('#infolist > div.listwrap > table > tbody>tr').items()
    result=set()#result为set集合
    for tr in tr_list:
        # infolist > div.listwrap > table > tbody > tr:nth-child(2) > td.info > ul > li.tli1 > a,前面一部分可以省略
        #attr['href]表示a中的链接元素
        url=tr('td.info > ul > li.tli1 > a').attr('herf')
        result.add(url)
    return result

def xiaoqu_parse(response):
    """
    小区详情页匹配代码样例url:http://cd.58.com/xiaoqu/shenxianshudayuan/
    返回这个小区的详细信息的dict字典，主要信息包括小区名称，小区参考房价，小区地址，小区建筑年代
    :param response:
    :return:
    """
    result=dict()
    jpy=PyQuery(response.text)
    result['name']=jpy('body > div.body-wrapper > div.title-bar > span.title').text()
    result['reference_price']=jpy('body > div.body-wrapper > div.basic-container > div.info-container '
                                  '> div.price-container > span.price').text()
    result['address']=jpy('tr:nth-child(1) > td:nth-child(4)').text()
    #'times': ['70年', '58同城成都小区频道为您提供新的小区信息，包括小区的二手房、租房、小区均价和小区的周边信息等。
    # 欢迎使用58同城成都小区频道！手机版请点击', '桐梓林欧城小区']
    result['times']=jpy('tr:nth-child(4) > td:nth-child(2)').text().split()
    result['times']=result['times'][0]
    print(result)
    return result

def get_ershou_price_list(resopnse):
    """
    网页链接：http://cd.58.com/xiaoqu/shenxianshudayuan/ershoufang/
    匹配二手房列表页面的所有房价信息
    返回一个价格列表list
    :param resopnse:
    :return:
    """
    jpy=PyQuery(resopnse.text)
    ##infolist > div.listwrap > table > tbody > tr:nth-child(1) > td.tc > span:nth-child(3)这样不行
    price_tag=jpy('tr> td.tc > span:nth-child(3)').text().split()
    price_tag=[i[:3] for i in price_tag] #遍历price_tag截取到倒数第三个元素
    #price_tag=jpy('tr> td.tc > b').text()
    print(price_tag)
    return price_tag

def chuzu_list_pag_get_detail_url(response):
    """
    页面链接：http://cd.58.com/xiaoqu/shenxianshudayuan/chuzu/
    获取出租列表页所有详情页url
    返回url的列表list
    :param response:
    :return:
    """
    jpy=PyQuery(response.text)
    ##infolist > div.listwrap > table > tbody > tr:nth-child(1) > td.t > a.t这样子输出无结果
    a_list=jpy('tr> td.t > a.t').items()
    url_list=[a.attr('href') for a in a_list]
    print(url_list)
    return url_list

def get_chuzu_house_info(response):
    """
    获取出租详情页的相关信息：http://cd.58.com/zufang/34317530918600x.shtml
    返回一个dict包含：出租页标题，出租价格，房屋面积，房屋类型
    :param response:
    :return:
    """
    jpy=PyQuery(response.text)
    result=dict()
    result['name']=jpy('body > div.main-wrap > div.house-title > h1').text()
    result['zu_price']=jpy('body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-basic-desc > div.house-desc-item.fl.c_333 > div > span.c_ff552e > b').text()
    result['type']=jpy('body > div.main-wrap > div.house-basic-info > div.house-basic-right.fr > div.house-basic-desc > div.house-desc-item.fl.c_333 > ul > li:nth-child(2) > span:nth-child(2)').text()
    result['type'], result['mianji'], *_ = result['type'].split()
    print(result)
    return result

#当parse.py作为程序入口时调用
if __name__=='__main__':
    import requests
    # r=requests.get('http://cd.58.com/zufang/34317530918600x.shtml')
    # get_chuzu_house_info(r)
    # r=requests.get('http://cd.58.com/xiaoqu/shenxianshudayuan/chuzu/')
    # chuzu_list_pag_get_detail_url(r)
    # r=requests.get('http://cd.58.com/xiaoqu/shenxianshudayuan/ershoufang/')
    # get_ershou_price_list(r)
    r=requests.get('http://cd.58.com/xiaoqu/tongzilinoucheng/')
    xiaoqu_parse(r)