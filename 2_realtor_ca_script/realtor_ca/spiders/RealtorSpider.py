import scrapy
from realtor_ca.items import RealtorItem
import time
import re
import traceback

import csv


class UrlScraper(scrapy.Spider):
    name = "url_scraper"

    #start_urls = ['https://www.realtor.ca/Residential/Single-Family/10780338/161-Ch-du-Cur%C3%A9-Deslauriers-279-Mont-Tremblant-Quebec-J8E1C9-Tremblant-Station']
    #start_urls = ['https://www.realtor.ca/Residential/Single-Family/16824737/29-PINE-AVE-S-Mississauga-Ontario-L5H2P9-Port-Credit']
    start_urls = []
    i=0
    csvReader = csv.reader(open('/home/myanime/realtor_ca/realtor_ca/spiders/all.csv', 'rb'), delimiter=' ', quotechar='|')
    for row in csvReader:
        start_urls.append(row[0])

    def parse(self, response):

        def nws(mystr):
            try:
                mystr = mystr.strip()
                mystr = re.sub(r'\s+', ' ', mystr)
                return mystr
            except:
                return None
        my_url = None
        listing_title =None
        price = None
        deleted = None

        #lblIndividualName
                
        property_type = None
        legal_title = None
        built_in = None
        parking = None
        neighborhood = None
        building_type = None

        date = None
        address = None
        bathroom = None
        for_rent_from = None
        furnished = None
        pets = None
        visits = None
        description = None
        

        try:
            my_url = str(response.url)
            listing_title = nws(response.css('div.m_property_dtl_address_lft h1#m_property_dtl_address::text').extract_first())
            price = nws(response.css('div#m_property_dtl_info_hdr_price::text').extract_first())

            realtor_title = nws(response.css('span#lblTitle::text').extract_first())
            realtor_name = nws(response.css('span#lblIndividualName::text').extract_first())
            realtor_url = nws(response.css('span#lblMediaLinks a').xpath("@href").extract_first())
            realtor_phone = nws(response.css('span#lblPhone_0::text').extract_first())
            listingID = nws(response.css('div.m_property_dtl_info_hdr_lft_listingid::text').extract_first())
            number_bedrooms = nws(response.css('span#m_property_dtl_beds::text').extract_first())
            number_bathrooms = nws(response.css('span#m_property_dtl_baths::text').extract_first())
            community_name = nws(response.css('span#communityname_value::text').extract_first())
            land_size = nws(response.css('span#landsize_value::text').extract_first())
            number_of_stories = nws(response.css('span#stories_value::text').extract_first())
            fax_number_broker = nws(response.css('span#lblOfficePhone_1::text').extract_first())
            phone_number_broker = nws(response.css('span#lblOfficePhone_0::text').extract_first())
            try:
                office_address_broker = nws(response.css('span#lblOfficeAddress::text')[0].extract())
                office_address_broker = office_address_broker + "," + nws(response.css('span#lblOfficeAddress::text')[1].extract())
            except:
                pass
            office_designation_broker = nws(response.css('span#lblOfficeDesignation::text').extract_first())
            office_name_broker= nws(response.css('span#lblOfficeName::text').extract_first())

            property_type = nws(response.css('span#propertytype_value::text').extract_first())
            legal_title = nws(response.css('span#title_value::text').extract_first())
            built_in = nws(response.css('span#builtin_value::text').extract_first())
            parking = nws(response.css('span#parkingtype_value::text').extract_first())
            neighborhood = nws(response.css('span#neighborhoodname_value::text').extract_first())
            building_type = nws(response.css('span#buildingtype_value::text').extract_first())

            partialbathrooms= nws(response.css('span#m_property_dtl_blddata_val_partialbathrooms::text').extract_first())
            totalbathrooms= nws(response.css('span#m_property_dtl_blddata_val_totalbathrooms::text').extract_first())
            cooling= nws(response.css('span#m_property_dtl_blddata_val_cooling::text').extract_first())
            exteriorfinish= nws(response.css('span#m_property_dtl_blddata_val_exteriorfinish::text').extract_first())
            fireplace= nws(response.css('span#m_property_dtl_blddata_val_fireplace::text').extract_first())
            fireplacefuel= nws(response.css('span#m_property_dtl_blddata_val_fireplacefuel::text').extract_first())
            interiorfloorspace= nws(response.css('span#m_property_dtl_blddata_val_interiorfloorspace::text').extract_first())
            heatingfuel= nws(response.css('span#m_property_dtl_blddata_val_heatingfuel::text').extract_first())
            style= nws(response.css('span#m_property_dtl_blddata_val_style::text').extract_first())
            utilitysewer= nws(response.css('span#m_property_dtl_blddata_val_utilitysewer::text').extract_first())
            utilitywater= nws(response.css('span#m_property_dtl_blddata_val_utilitywater::text').extract_first())

            amenitiesnearby = nws(response.css('span#m_property_dtl_data_val_amenitiesnearby::text').extract_first())
            farmtype = nws(response.css('span#m_property_dtl_data_val_farmtype::text').extract_first())
            monthlymaintenancefees = nws(response.css('span#m_property_dtl_data_val_monthlymaintenancefees::text').extract_first())
            parkingtype = nws(response.css('span#m_property_dtl_data_val_parkingtype::text').extract_first())
            pooltype = nws(response.css('span#m_property_dtl_data_val_pooltype::text').extract_first())
            totalparkingspaces = nws(response.css('span#m_property_dtl_data_val_totalparkingspaces::text').extract_first())
            zoningtype = nws(response.css('span#m_property_dtl_data_val_zoningtype::text').extract_first())
            

            description = nws(response.css('div#m_property_dtl_gendescription::text').extract_first())


        except:
            deleted = "Posting Deleted"
            traceback.print_exc()
        yield RealtorItem(deleted=deleted, \
                    my_url=my_url, \
                    listing_title=listing_title, \
                    price=price, \
                          \
                    #address=address, \
                    #bathroom=bathroom,\
                    description=description, \
                    #date=date, \
                          \
                    property_type = property_type, \
                    legal_title = legal_title, \
                    built_in = built_in, \
                    parking = parking, \
                    neighborhood = neighborhood, \
                    building_type = building_type, \
                          \
                    amenitiesnearby=amenitiesnearby,\
                    farmtype=farmtype,\
                    monthlymaintenancefees=monthlymaintenancefees,\
                    parkingtype=parkingtype,\
                    pooltype=pooltype,\
                    totalparkingspaces=totalparkingspaces,\
                    zoningtype=zoningtype,\
                          \
                    partialbathrooms=partialbathrooms, \
                    totalbathrooms=totalbathrooms, \
                    cooling=cooling, \
                    exteriorfinish=exteriorfinish, \
                    fireplace=fireplace, \
                    fireplacefuel=fireplacefuel, \
                    interiorfloorspace=interiorfloorspace, \
                    heatingfuel=heatingfuel, \
                    style=style, \
                    utilitysewer=utilitysewer, \
                    utilitywater=utilitywater, \
                          \
                    realtor_name=realtor_name,\
                    realtor_url=realtor_url,\
                    realtor_phone=realtor_phone,\
                    listingID=listingID,\
                    number_bedrooms=number_bedrooms,\
                    number_bathrooms=number_bathrooms,\
                    community_name=community_name,\
                    land_size=land_size,\
                    number_of_stories=number_of_stories,\
                    fax_number_broker=fax_number_broker,\
                    phone_number_broker=phone_number_broker,\
                    office_address_broker=office_address_broker,\
                    office_designation_broker=office_designation_broker,\
                    office_name_broker=office_name_broker,\
                    realtor_title=realtor_title)
