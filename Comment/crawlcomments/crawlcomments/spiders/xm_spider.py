# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import json, re
import logging
import xlrd
from crawlcomments.items import XMCommentItem

logger = logging.getLogger(__name__)


class XiaomiCommentSpider(scrapy.Spider):
    name = 'xiaomi-comment'

    def start_requests(self):
        comment_total = 2394
        reqs = []
        # if comment_total % 20 == 0:  # 算出评论的页数，一页20条评论
        #     page = comment_total // 20
        # else:
        #     page = comment_total // 20 + 1
        # for k in range(1, page):
        #     url = "https://comment.huodong.mi.com/comment/entry/getList?goods_id=8625&v_pid=&orderby=1&showimg=0&profile_id=0&jsonpcallback=jQuery111301510225871124462_1540446534217&_=1540446534221&pagesize=20&pageindex=" + str(
        #         k)
        #     headers = {
        #         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        #         "Referer": url
        #     }
        #     reqs.append(Request(url, headers=headers))
        # return reqs
        url = "https://comment.huodong.mi.com/comment/entry/getList?goods_id=8625&v_pid=&orderby=1&showimg=0&profile_id=0&jsonpcallback=jQuery111301510225871124462_1540446534217&_=1540446534221&pagesize=20&pageindex=" + str(
            1)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
            "Referer": url
        }
        return [Request(url, headers=headers)]


    def parse(self, response):
        temp = str(response.body).split('jQuery111301510225871124462_1540446534217(')
        temp1 = temp[1][:-1]
        print(unicode(temp1, "utf-8"))
    # js = json.loads(temp, encoding="utf-8")
    # js = json.loads(temp, encoding="utf-8")
    # print(js)
    # comments = js['data']['comments']  # 该页所有评论
    # items = []
    # for comment in comments:
    #     item = XMCommentItem()
    #     item['comment_id'] = comment['comment_id']
    #     item['user_id'] = comment['user_id']
    #     item['user_name'] = comment['user_name']
    #     item['user_avatar'] = comment['user_avatar']
    #     item['comment_content'] = comment['comment_content']
    #     item['comment_grade'] = comment['comment_grade']
    #     item['add_time'] = comment['add_time']
    #     item['add_timestamp'] = comment['add_timestamp']
    #     item['up_num'] = comment['up_num']
    #     item['down_num'] = comment['down_num']
    #     item['reply_content'] = comment['reply_content']
    #     item['reply_up_num'] = comment['reply_up_num']
    #     item['reply_time'] = comment['reply_time']
    #     item['comment_labels'] = comment['comment_labels']
    #     item['comment_title'] = comment['comment_title']
    #     item['user_reply_num'] = comment['user_reply_num']
    #     item['is_top'] = comment['is_top']
    #     item['up_rate'] = comment['up_rate']
    #     item['average_grade'] = comment['average_grade']
    #     item['total_grade'] = comment['total_grade']
    #     item['spec_value'] = comment['spec_value']
    #     item['site_id'] = comment['site_id']
    #     item['comment_images'] = comment['comment_images']
    #     item['comment_videos'] = comment['comment_videos']
    #     item['marks'] = comment['marks']
    #     item['tags'] = comment['tags']
    #     yield item
