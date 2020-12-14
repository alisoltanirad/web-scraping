# Data Source: https://brickset.com/
# Dependencies: ScrPy
import requests
import scrapy


class BricksetSpider(scrapy.Spider):
    name = 'brickset_spider'
    start_urls = ['https://brickset.com/sets/year-2020']

    def parse(self, response):
        for item in response.css('.set'):
            yield {
                'Name': item.css('h1 :: text').extract_first(),
            }
