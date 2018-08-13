from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# 'followall' is the name of one of the spiders of the project.
process.crawl('shfe', domain='www.shfe.com.cn')
process.start() # the script will block here until the crawling is finished
# process.join()
process1 = CrawlerProcess(get_project_settings())
process1.crawl('cffex', domain='www.shfe.com.cn')
process1.start()
# process.join()
# process = CrawlerProcess(get_project_settings())
# process.crawl('dce', domain='www.shfe.com.cn')
# process.start()
# process.join()