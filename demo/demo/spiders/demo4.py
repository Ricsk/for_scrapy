# -*- coding: utf-8 -*-
import scrapy


class Demo4Spider(scrapy.Spider):
    name = 'demo4'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        pass
