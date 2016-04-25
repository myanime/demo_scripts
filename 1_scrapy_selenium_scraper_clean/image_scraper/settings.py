# -*- coding: utf-8 -*-

BOT_NAME = 'image_scraper'

SPIDER_MODULES = ['image_scraper.spiders']
NEWSPIDER_MODULE = 'image_scraper.spiders'

ITEM_PIPELINES = {'image_scraper.pipelines.RenamePipeline': 1}
IMAGES_STORE = './downloaded_pictures/'
