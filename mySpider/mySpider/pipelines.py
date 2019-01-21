# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        #管道专门处理数据的程序
        print(item)
        return item
