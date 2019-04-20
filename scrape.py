import scrapy
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy import signals

from spiders.rpgSpider import RpgSpider


records = []
class ItemPipeline(object):
	def process_item(self, item, spider):
		records.append(item)


def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'ITEM_PIPELINES': {
            '__main__.ItemPipeline': 1
        }
    })

    process.crawl(RpgSpider)
    process.start()

    from pprint import pprint
    pprint(records)
    1/0

if __name__ == "__main__":
    main()