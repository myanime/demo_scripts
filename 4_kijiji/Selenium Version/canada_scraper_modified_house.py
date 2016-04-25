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

url_first = ['b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/gta-greater-toronto-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/ottawa-gatineau-area/page-','b-house-rental/barrie/page-','b-house-rental/belleville-area/page-','b-house-rental/brantford/page-','b-house-rental/brockville/page-','b-house-rental/chatham-kent/page-','b-house-rental/cornwall-on/page-','b-house-rental/guelph/page-','b-house-rental/hamilton/page-','b-house-rental/kapuskasing/page-','b-house-rental/kenora/page-','b-house-rental/kingston-area/page-','b-house-rental/kitchener-area/page-','b-house-rental/leamington/page-','b-house-rental/london/page-','b-house-rental/muskoka/page-','b-house-rental/norfolk-county/page-','b-house-rental/north-bay/page-','b-house-rental/owen-sound/page-','b-house-rental/peterborough-area/page-','b-house-rental/renfrew-county-area/page-','b-house-rental/sarnia-area/page-','b-house-rental/sault-ste-marie/page-','b-house-rental/st-catharines/page-','b-house-rental/sudbury/page-','b-house-rental/thunder-bay/page-','b-house-rental/timmins/page-','b-house-rental/windsor-area-on/page-','b-house-rental/woodstock-on/page-']
url_second = ['/c43l1700272?price=0__800','/c43l1700272?price=800__850','/c43l1700272?price=850__900','/c43l1700272?price=900__950','/c43l1700272?price=950__1000','/c43l1700272?price=1000__1050','/c43l1700272?price=1050__1100','/c43l1700272?price=1100__1150','/c43l1700272?price=1150__1200','/c43l1700272?price=1200__1250','/c43l1700272?price=1250__1300','/c43l1700272?price=1300__1350','/c43l1700272?price=1350__1400','/c43l1700272?price=1400__1450','/c43l1700272?price=1450__1500','/c43l1700272?price=1500__1550','/c43l1700272?price=1550__1600','/c43l1700272?price=1600__1650','/c43l1700272?price=1650__1700','/c43l1700272?price=1700__1750','/c43l1700272?price=1750__1800','/c43l1700272?price=1800__1850','/c43l1700272?price=1850__1900','/c43l1700272?price=1900__1950','/c43l1700272?price=1950__2000','/c43l1700272?price=2000__2050','/c43l1700272?price=2050__2100','/c43l1700272?price=2100__2150','/c43l1700272?price=2150__2200','/c43l1700272?price=2200__2250','/c43l1700272?price=2250__2300','/c43l1700272?price=2300__2350','/c43l1700272?price=2350__2400','/c43l1700272?price=2400__2450','/c43l1700272?price=2450__2500','/c43l1700272?price=2500__2550','/c43l1700272?price=2500__9999999','/c43l1700184?price=0__800','/c43l1700184?price=800__850','/c43l1700184?price=850__900','/c43l1700184?price=900__950','/c43l1700184?price=950__1000','/c43l1700184?price=1000__1050','/c43l1700184?price=1050__1100','/c43l1700184?price=1100__1150','/c43l1700184?price=1150__1200','/c43l1700184?price=1200__1250','/c43l1700184?price=1250__1300','/c43l1700184?price=1300__1350','/c43l1700184?price=1350__1400','/c43l1700184?price=1400__1450','/c43l1700184?price=1450__1500','/c43l1700184?price=1500__1550','/c43l1700184?price=1550__1600','/c43l1700184?price=1600__1650','/c43l1700184?price=1650__1700','/c43l1700184?price=1700__1750','/c43l1700184?price=1750__1800','/c43l1700184?price=1800__1850','/c43l1700184?price=1850__1900','/c43l1700184?price=1900__1950','/c43l1700184?price=1950__2000','/c43l1700184?price=2000__2050','/c43l1700184?price=2050__2100','/c43l1700184?price=2100__2150','/c43l1700184?price=2150__2200','/c43l1700184?price=2200__2250','/c43l1700184?price=2250__2300','/c43l1700184?price=2300__2350','/c43l1700184?price=2350__2400','/c43l1700184?price=2400__2450','/c43l1700184?price=2450__2500','/c43l1700184?price=2500__2550','/c43l1700184?price=2500__9999999','/c43l1700006','/c43l1700129','/c43l1700206','/c43l1700247','/c43l1700239','/c43l1700133','/c43l1700242','/c43l80014','/c43l1700237','/c43l1700249','/c43l1700181','/c43l1700209','/c43l1700240','/c43l1700214','/c43l1700078','/c43l1700248','/c43l1700243','/c43l1700187','/c43l1700217','/c43l1700074','/c43l1700189','/c43l1700244','/c43l80016','/c43l1700245','/c43l1700126','/c43l1700238','/c43l1700220','/c43l1700241']
url_base = "http://www.kijiji.ca/"

def get_listing(pages_to_scrape, area_page):
    for x in range(1,pages_to_scrape):
        try:
            print x
            try:
                driver.set_page_load_timeout(30)
                driver.get(url_base + url_first[area_page] + str(x) + url_second[area_page])
            except:
                time.sleep(5)
                traceback.print_exc()
                pass
            time.sleep(1)
            myList = driver.find_elements_by_css_selector('a.title')
            for entry in range(0, len(myList)):
                
                with open("housenew", "a") as text_file:
                    text_file.write(myList[entry].get_attribute("href"))
                    text_file.write("\n")
        except:
            traceback.print_exc()
            pass

driver = webdriver.Firefox()

for area_page in range(0, len(url_first)):
    driver.get(url_base + url_first[area_page] + "1" + url_second[area_page])
    time.sleep(2)
    print "##### " + str(url_first[area_page])+ str(url_second[area_page]) + "   " +str(driver.find_element_by_css_selector("div.showing").text)
    time.sleep(2)
    number_of_adds = driver.find_element_by_css_selector("div.showing").text
    int_adds = number_of_adds.replace(",", "")
    int_adds = int_adds.split("of ")[1]
    int_adds = int_adds.split(" Ads")[0]
    int_adds = int(int_adds)
    pages_to_scrape = (int(int_adds)/int(20))+1
    print int_adds
    print pages_to_scrape
    get_listing(pages_to_scrape, area_page)




