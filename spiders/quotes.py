import scrapy
from scrapy.spiders import CrawlSpider, Rule
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
           'https://store.playstation.com/en-gb/grid/STORE-MSF75508-GAMEGENREROLEPLA/1?gameContentType=games&platform=psp',
           'https://store.playstation.com/en-gb/grid/STORE-MSF75508-GAMEGENREROLEPLA/2?gameContentType=games&platform=psp'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        games_list = []
        games = response.xpath('//div[@class="grid-cell__body"]')
        next_page = response.xpath('.//a')
        print(next_page)
        
        for num in range(0, int(len(games))):
            game = {
                'title': games.xpath('//div[@class="grid-cell__title"]//text()')[num].extract(),
                'url': 'https://store.playstation.com/' + games.xpath('a/@href')[num].extract(),
            }
            games_list.append(game)


        
        filename = 'rpg-games.html'
        with open(filename, 'w') as f:
            for game in games_list:
                f.write(str(game['title']))
                f.write("\n")
                f.write(str(game['url']))
                f.write("\n")
                f.write("\n")