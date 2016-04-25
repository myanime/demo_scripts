from selenium import webdriver
import os
import time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import threading
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import traceback
import csv
import itertools
import fileinput
import random

start_page = 8900
scraper_number = 5
url_base = "https://www.realtor.ca/Residential/Map.aspx#CultureId=1&ApplicationId=1&RecordsPerPage=9&MaximumResults=9&PropertySearchTypeId=1&TransactionTypeId=2&StoreyRange=0-0&BedRange=0-0&BathRange=0-0&LongitudeMin=-106.4925231933594&LongitudeMax=-65.0960388183594&LatitudeMin=38.00162867052972&LatitudeMax=60.00245421381937&SortOrder=A&SortBy=1&viewState=m&CurrentPage="
url_start = url_base + str(start_page)

driver = webdriver.Firefox()
time.sleep(10)
driver.get(url_start)
time.sleep(10)
area_page = start_page * 9
current_page = start_page

for x in range(0, 1500):
    try:
        for i in range(1, 10):
            try:
                with open("url_list" + str(scraper_number), "a") as f: 
                    f.write(driver.find_element_by_xpath("/html/body/form/div[4]/div[1]/div[5]/div/div[1]/div[5]/div[1]/div/div[" + str(i) +"]/a").get_attribute("href"))
                    f.write('\n')
            except:
                with open("url_list" + str(scraper_number), "a") as f:
                    f.write("error")
                    f.write("\n")
        time.sleep(5)
        driver.find_element_by_css_selector("#nextPage").click()
        #print area_page
        area_page = area_page + 9
        current_page = current_page + 1
        print current_page
        time.sleep(5)
    except:
        time.sleep(10)
        driver.get(url_base + str(current_page))
        time.sleep(15)
        print traceback.print_exc()
