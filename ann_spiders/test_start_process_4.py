import scrapy
from scrapy.crawler import CrawlerRunner
# from scrapy.utils import defer
from scrapy.utils.project import get_project_settings
from ann_spiders.spiders.cffex import CffexSpider
from ann_spiders.spiders.shfe import BulletinSpider
from ann_spiders.spiders.dce import DceSpider
from twisted.internet import defer, reactor

settings = get_project_settings()
runner = CrawlerRunner(settings)

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CffexSpider)
    yield runner.crawl(BulletinSpider)
    yield runner.crawl(DceSpider)
    reactor.stop()

crawl()
reactor.run()