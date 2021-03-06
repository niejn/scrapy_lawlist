from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# class MySpider1(scrapy.Spider):
#     # Your first spider definition
#     ...
#
# class MySpider2(scrapy.Spider):
#     # Your second spider definition
from ann_spiders.spiders.cffex import CffexSpider

...

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CffexSpider)
    # yield runner.crawl(MySpider2)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished