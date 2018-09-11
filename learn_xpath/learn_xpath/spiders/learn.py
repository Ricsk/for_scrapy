# -*- coding: utf-8 -*-
import scrapy
import re
import random
from learn_xpath.items import LearnXpathItem
class LearnSpider(scrapy.Spider):

    name = 'learn'
    start_urls = ['http://quote.eastmoney.com/stocklist.html']
    user_agent_list = [ \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]

    def __init__(self):
        self.count = 0
        self.cc = 0

    def parse(self, response):
        #with open('out_test3.txt', 'w') as f:
            #f.write(str(response.body))
        for href in response.xpath('.//a/@href'):
            stock = href.extract()
            ua = random.choice(self.user_agent_list)  # 随机抽取User-Agent
            #with open('out_test2.txt', 'a') as f:
                #f.write(str(stock))
            #too = re.findall(r'[s][hz]\d{6}', stock)[0]

            try:
                too = re.findall(r"[s][hz]\d{6}", stock)[0]
                url = 'https://gupiao.baidu.com/stock/' + too + '.html'
                #print(url)
                #with open('out_test4.txt', 'a') as f:
                    #f.write(str(url) + '\n')
                #print(1)

                #print(url)
                headers = {
                    'Accept-Encoding': 'gzip, deflate, sdch, br',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Connection': 'keep-alive',
                    'Referer': 'https://gupiao.baidu.com/',
                    'User-Agent': ua
                }  # 构造请求头
                #self.cc+=1
                #with open('s_out.txt', 'a') as f:
                   # f.write(str(self.cc) + ' ' + str(ua) + '\n')
                yield scrapy.Request(url, callback=self.parse_s, headers=headers)
            except:
                continue

    def parse_s(self,response):
        #with open('out_test.txt', 'a') as f:
            #f.write(str(response.body))
        #items = LearnXpathItem2()
        stoo = response.css('.stock-bets')
        div = stoo.xpath('.//div[@class = "bets-content"]')
        keyList = div.xpath('.//dt').extract()
        valueList = div.xpath('.//dd').extract()
        info = {}
        iinfos = LearnXpathItem()
        for i in range(len(keyList)):
            key = re.findall(r'>.*</dt>', keyList[i])[0][1:-5]
            try:
                val = re.findall(r'>\d+\.?.*</dd>', valueList[i])[0][1:-5]
            except:#保证有值
                val = '--'
            #info[key] = val
        self.count += 1
        #try:
        nam = stoo.css('.bets-name').extract()[0]
            #print(nam)
        #except:
            #with open('c_out2.txt', "a") as f:
               # f.write(str(self.count) + '\n')
        #print(nam)
        #info.update({'href' : re.findall(r'href=".*"', nam)[0][6:-1]})
        info.update({'name' : re.findall(r'\s.*\(', nam)[0][13:-1]})
        iinfos['name'] = info['name']
        #print(iinfos['name'])
        #infos['openstock'] = info['今开']#为什么写不进去
        #with open('out_test.txt', 'w') as f:
            #f.write(str(ans))
        yield iinfos
    '''
    start_urls = ['http://quote.eastmoney.com/stocklist.html']
    '''
    '''保存所有的股票名称以及股票代码（使用items）
    def start_requests(self):
        urls = ["http://quote.eastmoney.com/stocklist.html"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for stock in response.xpath('.//a[@href]'):
            item = LearnXpathItem()
            tt = stock.extract()
            #item.append(tt)
            try:
                val = re.findall(r'[s][hz]\d{6}', tt)[0]
            except:
                continue
            try:
                key = re.findall(r'>.*<', tt)[0][1:-1]
            except:
                continue
            item['name'] = key
            item['val'] = val
            yield item
        with open('out_test.txt', 'w') as f:
            for i in range(len(item)):
                f.write(str(item[i]) + '\n')
        妄图获取所有a标签的内容
        item = []
        for stock in response.xpath('.//a/text()'):
            item.append(stock.extract())
        with open('out_test.txt', 'w') as f:
            for i in range(len(item)):
                f.write(str(item[i]) + '\n')
        找到所有a标签的href并且存到list中
        item = []
        for stock in response.xpath('.//a/@href'):
            url = stock.extract()
            try:
                use = re.findall(r'[s][sh]\d{6}', url)[0]
                item.append(use)
            except:
                continue
        with open('out_test.txt', 'w') as f:
            for i in range(len(item)):
                f.write(str(item[i]) + '\n')
        提取所有a标签的href
        for stock in response.xpath('.//a/href')
            item.append(stock.extract())
        with open('out_test.txt', 'w') as f:
            for i in range(len(item)):
                f.write(str(item[i]) + '\n')
            将所有a标签保存在list输出
        for stock in response.xpath('.//a'):
            item.append(stock.extract())
        with  open("out_test2.txt", "w") as f:
            for i in range(len(item)):
                f.write(str(item[i]) + '\n')
        '''
    #直接输出所有内容
               # f.write(response.body)
        #输出所有a标签
                #for stock in response.xpath('.//a'):#提取出selectorlist
                    #for css in stock.extract():提取信息
                        #f.write(str(css) + '\n')
                    #f.write(str(stock.extract()) + '\n')
            #self.log('Saved file %s.' % "out_test.txt")
'''
        直接寻找股票代码并输出
            try:
                url = re.findall(r'[s][hz]\d{6}', stock)[0]
                item.append(url)
            except:
                continue;
        with open("out.txt", "w") as f:
            for i in range(len(item)):
                f.write(str(item[i]))
'''
