# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class SQLlitePipeline:
    def open_spider(self, spider):
        self.connection = sqlite3.Connection("quotes_API.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute("""
                CREATE TABLE quotes_scrapped_using_api(
                    author TEXT,
                    tags LIST,
                    quote TEXT
                    )    
            """)
            self.connection.commit()
        except sqlite3.OperationalError:
            pass

    def process_item(self, item, spider):
        self.c.execute("""
                    INSERT INTO quotes_scrapped_using_api (author,tags,quote) VALUES(?,?,?)
                """, (
            item.get('author'),
            str(item.get('tags')),
            item.get('quote')
        ))
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()
