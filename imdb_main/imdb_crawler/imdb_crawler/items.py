# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImdbCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    release_year = scrapy.Field() 
    viewer_rating = scrapy.Field()
    runtime = scrapy.Field()
    genre = scrapy.Field()
    stars = scrapy.Field()
    # pass
