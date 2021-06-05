# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class SQLlitePipeline:
    def open_spider(self, spider):
        """ Creates a database before the spider runs """
        self.connection = sqlite3.Connection("quotes_API.db")  # Creates database
        self.c = self.connection.cursor()  # Creates cursor for the database
        try:  # Checks for the error
            self.c.execute("""
                CREATE TABLE quotes_scrapped_using_api(
                    author TEXT,
                    tags LIST,
                    quote TEXT
                    )    
            """)
            self.connection.commit()  # Commit the changes after the database is created
        except sqlite3.OperationalError:  # If database already created then throws OperationalError
            pass

    def process_item(self, item, spider):
        """ Adds the Scrapped data into database using cursor """
        self.c.execute("""
                    INSERT INTO quotes_scrapped_using_api (author,tags,quote) VALUES(?,?,?)
                """, (
            item.get('author'),  # Grabs author value
            str(item.get('tags')),  # Grabs tags list and convert whole list into string
            item.get('quote')  # Grabs the quote
        ))
        self.connection.commit()  # Commit the changes to the database

    def close_spider(self, spider):
        """ Closes the connection from the db after the crawling is completed """
        self.connection.close()  #
