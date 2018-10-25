# -*- coding: UTF-8 -*-

import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import json, re
import logging
import xlrd
from crawlcomments.items import JDCommentItem

logger = logging.getLogger(__name__)


class ProxyMiddleware():
    def __init__(self, proxy_url):
        self.logger = logging.getLogger(__name__)
        self.proxy_url = proxy_url

    def get_random_proxy(self):
        try:
            response = requests.get(self.proxy_url)
            if response.status_code == 200:
                proxy = response.text
                return proxy
        except requests.ConnectionError:
            return False

    def process_request(self, request, spider):
        if request.meta.get('retry_times'):
            proxy = self.get_random_proxy()
            if proxy:
                uri = 'https://{proxy}'.format(proxy=proxy)
                self.logger.debug('使用代理 ' + proxy)
                request.meta['proxy'] = uri

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(
            proxy_url=settings.get('PROXY_URL')
        )


class JD_Spider(scrapy.Spider):
    name = "jd-comment"
    start_urls = []

    # 根据要爬取的产品的sku和评论页标生成起始页
    # start_urls.append(
    #     "https://sclub.jd.com/comment/productPageComments.action?productId=28210193795&score=0&sortType=5&page=0&pageSize=10")

    xlrd.Book.encoding = "utf-8"
    data = xlrd.open_workbook("info.xlsx")
    # goods为要抓取评论的商品信息，现提供一个goods.xls文件供参考,第1列：商品ID；第2列：商品评论数；第3列：商品的commentVersion
    # test.xlsx也可以使用
    table = data.sheets()[0]
    nrows = table.nrows  # 行数
    ncols = table.ncols  # 列数
    sku = table.col_values(0)  # 商品ID
    comment_n = table.col_values(1)  # 商品评论数
    # comment_V = table.col_values(2)  # 商品评论的commentVersion
    for i in range(len(sku)):  # 一件商品一件商品的抽取
        good_num = int(sku[i])
        comment_total = int(comment_n[i])
        if comment_total % 10 == 0:  # 算出评论的页数，一页10条评论
            page = comment_total // 10
        else:
            page = comment_total // 10 + 1
        if comment_total > 0:
            for k in range(0, page):
                url = "https://sclub.jd.com/comment/productPageComments.action?productId=" + str(good_num) + "&score=0&sortType=5&isShadowSku=0&fold=1&pageSize=10&page=" + str(k)
                start_urls.append(url)

    # logger.debug(start_urls)

    def parse(self, response):
        temp = response.body.decode("gbk").encode("utf-8")
        js = json.loads(temp, encoding="utf-8")
        comments = js['comments']  # 该页所有评论
        items = []
        for comment in comments:
            item = JDCommentItem()
            item['user_name'] = comment['nickname']
            item['user_ID'] = comment['id']
            item['userProvince'] = comment['userProvince']
            item['content'] = comment['content']
            item['good_ID'] = comment['referenceId']
            item['good_name'] = comment['referenceName']
            item['date'] = comment['referenceTime']
            item['replyCount'] = comment['replyCount']
            item['score'] = comment['score']
            item['status'] = comment['status']
            title = ""
            item['title'] = title
            # item['userRegisterTime'] = comment['userRegisterTime']
            item['productColor'] = comment['productColor']
            item['productSize'] = comment['productSize']
            item['userLevelName'] = comment['userLevelName']
            item['isMobile'] = comment['isMobile']
            item['days'] = comment['days']
            yield item
            # items.append(item)
        # return items
