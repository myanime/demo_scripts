# -*- coding: utf-8 -*-
from canadascraper.items import AddressItems
from canadascraper.items import UrlItems
import scrapy
import traceback

class FastScraper(scrapy.Spider):
    name = "fast_scrape"
    start_urls = [line.rstrip('\n') for line in open('./canadascraper/spiders/url')]
    def parse(self, response):
        arrayurl_scraped = response.css("div.title a.title").xpath("@href").extract()
        for x in range (0, len(arrayurl_scraped)):
            url_scraped = arrayurl_scraped[x]
            yield UrlItems(url_scraped=url_scraped)
        
class RoomScraper(scrapy.Spider):
    name = "room_scraper"
    start_urls = [line.rstrip('\n') for line in open('/home/myanime/canadaSraper/canadascraper/canadascraper/spiders/room')]
    def parse(self, response):
        my_url = None
        listing_title =None
        date = None
        price = None
        address = None
        bathroom = None
        for_rent_from = None
        furnished = None
        pets = None
        visits = None
        description = None
        deleted = None

        try:
            my_url = str(response.url)
            listing_title = response.xpath("//span[@itemprop='name']").css("h1::text").extract_first()
            price = response.xpath("//span[@itemprop='price']").css("strong::text").extract_first()
            description = response.xpath("//table/tbody/tr[1]/td").css("::text").extract()
            attributes = response.css("table.ad-attributes tr").css("::text").extract()
            date = attributes[3]
            address = attributes[13]
            
            furnished = attributes[25]
            pets = attributes[30]
            
        except:
            print traceback.print_exc()
            deleted = "Posting Deleted"

        yield AddressItems(deleted=deleted, my_url=my_url, date=date, listing_title=listing_title, price=price, address=address, bathroom=bathroom, for_rent_from=for_rent_from, furnished=furnished, pets=pets, visits=visits, description=description)

class CondoScraper(scrapy.Spider):
    name = "condo_scraper"
    start_urls = [line.rstrip('\n') for line in open('/home/myanime/canadaSraper/canadascraper/canadascraper/spiders/condo')]
    def parse(self, response):
        my_url = None
        listing_title =None
        date = None
        price = None
        address = None
        bathroom = None
        for_rent_from = None
        furnished = None
        pets = None
        visits = None
        description = None
        deleted = None

        try:
            my_url = str(response.url)
            listing_title = response.xpath("//span[@itemprop='name']").css("h1::text").extract_first()
            price = response.xpath("//span[@itemprop='price']").css("strong::text").extract_first()
            description = response.xpath("//table/tbody/tr[1]/td").css("::text").extract()            

            attributes = response.css("table.ad-attributes tr").css("::text").extract()
            for x in range (0, len(attributes)):
                attributes[x] = attributes[x].strip()

            date = attributes[3]
            address = attributes[13]
            cut_attributes = attributes[22:len(attributes)]
            bathroom = cut_attributes
            
        except:
            deleted = "Posting Deleted"
            traceback.print_exc()
        yield AddressItems(deleted=deleted, \
                   my_url=my_url, \
                   date=date, \
                   listing_title=listing_title, \
                   price=price, address=address, \
                   bathroom=bathroom,\
                   description=description)

class HouseScraper(scrapy.Spider):
    name = "house_scraper"
    start_urls = [line.rstrip('\n') for line in open('/home/myanime/canadaSraper/canadascraper/canadascraper/spiders/house')]
    def parse(self, response):
        my_url = None
        listing_title =None
        date = None
        price = None
        address = None
        bathroom = None
        for_rent_from = None
        furnished = None
        pets = None
        visits = None
        description = None
        deleted = None

        try:
            my_url = str(response.url)
            listing_title = response.xpath("//span[@itemprop='name']").css("h1::text").extract_first()
            price = response.xpath("//span[@itemprop='price']").css("strong::text").extract_first()
            description = response.xpath("//table/tbody/tr[1]/td").css("::text").extract()

            attributes = response.css("table.ad-attributes tr").css("::text").extract()
            for x in range (0, len(attributes)):
                attributes[x] = attributes[x].strip()

            date = attributes[3]
            address = attributes[13]
            cut_attributes = attributes[22:len(attributes)]
            bathroom = cut_attributes
            
        except:
            deleted = "Posting Deleted"
            traceback.print_exc()

        yield AddressItems(deleted=deleted, \
                           my_url=my_url, \
                           date=date, \
                           listing_title=listing_title, \
                           price=price, address=address, \
                           bathroom=bathroom,\
                           description=description)

