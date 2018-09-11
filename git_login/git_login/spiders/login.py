# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.http import Request, FormRequest, HtmlResponse


class LoginSpider(scrapy.Spider):

    name = 'login'
    start_urls = [
        'https://github.com',
    ]
    #allowed_domains = ['github.com/login']
    post_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Referer": "https://github.com/",
    }
    def start_requests(self):
        start_urls = ['https://github.com/login/']
        for url in start_urls:
            yield scrapy.Request(url = url, meta={'cookiejar':1}, callback = self.post_login)

    def post_login(self, response):
        authenticity_token = response.xpath('.//input[@name = "authenticity_token"]/@value').extract()[0]
        logging.info('authenticity_token='+authenticity_token)
        login = 'Ricsk'
        password = 'supportornot777'
        yield scrapy.FormRequest.from_response(response,
                                      url='https://github.com/session',
                                      meta={'cookiejar': response.meta['cookiejar'],'login':login},
                                      headers=self.post_headers,  # 注意此处的headers
                                      formdata={
                                          'utf8': '✓',
                                          'login': login,
                                          'password': password,
                                          'authenticity_token': authenticity_token
                                      },
                                      callback=self.after_login,
                                      dont_click=True
                                      )

    def after_login(self, response):
        for url in self.start_urls:
            yield Request(url=url + '/' + response.meta['login'], meta={'cookiejar': response.meta['cookiejar']},callback=self.parse)

    def parse(self, response):
        print(response.url)
        ans = response.xpath('.//div[@class = "mt-4"]')
        ans = ans.xpath('.//li')
        for a in ans:
            s = a.xpath('.//a[@class = "text-bold"]/@href').extract()
            if len(s) != 0:
                print(s)