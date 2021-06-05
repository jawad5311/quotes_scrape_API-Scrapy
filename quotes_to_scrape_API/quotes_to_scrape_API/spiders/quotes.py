import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        resp = json.loads(response.body)
        quotes = resp.get('quotes')
        for quote in quotes:
            yield {
                'author': quote['author']['name'],
                'tags': quote['tags'],
                'quote': quote['text']
            }

        has_next = resp.get('has_next')
        if has_next:
            next_page = resp.get('page') + 1
            yield scrapy.Request(
                url=f"https://quotes.toscrape.com/api/quotes?page={next_page}",
                callback=self.parse
            )
