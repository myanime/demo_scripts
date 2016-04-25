# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealtorItem(scrapy.Item):
    my_url = scrapy.Field()
    listing_title = scrapy.Field()
    #date = scrapy.Field()
    price = scrapy.Field()
    #address = scrapy.Field()
    #bathroom = scrapy.Field()
    #for_rent_from = scrapy.Field()
    #furnished = scrapy.Field()
    #pets = scrapy.Field()
    #visits = scrapy.Field()
    description = scrapy.Field()
    deleted = scrapy.Field()

    realtor_name=scrapy.Field()
    realtor_url=scrapy.Field()
    realtor_title=scrapy.Field()
    realtor_phone=scrapy.Field()
    listingID=scrapy.Field()
    number_bedrooms=scrapy.Field()
    number_bathrooms=scrapy.Field()
    community_name=scrapy.Field()
    land_size=scrapy.Field()
    number_of_stories=scrapy.Field()
    fax_number_broker=scrapy.Field()
    phone_number_broker=scrapy.Field()
    office_address_broker=scrapy.Field()
    office_designation_broker=scrapy.Field()
    office_name_broker=scrapy.Field()
                
    property_type = scrapy.Field()
    legal_title = scrapy.Field()
    built_in = scrapy.Field()
    parking = scrapy.Field()
    neighborhood = scrapy.Field()
    building_type = scrapy.Field()

    amenitiesnearby=scrapy.Field()
    farmtype=scrapy.Field()
    monthlymaintenancefees=scrapy.Field()
    parkingtype=scrapy.Field()
    pooltype=scrapy.Field()
    totalparkingspaces=scrapy.Field()
    zoningtype=scrapy.Field()


    partialbathrooms = scrapy.Field()
    totalbathrooms = scrapy.Field()
    cooling = scrapy.Field()
    exteriorfinish = scrapy.Field()
    fireplace = scrapy.Field()
    fireplacefuel = scrapy.Field()
    interiorfloorspace = scrapy.Field()
    heatingfuel = scrapy.Field()
    style = scrapy.Field()
    utilitysewer = scrapy.Field()
    utilitywater = scrapy.Field()
    pass
