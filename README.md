# Quote Scrape from API using scrapy

## About Project
- Scraped data from ```https://quotes.toscrape.com/scroll```. 
- Scraping all the available quotes on site.
- Storing them into DataBase using PipeLines.

This page returns data as json object which needs to be collected using a different technique. 

## How it Works
- Request the first page
- Converts the returned json data python dictionary
- Yield the data from this created dict
- Checks for the next available page
- Creates URL for the next page and calls the parse method again
- Add data to database by Pipelines using SQLlite3
