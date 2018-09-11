# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import re

class MoocSpider(scrapy.Spider):
    name = 'mooc'
    #allowed_domains = ['www.icourse163.org']
    #start_urls = ['http://www.icourse163.org/']
    cookie={'NTES_SESS': '8mChGvDJAWQsM3_gWRbsWxN6bq1MSNmUGIQLrjYivSDDE_XDPEyXqNBWi835oe3gZ75BsvxkD9WUGPvGVWlkrgThQyV0P.b1PMl6q4D2GHYMVoD0zcI_VFfPYAMbgy_ufup3SY3ZtB4W3A78w4KAJLtz.te1nv8UbO5tTXe4BgirHM6kF59P6plum', 'EDUWEBDEVICE': '65dfa27ef3264e8696996b960d5378c9', '__utmz': '63145271.1524485244.14.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic', 'S_INFO': '1526299994|0|3&20##|g586268', 'STUDY_PERSIST': '"ev43caKG4G2DJjFGf3tUGQuuTVBNJbARQJqjcsneb2SryOPMnf4Cck+cTjyNV4XlYZDBg+SrsDnBjTayu/4+liTZr1RhqKWQmEkN1mpfOr09U8E/lP+tNMnSUe8CNT1Cf7YNu45ytXKevZvyCfm8m8izJUNbML9oB0UhwizEuJW5m0GIxpmpaPqo9OfR3fT8R2G/xA5nSbCndOP9z/08iaerrzfin1SwA7cBFulC07YtbbMCuQrcAiDbfyn/qhOQ8WQLi3xTJ45sq/acjsEWiA=="', 'eduplayer_device_id': '15202299125635257204409', 'utm': '"eyJjIjoiIiwiY3QiOiIiLCJpIjoiIiwibSI6IiIsInMiOiIiLCJ0IjoiIn0=|aHR0cHM6Ly93d3cuaWNvdXJzZTE2My5vcmcvaG9tZS5odG0/dXNlcklkPTExMzYxMTE1NjY="', 'P_INFO': 'g586268@163.com|1526299994|1|imooc|00&99|zhj&1526296222&imooc#zhj&330100#10#0#0|&0|imooc|g586268@163.com', 'STUDY_SESS': '"0HQzjmh0ZCr3FiQbjV0UqqpofI/F2SJ2jrS+EHPWwP10LL+BGGYnikLekJNz1zaH3dRb5sY5Uz1LTU/o8kxnhlzHv0gKJhOns5GJDLbuPCaywH36bFr+Y88nny9AhGmYtLs5yEygynq123rVZ5ADrt03PmL2UVwi49J5Xeb6B2CAB324xXcBe7qOJTRrr0/A"', 'videoResolutionType': '3', '__utma': '63145271.1191946113.1520229867.1526293958.1526296226.24', 'mp_MA-A976-948FFA05E931_hubble': '%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fwww.icourse163.org%2Fpassport%2Flogingate%2FchangeCookie.htm%3Ftype%3Durs%26returnUrl%3DaHR0cHM6Ly93d3cuaWNvdXJzZTE2My5vcmcvaG9tZS5odG0_dXNlcklkPTExMzYxMTE1NjY.%26edusave%3D1%26loginWay%3D0%22%2C%22updatedTime%22%3A%201526299994621%2C%22sessionStartTime%22%3A%201526298392551%2C%22deviceUdid%22%3A%20%22112cf5da-9771-4d35-a03e-2e30aae8ef53%22%2C%22persistedTime%22%3A%201524813488735%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22cd6c5afc4df46db5560b952ac0771704438e71cc%22%2C%22time%22%3A%201526299994621%7D%2C%22sessionUuid%22%3A%20%226fad9f8b-4425-4a7e-8191-6a34cb4d0922%22%7D', 'STUDY_INFO': '"g586268@163.com|-1|1136111566|1526299994565"', '__utmb': '63145271.20.8.1526299994606', '__utmc': '63145271', 'NTES_PASSPORT': 'dWrW2XEuFgbCaXJ.BlrxWOtp3dd75hGBzK9COLXoa_ZGqimB3qtmALlQ5lnRxZ2WTMMmm3hOb.PXT5JY9dbMjTwcDULMqxmP8mSED8OxLqilPYPgex5uyLOgPrQjOm7zeqKwNNk6_U7Kd.ENzIR.MXCfXOIfzRE6a', 'NTESSTUDYSI': '65ace97f8a09419594c6246f69d82eb4'}
    headers = {
        'Host': 'www.icourse163.org',
        'Referer': 'https://www.icourse163.org/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

    def start_requests(self):
        urls = ['https://www.icourse163.org/home.htm?userId=1136111566#/home/course']
        for url in urls:
            yield SplashRequest(url=url, cookies = self.cookie, headers=self.headers, callback=self.parse, args={'wait': 10})

    def parse(self, response):
        with open ('user_crouse.txt', 'wb') as f:
            f.write(response.body)
        #ans = response.xpath('.//div[@class="home-content"]')
        #with open('ans.txt', 'wb') as f:
            #f.write(ans.extract()[0].encode("GBK", 'ignore'))
