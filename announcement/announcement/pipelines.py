# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class AnnouncementPipeline(object):
    def process_item(self, item, spider):

        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.ann_title_set = set()

    def process_item(self, item, spider):
        title = item['title']
        if title in self.ann_title_set:
            raise DropItem("Duplicate announcement found: %s" % item)
        self.ann_title_set.add(title)
        return item
