# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GuokrSpider(CrawlSpider):
    name = 'guokr'
    allowed_domains = ['guokr,com']
    start_urls = ['https://www.guokr.com/ask/highlight']

    rules = (
        # 提取列表页的url地址
        Rule(LinkExtractor(allow=r'/ask/highlight/\?page=\d+'), follow=True),
        # 提取详情页的url地址
        Rule(LinkExtractor(allow=r'question/\d+/'), callback='parse_item'),
    )

    def parse_item(self, response):

        item = {}

        item["title"] = response.xpath("//h1[@id='articleTitle']/text()").extract_first()
        item["desc"] = response.xpath("//div[@id='questionDesc']/p/text()").extract_first()
        item["href"] = response.url

        print(item)
