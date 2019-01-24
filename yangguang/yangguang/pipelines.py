# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from pymongo import MongoClient

client = MongoClient()
collection = client["yangguang"]["yg"]


class YangguangPipeline(object):
    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        print(item)
        collection.insert_one(dict(item))  # 此时item不是字段，不能直接存入mongodb
        return item

    def process_content(self, content):  # 处理content字段的数据
        content = [re.sub("\xa0|\s", "", i) for i in content]  # 替换字符串中的\xa0,\s
        content = [i for i in content if len(i) > 0]  # 删除列表中的空字符串
        return content
