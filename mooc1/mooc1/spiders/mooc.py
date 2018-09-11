# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule, Request
from scrapy.linkextractors import LinkExtractor
from scrapy import FormRequest
from scrapy_splash import SplashRequest

class MoocSpider(CrawlSpider):
    name = 'mooc'
    #allowed_domains = ['www.icourse163.org']
    #start_urls = ['http://www.icourse163.org/']
    cookie = {'utm': '"eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0', 'NTESSTUDYSI': '5f0dc518a66e41cca059af4f3bc5ee1b', 'mp_MA-A976-948FFA05E931_hubble': '%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fwww.icourse163.org%2F%22%2C%22updatedTime%22%3A%201525602596075%2C%22sessionStartTime%22%3A%201525602596066%2C%22deviceUdid%22%3A%20%22112cf5da-9771-4d35-a03e-2e30aae8ef53%22%2C%22persistedTime%22%3A%201524813488735%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201525602596075%7D%2C%22sessionUuid%22%3A%20%2276d45dd5-e37f-46a9-97ca-3bd9ca3ee913%22%7D', '__utmb': '63145271.2.9.1525602597', 'STUDY_INFO': '"g586268@163.com|-1|1136111566|1525602592215"', '__utmz': '63145271.1524485244.14.3.utmcsr', 'videoResolutionType': '3', 'NETEASE_WDA_UID': '1136111566#|#1519893318339', '__utma': '63145271.1191946113.1520229867.1525268418.1525602597.19', '__utmc': '63145271', 'eduplayer_device_id': '15202299125635257204409', 'STUDY_PERSIST': '"ev43caKG4G2DJjFGf3tUGQuuTVBNJbARQJqjcsneb2SryOPMnf4Cck+cTjyNV4XlYZDBg+SrsDnBjTayu/4+lhKqY8XppgY6cJgVLTM8PX+d/RX4mIivjU+98qFDkEEeSaGyDgOhwxQTE0Ve1RKA5vGvSLkZnsyt6YHk4fRrB6rqYPJAAV05fquXa2dWqZm4BGKdgOu+Yp9i73TosPPCJaerrzfin1SwA7cBFulC07YtbbMCuQrcAiDbfyn/qhOQ8WQLi3xTJ45sq/acjsEWiA', 'STUDY_SESS': '"0HQzjmh0ZCr3FiQbjV0UqqpofI/F2SJ2jrS+EHPWwP10LL+BGGYnikLekJNz1zaHmXzS9nRcKTZugMN1zJtTFlzHv0gKJhOns5GJDLbuPCaIwVp3z+2Yw50JPdlZEF0xAnPYAUgzBnyKb9p6pU+IcN03PmL2UVwi49J5Xeb6B2CAB324xXcBe7qOJTRrr0/A"', 'EDUWEBDEVICE': '65dfa27ef3264e8696996b960d5378c9', 'P_INFO': 'g586268@163.com|1524625063|1|imooc|00&99|zhj&1524485690&imooc#zhj&330100#10#0#0|&0|imooc|g586268@163.com'}
    headers = {
        'Connection': 'keep - alive',  # 保持链接状态
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        'Referer': 'https://www.icourse163.org/'
    }
    '''
    def start_requests(self):
        yield SplashRequest(url = 'https://www.icourse163.org/user/setting/personInfoEdit.htm#/setting', headers=self.headers, cookies=self.cookie, callback=self.parse)

    def parse(self, response):
        print(response.url)
        with open('user.txt', 'wb') as f:
            f.write(response.body)
    '''
    rules = (
        Rule(LinkExtractor(allow=(r'^https://www.icourse163.org.*')), callback='parses', follow = True),
    )

    def start_requests(self):
        yield scrapy.Request(url = 'http://www.icourse163.org/', headers=self.headers, cookies=self.cookie)

    def parses(self, response):
        file = response.url.split('/')[-1].split('.')[0]
        file = file + '.txt'
        with open('./web/' + file, 'wb') as f:
            f.write(response.body)
        if file == "personInfoEdit.txt":
            with open('ser2.txt', 'wb') as f:
                f.write(response.body)
            yield SplashRequest(url=response.url, headers=self.headers, cookies=self.cookie, callback=self.parsess)
    def parsess(self, response):
        with open('user2.txt', 'wb') as f:
            f.write(response.body)


