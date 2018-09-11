# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SumLearn1Pipeline(object):
    def process_item(self, item, spider):
        return item


class my_Pipline(object):

    #def __init__(self):
    def open_spider(self, spider):
        self.file = open('out_ans.txt', 'w')

    def close_spider(self, spider):
        self.file.close()
        print('ok')

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.file.write(line)
        except:
            pass
        return item