# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AddressItems(scrapy.Item):
    my_url = scrapy.Field()
    listing_title = scrapy.Field()
    date = scrapy.Field()
    price = scrapy.Field()
    address = scrapy.Field()
    bathroom = scrapy.Field()
    for_rent_from = scrapy.Field()
    furnished = scrapy.Field()
    pets = scrapy.Field()
    visits = scrapy.Field()
    description = scrapy.Field()
    deleted = scrapy.Field()
class UrlItems(scrapy.Item):
    url_scraped = scrapy.Field()
    url_input = scrapy.Field()
