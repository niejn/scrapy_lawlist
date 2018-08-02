from scrapy import cmdline
# cmdline.execute("scrapy crawl cffex -o cffex.csv".split())
from sqlalchemy import create_engine

# _engine = create_engine('ann_spiders.sqlite', echo=True)
cmdline.execute("scrapy crawl cffex".split())