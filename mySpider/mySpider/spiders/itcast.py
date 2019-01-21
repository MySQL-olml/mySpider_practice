# -*- coding: utf-8 -*-
from pprint import pprint

import scrapy

#自定义spider类,继承scrapy.spider
class ItcastSpider(scrapy.Spider):
    name = "itcast" #爬虫名
    #允许爬取的范围，放置爬虫爬到别的网站
    allowed_domains = ["itcast.cn"]
    #开始爬取的url地址
    start_urls = [
        'http://www.itcast.cn/channel/teacher.shtml',
    ]

    #数据提取的方法，接受下载中间件传过来的response
    def parse(self, response):
        #scrap的response对象可以直接进行xpath
        ret = response.xpath("//div[@class='li_txt']//h3/text()").extract()
        #分组
        ret_list = response.xpath("//div[@class='li_txt']")

        for ret in ret_list:
            #创建一个数据字典
            item  = {}
            #利用scrapy封装好的xpath选择器定位元素，并通过extract()或者extract_first()获取数据
            item['name'] = ret.xpath('.//h3/text()').extract_first()
            item['level'] = ret.xpath('.//h4/text()').extract_first()
            item['introduce'] = ret.xpath('.//p/text()').extract_first()

            # pprint(item)

            yield item



