# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class TaoSpider(scrapy.Spider):
    name = 'tao'
    #allowed_domains = ['www.taobao.com']
    def start_requests(self):
        start_urls = [
            'https://s.taobao.com/search?q=%E6%98%BE%E7%A4%BA%E5%B1%8F%E5%8F%AF%E6%97%8B%E8%BD%AC&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180411&ie=utf8']
        for url in start_urls:
            yield SplashRequest(url=url, callback = self.parse, args = {'wait':1}, endpoint='render.html')
    def parse(self, response):
        title = response.xpath('.//div[@class="row row-2 title"]/a/text()').extract()
        print('结果如下：', title)
