# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re
import os
from for_AJ.items import ForAjItem
import random


class DemoSpider(scrapy.Spider):
    name = 'Demo'
    #allowed_domains = ['nike.com/cn/zh_cn']
    start_urls = ['https://www.nike.com/cn/launch/?s=upcoming']
    #start_urls = ['https://www.nike.com/cn/launch/t/air-presto-mid-utility-acronym-racer-pink-black-photo-blue/']
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" 
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    #def parse(self, response):
        #with open('out_test.txt', 'wb') as f:
           # f.write(response.body)
       # print(response.url)

    def start_requests(self):
        ua = random.choice(self.user_agent_list)
        headers = {
            'Connection': 'keep-alive',
            'User-Agent': ua
        }
        for url in self.start_urls:
            yield SplashRequest(url=url, headers = headers, meta = {'cookiejar':1}, callback = self.parse)

    def parse(self, response):
        upcoming = response.xpath('.//div[@class="product-card ncss-row mr0-sm ml0-sm"]')
        for upcome in upcoming.extract():
            #取下级url
            ls_url = re.findall(r'href=.*?\/\"', upcome)[0].replace(u'\xa0', u' ').split('\"')[1]
            #取鞋名
            ls_name = ls_url.split('/')[-2]
            #取日期
            ls_date = re.findall(r'test-startDate">.*<',upcome)[0].replace(u'\xa0', u' ').split('>')[1].split('<')[0]
            path='./'+ls_date+'/'+ls_name
            flag = os.path.exists(path)
            if not flag:
                os.makedirs(path)
            #print(response.url[:29])
            ua = random.choice(self.user_agent_list)
            headers = {
                'Connection': 'keep-alive',
                'User-Agent': ua
            }
            print('2')
            yield SplashRequest(url = response.url[:30]+'/t/'+ls_name+'/', meta = {'datee': ls_date, 'lsname':ls_name,
                                'cookiejar':response.meta['cookiejar']}, headers = headers,
                                 callback = self.parse2)

    def parse2(self, response):
        print('1')
        datee = response.meta['datee']
        ls_name = response.meta['lsname']
        imageurl = []
        item = ForAjItem()
        item['title'] = './' +datee + '/' + ls_name
        print(response.url)
        with open('./'+datee + '/'+ ls_name+ '/'+ 'source.txt', 'wb') as f:
            f.write(response.body)

        #image_urls = response.xpath('.//figure')

