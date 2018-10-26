# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
from crawlcomments.items import JDCommentItem
from crawlcomments.items import XMCommentItem
from crawlcomments.items import TMCommentItem


# class CrawlcommentsPipeline(object):
#     def process_item(self, item, spider):
#         return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db, mongo_jd_collection,mongo_xm_collection,mongo_tm_collection):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_jd_collection = mongo_jd_collection
        self.mongo_xm_collection = mongo_xm_collection
        self.mongo_tm_collection = mongo_tm_collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
            mongo_jd_collection=crawler.settings.get('MONGO_JD_COLLECTION'),
            mongo_xm_collection=crawler.settings.get('MONGO_XM_COLLECTION'),
            mongo_tm_collection=crawler.settings.get('MONGO_TM_COLLECTION'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
        self.post_jd = self.db[self.mongo_jd_collection]
        self.post_xm = self.db[self.mongo_xm_collection]
        self.post_tm = self.db[self.mongo_tm_collection]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, JDCommentItem):
            data = dict(item)
            self.post_jd.insert(data)
        if isinstance(item, XMCommentItem):
            data = dict(item)
            self.post_xm.insert(data)
        if isinstance(item, TMCommentItem):
            data = dict(item)
            self.post_tm.insert(data)
        # if isinstance(item, UserItem) or isinstance(item, WeiboItem):
        #     self.db[item.collection].update({'id': item.get('id')}, {'$set': item}, True)
        # if isinstance(item, UserRelationItem):
        #     self.db[item.collection].update(
        #         {'id': item.get('id')},
        #         {'$addToSet':
        #             {
        #                 'follows': {'$each': item['follows']},
        #                 'fans': {'$each': item['fans']}
        #             }
        #         }, True)
        return item
