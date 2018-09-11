# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'JD'
    #allowed_domains = ['www.jd.com']
    start_urls = ['https://item.jd.com/2600240.html']

    def parse(self, response):
        with open ('demo.txt', 'wb') as f:
            for JDInfo in response.xpath('.//dl'):
            keyList = JDInfo.css('.//dt').extract()
            valList = JDInfo.css('.//dd').extract()
            f.write(keyList[i] + ' ' + valList[i] + '\n')
