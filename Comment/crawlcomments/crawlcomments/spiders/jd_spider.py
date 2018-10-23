# -*- coding: UTF-8 -*-

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import json ,re


class JD_Spider(BaseSpider):

    name = "jd" # spider name
    start_urls = ["https://search.jd.com/Search?keyword=%E7%B1%B3%E5%AE%B6%E7%9F%B3%E8%8B%B1%E8%A1%A8&enc=utf-8&wq=%E7%B1%B3%E5%AE%B6%E7%9F%B3%E8%8B%B1%E8%A1%A8&pvid=012763e879184188855071437f87656a"] # start url 要采集的网页地址
