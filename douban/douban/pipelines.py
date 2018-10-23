# -*- coding: utf-8 -*-
import pymongo
import scrapy

from douban.settings import MONGO_DB_COLLECTION, MONGO_DB_NAME, MONGO_HOST, MONGO_PORT
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        host = MONGO_HOST
        port = MONGO_PORT
        db_name = MONGO_DB_NAME
        db_collection = MONGO_DB_COLLECTION
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[db_name]
        self.post = mydb[db_collection]
        pass

    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item

class DoubanItemImg(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)


    def get_media_requests(self, item, info):
            yield scrapy.Request(item['img_url'])

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
