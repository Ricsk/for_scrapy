# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LearnXpathItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()

    # val = scrapy.Field()

'''' 
class LearnXpathItem(scrapy.Item):
    name = scrapy.Field()
    #openstock = scrapy.Field()#开盘
    done_num = scrapy.Field()#成交量
    hight = scrapy.Field()#最高
    to_the_best = scrapy.Field()#涨停
    take_out = scrapy.Field()#内盘
    done_money = scrapy.Field()#成交额
    rate1 = scrapy.Field()#委比（要买入的量和要卖出的量的比）
    sum = scrapy.Field()#流通市值
    pe = scrapy.Field()
    e = scrapy.Field()#每股收益
    sum_num = scrapy.Field()#总股本
    yesdone = scrapy.Field()#昨收
    change_rate = scrapy.Field()#还手率
    blow = scrapy.Field()#最低
    to_the_worst = scrapy.Field()#跌停
    take_in = scrapy.Field()#外盘
    roll_rate = scrapy.Field()#振幅
    rate2 = scrapy.Field()#量比
    sum_money = scrapy.Field()#总市值
    pb = scrapy.Field()
    pr_p = scrapy.Field()#每股净资产
    loll_sum = scrapy.Field()#流通股本
    '''
