# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from zhihu_user.mongoData import MongoData

class ZhihuUserPipeline(object):

    mdb = MongoData()

    def process_item(self, item, spider):
        if item is not None:
            self.mdb.insertData(dict(item))
        return item
