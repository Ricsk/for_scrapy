# -*- coding: utf-8 -*-
import scrapy
import os
import re
from selenium import webdriver


class MoocSpider(scrapy.Spider):
    name = 'mooc'
    allowed_domains = ['mail.163.com']
    start_urls = ['http://mail.163.com/']
    count = 0
    def parse(self, response):
        #with open("163.txt", 'wb') as f:
            #f.write(response.body)
        divv = response.xpath('.//div[@class = "headerNav"]')
        href = divv.xpath('.//a[@href]/@href')
        for ans in href:
            url = ans.extract()
            #with open('url.txt', 'a') as f:
                #f.write(url + '\n')
            #yield scrapy.Request(url=url, callback=self.parse2)
            request = scrapy.Request(url=url, callback=self.parse2)
            request.meta['PhantomJS'] = True
            yield request

    def parse2(self, response):
        self.count += 1
        #with open('./nojs/' + str(self.count) + '.txt', 'wb') as f:
            #f.write(response.body)
        with open('./js/' + str(self.count) + '.txt', 'wb') as f:
            f.write(response.body)