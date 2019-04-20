import scrapy
from scrapy.spiders import CrawlSpider, Rule
import json

class RpgSpider(scrapy.Spider):
    name = "rpgs"

    start_urls = ['https://store.playstation.com/en-gb/grid/STORE-MSF75508-GAMEGENREROLEPLA/1?gameContentType=games&platform=psp']

    def parse(self, response):
        games = response.xpath('//div[@class="grid-cell__body"]')
        
        for num in range(0, int(len(games))):
            game = {
                'title': games.xpath('//span[@title]//text()')[num].extract(),
                'url': 'https://store.playstation.com' + games.xpath('a/@href')[num].extract(),
                'image': games.xpath('//div[@class="product-image__img product-image__img--main"]')[num].xpath('img')[0].extract()
            }
            yield game
        
        pages = response.xpath('//a/@href').extract()
        page_links = []
        
        for page in pages:
            if '&platform=psp' in page and page not in  self.start_urls[0]:
                page_links.append(page)

        page_links = list(set(page_links))

        for page in page_links:
            page = 'https://store.playstation.com' + page
            next_page = response.urljoin(page)
            yield scrapy.Request(next_page, callback=self.parse)