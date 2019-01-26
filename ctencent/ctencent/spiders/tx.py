# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TxSpider(CrawlSpider):
    name = 'tx'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        #提取列表页的url地址 ？需要使用\进行转义否则获取不到
        Rule(LinkExtractor(allow=r'position.php\?&start=\d+#a'),follow=True),
        #提取详情页的url地址
        Rule(LinkExtractor(allow=r'position_detail.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),

    )

    def parse_item(self, response):
        item = {}
        #提取标题
        item["title"] = response.xpath("//td[@id='sharetitle']/text()").extract_first()
        #提取工作职责
        item["duty"] = response.xpath("//div[text()='工作职责：']/following-sibling::ul[1]/li/text()").extract()
        #提取工作要求
        item["require"] = response.xpath("//div[text()='工作要求：']/following-sibling::ul[1]/li/text()").extract()

        print(item)
