# -*- coding: utf-8 -*-

import scrapy

class HousePicture(scrapy.Item):
    file_urls = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    my_nice_file_name = scrapy.Field()
   
class ImageScraperItem(scrapy.Item):
    pass
