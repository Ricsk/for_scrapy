# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LearnXpathPipeline(object):
    def process_item(self, item, spider):
        return item


class LearnXpathPipelineINFO(object):

    def __init__(self):
        self.file = open('out.txt', 'w')

    def spider_closed(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.file.write(line)
        except:
            pass
        return item
'''
class  LearnXpathPipelineinfor_pip(object):
    def __init__(self):
        self.file = open('info_out.txt', 'w')

    def spider_closed(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.file.write(line)
        except:
            pass
        return item
'''