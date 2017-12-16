import scrapy
from scrapy.crawler import Crawler, CrawlerProcess
from scrapy import signals

from spiders.quotes import QuotesSpider

def main():
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(QuotesSpider)
    process.start()

if __name__ == "__main__":
    main()