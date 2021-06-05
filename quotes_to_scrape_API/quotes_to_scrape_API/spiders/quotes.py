
"""
    Scrape Quotes from an API request using Scrapy

        - Scraped data from ```https://quotes.toscrape.com/scroll```.
        - Scraping all the available quotes on site.
        - Storing them into DataBase using PipeLines.
"""

import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes'  # Crawler Name
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['https://quotes.toscrape.com/api/quotes?page=1']

    def parse(self, response):
        resp = json.loads(response.body)  # Converts the recieved JSON data into py dict
        quotes = resp.get('quotes')  # Grabs all the quotes data
        for quote in quotes:
            # Go through the each quote and scrape the required data using dict keys
            yield {
                'author': quote['author']['name'],
                'tags': quote['tags'],
                'quote': quote['text']
            }

        has_next = resp.get('has_next')  # Checks if the next page available or not
        if has_next:
            next_page = resp.get('page') + 1  # Holds the current page and adds 1 to it
            yield scrapy.Request(
                url=f"https://quotes.toscrape.com/api/quotes?page={next_page}",
                callback=self.parse
            )
