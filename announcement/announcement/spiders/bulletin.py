# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.linkextractors import LinkExtractor
from ..items import AnnouncementItem
class BulletinSpider(scrapy.Spider):
    name = 'bulletin'
    allowed_domains = ['www.shfe.com.cn']
    start_urls = ['http://www.shfe.com.cn/news/notice/']
    # http://www.shfe.com.cn/news/notice/911330699.html url which contains img
    def parse(self, response):
        # le = LinkExtractor(restrict_css='div.lawbox ul')
        le = LinkExtractor(restrict_css='div.lawbox>ul')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_announcement)

        # 提取"下一页"的链接
        # links = LinkExtractor(restrict_xpaths='//div[@class="page-no"]/a[text()="下页>"]')
        # if links:
        #     next_url = links[0].url
        #     yield scrapy.Request(next_url, callback=self.parse)

    def parse_announcement(self, response):
        ann_item = AnnouncementItem()
        detail_text = response.css('div.article-detail-text')
        text_list = detail_text.xpath('//p/text()').extract()
        text_list = list(map(lambda x: x.strip(), text_list))
        text_list = list(filter(lambda x: x, text_list))
        body_text = '\n'.join(text_list)
        pub_id = detail_text.css('p:nth-child(3)::text').extract_first()
        ann_item['pub_id'] = pub_id
        pub_date = detail_text.xpath('//p[@class="article-date"]/text()').extract_first()
        ann_item['pub_date'] = pub_date
        ann_item['exchange'] = 'SHFE'
        ann_item['body_text'] = body_text
        title = detail_text.xpath('./h1/text()').extract_first()
        ann_item['title'] = title
        today = datetime.datetime.now()
        today_str = today.strftime('%Y%m%d')
        ann_item['update_time'] = today_str
        yield ann_item
