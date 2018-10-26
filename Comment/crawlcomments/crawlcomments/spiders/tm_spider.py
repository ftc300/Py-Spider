# -*- coding: UTF-8 -*-

import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import json, re
import logging
import xlrd
from crawlcomments.items import TMCommentItem

logger = logging.getLogger(__name__)


class TM_Spider(scrapy.Spider):
    name = "tm-comment"
    start_urls = []

    # 根据要爬取的产品的sku和评论页标生成起始页
    # start_urls.append(
    #     "https://sclub.jd.com/comment/productPageComments.action?productId=28210193795&score=0&sortType=5&page=0&pageSize=10")

    xlrd.Book.encoding = "utf-8"
    data = xlrd.open_workbook("info.xlsx")
    table = data.sheets()[1]
    ncols = table.ncols  # 列数
    itemids = table.col_values(1)
    sellerids= table.col_values(0)
    for i in range(len(itemids)):
        itemid = int(itemids[i])
        sellerid = int(sellerids[i])
        url = "https://rate.tmall.com/list_detail_rate.htm?ItemId={}&sellerId={}&currentPage=1".format(itemid,sellerid)
        start_urls.append(url)

    # logger.debug(start_urls)


    def parse(self, response):
        temp = response.body
        temp = temp[1][:-2]
        # temp = temp.encode('gbk').decode('unicode_escape')
        js = json.loads(temp, encoding="utf-8")
        comments = js['rateDetail']['rateList'] # 该页所有评论
        items = []
        for comment in comments:
            item = TMCommentItem()
            item["auctionPicUrl"] = comment["auctionPicUrl"]
            item["userInfo"] = comment["userInfo"]
            item["displayRatePic"] = comment["displayRatePic"]
            item["dsr"] = comment["dsr"]
            item["displayRateSum"] = comment["displayRateSum"]
            item["appendComment"] = comment["appendComment"]
            item["fromMemory"] = comment["fromMemory"]
            item["picsSmall"] = comment["picsSmall"]
            item["tmallSweetPic"] = comment["tmallSweetPic"]
            item["rateDate"] = comment["rateDate"]
            item["rateContent"] = comment["rateContent"]
            item["fromMall"] = comment["fromMall"]
            item["userIdEncryption"] = comment["userIdEncryption"]
            item["sellerId"] = comment["sellerId"]
            item["displayUserLink"] = comment["displayUserLink"]
            item["id"] = comment["id"]
            item["aliMallSeller"] = comment["aliMallSeller"]
            item["reply"] = comment["reply"]
            item["pics"] = comment["pics"]
            item["buyCount"] = comment["buyCount"]
            item["userVipLevel"] = comment["userVipLevel"]
            item["auctionSku"] = comment["auctionSku"]
            item["anony"] = comment["anony"]
            item["displayUserNumId"] = comment["displayUserNumId"]
            item["goldUser"] = comment["goldUser"]
            item["attributesMap"] = comment["attributesMap"]
            item["headExtraPic"] = comment["headExtraPic"]
            item["aucNumId"] = comment["aucNumId"]
            item["displayUserNick"] = comment["displayUserNick"]
            item["carServiceLocation"] = comment["carServiceLocation"]
            item["userVipPic"] = comment["userVipPic"]
            item["serviceRateContent"] = comment["serviceRateContent"]
            item["memberIcon"] = comment["memberIcon"]
            item["attributes"] = comment["attributes"]
            item["position"] = comment["position"]
            item["cmsSource"] = comment["cmsSource"]
            item["tamllSweetLevel"] = comment["tamllSweetLevel"]
            item["useful"] = comment["useful"]
            item["displayUserRateLink"] = comment["displayUserRateLink"]
            yield item
        currentpage = js['rateDetail']['paginator']['page']
        lastpage = js['rateDetail']['paginator']['lastPage']

        if int(currentpage) < int(lastpage):
            yield scrapy.Request(response.request.url[:-1]+ str(int(currentpage)+1), callback=self.parse)
