# -*- coding: utf-8 -*-
import scrapy
import os
import re
from selenium import webdriver

class MoocSpider(scrapy.Spider):
    name = 'mooc'
    #allowed_domains = ['www.icourse163.org']
    #start_urls = ['http://www.icourse163.org/']
    def start_requests(self):
        urls = ['https://www.icourse163.org/home.htm?userId=1136111566#/home/course']
        for url in urls:
            request = scrapy.Request(url=url,callback=self.parse)
            request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        #with open('out.txt', 'wb') as f:
            #f.write(response.body)
        hrefs = response.xpath('//a[@href]/@href')
        for href in hrefs:
            url = href.extract()
            try:
                ans = re.findall(r'/.*\?tid.*', url)[0]
                ans = 'https://www.icourse163.org'+ans + '#/learn/content'
                request = scrapy.Request(url=ans, callback=self.parse2)
                yield request
            except:
                continue

    def parse2(self, response):

        with open('./out_url.txt', 'a') as f:
            f.write(response.url + '\n')
        filename = response.url
        filename = re.findall('tid=.*#', filename)[0][:-1]
        with open('./learn/'+filename+'.txt', 'wb') as f:
            f.write(response.body)
