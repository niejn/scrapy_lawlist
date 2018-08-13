from scrapy.utils.project import get_project_settings
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from ann_spiders.spiders.cffex import CffexSpider
from ann_spiders.spiders.shfe import BulletinSpider


configure_logging()
settings = get_project_settings()
runner = CrawlerRunner(settings)
# runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(CffexSpider)
    yield runner.crawl(BulletinSpider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished