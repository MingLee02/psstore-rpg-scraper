import json

import scrapy
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy import signals

from spiders.rpgSpider import RpgSpider


records = []


class ItemPipeline(object):
    def open_spider(self, spider):
        self.file = open('games.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        records.append(item)
        line = json.dumps(item, indent=4, sort_keys=False)
        self.file.write(line)
        return item

def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'ITEM_PIPELINES': {
            '__main__.ItemPipeline': 1
        }
    })

    process.crawl(RpgSpider)
    process.start()


if __name__ == "__main__":
    main()