# -*- coding: utf-8 -*-
import scrapy
from scrapy.http.cookies import CookieJar
from scrapy.http import Request,FormRequest

class MailSpider(scrapy.Spider):
    name = 'mail'
    #allowed_domains = ['mail.163.com']
    #start_urls = ['https://mail.163.com/']
    cookie_jar = CookieJar()
    def start_requests(self):
        urls = ['https://dl.reg.163.com/webzj/m163_2/pub/index_dl.html?wdaId=&pkid=CvViHzl&product=mail163'
                ,'https://dl.reg.163.com/getConf?callback=URSJSONP1524651825971&pkid=CvViHzl&pd=mail163&mode=1'
                ,'https://dl.reg.163.com/ini?pd=mail163&pkid=CvViHzl&pkht=mail.163.com&topURL=https%3A%2F%2Fmail.163.com%2F&nocache=1524651826394'
                ]
        for url in urls:
            yield scrapy.Request(url = url, meta={'cookiejar':1}, callback=self.parse)

    def parse(self, response):
        if response.url == 'https://dl.reg.163.com/ini?pd=mail163&pkid=CvViHzl&pkht=mail.163.com&topURL=https%3A%2F%2Fmail.163.com%2F&nocache=1524651826394':
            yield scrapy.Request(url = 'https://mail.163.com/', meta={'cookiejar':1}, callback = self.parse2)

    def parse2(self, response):
        pass
