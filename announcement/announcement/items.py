# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnnouncementItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pub_date = scrapy.Field()
    exchange = scrapy.Field()
    pub_id = scrapy.Field()
    body_text = scrapy.Field()
    update_time = scrapy.Field()
    url = scrapy.Field()

