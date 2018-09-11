# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import scrapy
import time


class Mooc4SpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class Mooc4DownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

class PhantomJSMiddleware(object):

    def process_request(cls, request, spider):
        c1 = {
            'name':'STUDY_INFO',
            'value':'"g586268@163.com|-1|1136111566|1527246786180"',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c2 = {
            'name': 'NTES_PASSPORT',
            'value': 'g3TAjYXZbnZUzM2aUQ4ElRTVHdJt.1NteokquAroTryqjKoGNj5ophTDmTbzXv4R6EEooNctaP8V_XgfsoFK1rS1w89aBE.Y1cVAau.Aom.DCkfsc2dwigogTsFzKwiphnE4_E2W1rhab6x9rEvCDq4XXWKr7Rlwk',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c3 = {
            'name': 'NTESSTUDYSI',
            'value': '0f2e1e8b2aa344a8a7828bef042689fe',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c4 = {
            'name': 'NTES_SESS',
            'value': '8.1GSh1kmb.WTRZkSPnmHbIpxEemtJ2d7te_AHnvblHrE_XDPEyXqNBWi835oe3gZ75BsvxkD9WvnM3cReHW9WaJNwm399WhVFjntDl.MfQfqFZi3ktPMYvex9wdCn0rwkVMoNP2SczDp61BVQd0YZYozB.ZWP7cqsmXoStsUVag6bn2b88sikFum',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c5 = {
            'name': 'P_INFO',
            'value': 'g586268@163.com|1527246786|1|imooc|00&99|zhj&1526899889&imooc#zhj&330100#10#0#0|&0|cloudmusic&imooc|g586268@163.com',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c6 = {
            'name': 'STUDY_PERSIST',
            'value': '"ev43caKG4G2DJjFGf3tUGQuuTVBNJbARQJqjcsneb2SryOPMnf4Cck+cTjyNV4XlYZDBg+SrsDnBjTayu/4+lkpiy0siJV9JVuCj3OD6L1gNPLeq0EebVsgFtW9Zny8dWa4O/lRUHndSsL6IMEIFVc8MhgBy6n325joucUWNTNHkGpLaMS98V8c2PWuDit1fbBgMKYutm2mclBf+1iCcuqerrzfin1SwA7cBFulC07YtbbMCuQrcAiDbfyn/qhOQ8WQLi3xTJ45sq/acjsEWiA=="',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c7 = {
            'name': 'STUDY_SESS',
            'value': '"0HQzjmh0ZCr3FiQbjV0UqqpofI/F2SJ2jrS+EHPWwP10LL+BGGYnikLekJNz1zaHotnUYCTim4oAfWHuINXQ1FzHv0gKJhOns5GJDLbuPCY19N5UlLbZmvM8Y9ubPxt8fa/S0/WSMZC7TKcS1Cioit03PmL2UVwi49J5Xeb6B2CAB324xXcBe7qOJTRrr0/A"',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c8 = {
            'name': 'S_INFO',
            'value': '1527246786|0|3&20##|g586268',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        c9 = {
            'name': 'NETEASE_WDA_UID',
            'value': '1136111566#|#1519893318339',
            'domain': '.icourse163.org',
            'path': '/',
            'httponly': True,
            'secure': False
        }
        if 'PhantomJS' in request.meta:
            driver = webdriver.PhantomJS()
            driver.customHeaders ={
                'Host': 'www.icourse163.org',
                'Referer': 'https://www.icourse163.org/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            }
            driver.get(request.url)
            #driver.deleteCookie('EDUWEBDEVICE')
            #driver.deleteCookie('NTESSTUDYSI')
            driver.add_cookie(c1)
            #logging.info("1")
            driver.add_cookie(c2)
            driver.add_cookie(c3)
            driver.add_cookie(c4)
            driver.add_cookie(c5)
            driver.add_cookie(c6)
            driver.add_cookie(c7)
            driver.add_cookie(c8)
            driver.add_cookie(c9)
            #time.sleep(3)
            driver.refresh()
            time.sleep(30)
            driver.implicitly_wait(2)
            content = driver.page_source.encode('utf-8')
            #driver.quit()
            return scrapy.http.HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
        else:
            driver = webdriver.PhantomJS()
            driver.customHeaders = {
                'Host': 'www.icourse163.org',
                'Referer': 'https://www.icourse163.org/',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            }
            driver.get(request.url)
            time.sleep(10)
            driver.implicitly_wait(2)
            content = driver.page_source.encode('utf-8')
            return scrapy.http.HtmlResponse(request.url, encoding='utf-8', body=content, request=request)
