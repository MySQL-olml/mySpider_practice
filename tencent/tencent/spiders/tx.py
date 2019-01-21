# -*- coding: utf-8 -*-
from pprint import pprint
import urllib.parse
import scrapy


class TxSpider(scrapy.Spider):
    name = "tx"
    allowed_domains = ["hr.tencent.com"]
    start_urls = [
        'https://hr.tencent.com/position.php?&start=0#a',
    ]

    def parse(self, response):
        #1.提取当前页面数据
            #先分组再获取
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        #遍历tr列表获取响应数据
        for tr in tr_list:
            item = {}
            item['position'] = tr.xpath("./td[1]/a/text()").extract_first()
            item['position_href'] = tr.xpath("./td[1]/a/@href").extract_first()
            item['position_sort'] = tr.xpath("./td[2]/text()").extract_first()
            item['num'] = tr.xpath("./td[3]/text()").extract_first()
            item['city'] = tr.xpath("./td[4]/text()").extract_first()
            item['date'] = tr.xpath("./td[5]/text()").extract_first()

            yield item

            # 翻页，请求下一页数据
            next_url = response.xpath("//a[@id='next']/@href").extract_first()

            # 判断是否是最后一页
            if next_url != "javascript:;":
                # 根据response的url地址，对next_url进行url地址的拼接，构造请求
                print(response.url)
                yield response.follow(next_url, callback=self.parse)
