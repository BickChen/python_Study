import scrapy


class MatchinfocrawlingSpider(scrapy.Spider):
    name = 'matchinfocrawling'
    #allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.vpgame.com/schedule']

    def parse(self, response):
        print(response.text)
