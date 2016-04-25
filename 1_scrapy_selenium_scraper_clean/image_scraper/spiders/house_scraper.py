from image_scraper.items import HousePicture
import scrapy
import time
import string
from scrapy.http import FormRequest
from scrapy.item import Item, Field
from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
from selenium import webdriver
import random
import time
class MyHouseSpider(scrapy.Spider):
    name = "my-house-spider"
    start_urls = ["https://www.google.com/"]
    number_of_pictures_to_scrape = 10
    def parse(self, response):
        print "#############################Google Image Scraper VERSION 1##############################"

        #Add the list of Search terms to this array
        city_urls = ['Jurmala', 'Florida', 'Miami']

        #Opens Selenium and Navigates to google.de
        driver = webdriver.Firefox()
        picture_array = []
        
        #Will loop through the city_urls (search terms)
        for city_number in range(0,len(city_urls)):
            i = 1
            while i < self.number_of_pictures_to_scrape:
                try:
                    search_string = string.replace(city_urls[city_number], '-', '+')
                    time.sleep(random.randrange(0,1,1))
                    driver.get("https://www.google.com/search?q=" + search_string + " beach+Homes&tbs=isz:lt%2Cislt:4mp&tbm=isch")
                    #Gets the URL of Image x
                    picture_url = driver.find_element_by_xpath("/html/body/div[5]/div[4]/div[2]/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div[1]/div[" +str(i) + "]/a").get_attribute("href")
                    #Clears the google path to give clean Image URL Path
                    picture_url = picture_url.split('http://images.google.de/imgres?imgurl=', 1)[1]
                    picture_url = picture_url.split('&imgrefurl', 1)[0]
                    picture_array.append(picture_url)
                    #Sends the URL to Scrapy to crawl and download
                    yield HousePicture(image_urls=[picture_url], my_nice_file_name=city_urls[city_number])
                    i = i + 1
                except:
                    i = i + 1
                
