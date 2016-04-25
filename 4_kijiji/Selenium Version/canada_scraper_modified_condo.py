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
            

url_first = ['b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/gta-greater-toronto-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/ottawa-gatineau-area/page-','b-apartments-condos/barrie/page-','b-apartments-condos/belleville-area/page-','b-apartments-condos/brantford/page-','b-apartments-condos/brockville/page-','b-apartments-condos/chatham-kent/page-','b-apartments-condos/cornwall-on/page-','b-apartments-condos/guelph/page-','b-apartments-condos/hamilton/page-','b-apartments-condos/kapuskasing/page-','b-apartments-condos/kenora/page-','b-apartments-condos/kingston-area/page-','b-apartments-condos/kitchener-area/page-','b-apartments-condos/leamington/page-','b-apartments-condos/london/page-','b-apartments-condos/muskoka/page-','b-apartments-condos/norfolk-county/page-','b-apartments-condos/north-bay/page-','b-apartments-condos/owen-sound/page-','b-apartments-condos/peterborough-area/page-','b-apartments-condos/renfrew-county-area/page-','b-apartments-condos/sarnia-area/page-','b-apartments-condos/sault-ste-marie/page-','b-apartments-condos/st-catharines/page-','b-apartments-condos/sudbury/page-','b-apartments-condos/thunder-bay/page-','b-apartments-condos/timmins/page-','b-apartments-condos/windsor-area-on/page-','b-apartments-condos/woodstock-on/page-']
url_second = ['/c37l1700272?price=0__800','/c37l1700272?price=800__850','/c37l1700272?price=850__900','/c37l1700272?price=900__950','/c37l1700272?price=950__1000','/c37l1700272?price=1000__1050','/c37l1700272?price=1050__1100','/c37l1700272?price=1100__1150','/c37l1700272?price=1150__1200','/c37l1700272?price=1200__1250','/c37l1700272?price=1250__1300','/c37l1700272?price=1300__1350','/c37l1700272?price=1350__1400','/c37l1700272?price=1400__1450','/c37l1700272?price=1450__1500','/c37l1700272?price=1500__1550','/c37l1700272?price=1550__1600','/c37l1700272?price=1600__1650','/c37l1700272?price=1650__1700','/c37l1700272?price=1700__1750','/c37l1700272?price=1750__1800','/c37l1700272?price=1800__1850','/c37l1700272?price=1850__1900','/c37l1700272?price=1900__1950','/c37l1700272?price=1950__2000','/c37l1700272?price=2000__2050','/c37l1700272?price=2050__2100','/c37l1700272?price=2100__2150','/c37l1700272?price=2150__2200','/c37l1700272?price=2200__2250','/c37l1700272?price=2250__2300','/c37l1700272?price=2300__2350','/c37l1700272?price=2350__2400','/c37l1700272?price=2400__2450','/c37l1700272?price=2450__2500','/c37l1700272?price=2500__2550','/c37l1700272?price=2500__9999999','/c37l1700184?price=0__800','/c37l1700184?price=800__850','/c37l1700184?price=850__900','/c37l1700184?price=900__950','/c37l1700184?price=950__1000','/c37l1700184?price=1000__1050','/c37l1700184?price=1050__1100','/c37l1700184?price=1100__1150','/c37l1700184?price=1150__1200','/c37l1700184?price=1200__1250','/c37l1700184?price=1250__1300','/c37l1700184?price=1300__1350','/c37l1700184?price=1350__1400','/c37l1700184?price=1400__1450','/c37l1700184?price=1450__1500','/c37l1700184?price=1500__1550','/c37l1700184?price=1550__1600','/c37l1700184?price=1600__1650','/c37l1700184?price=1650__1700','/c37l1700184?price=1700__1750','/c37l1700184?price=1750__1800','/c37l1700184?price=1800__1850','/c37l1700184?price=1850__1900','/c37l1700184?price=1900__1950','/c37l1700184?price=1950__2000','/c37l1700184?price=2000__2050','/c37l1700184?price=2050__2100','/c37l1700184?price=2100__2150','/c37l1700184?price=2150__2200','/c37l1700184?price=2200__2250','/c37l1700184?price=2250__2300','/c37l1700184?price=2300__2350','/c37l1700184?price=2350__2400','/c37l1700184?price=2400__2450','/c37l1700184?price=2450__2500','/c37l1700184?price=2500__2550','/c37l1700184?price=2500__9999999','/c37l1700006','/c37l1700129','/c37l1700206','/c37l1700247','/c37l1700239','/c37l1700133','/c37l1700242','/c37l80014','/c37l1700237','/c37l1700249','/c37l1700181','/c37l1700209','/c37l1700240','/c37l1700214','/c37l1700078','/c37l1700248','/c37l1700243','/c37l1700187','/c37l1700217','/c37l1700074','/c37l1700189','/c37l1700244','/c37l80016','/c37l1700245','/c37l1700126','/c37l1700238','/c37l1700220','/c37l1700241']
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
                
                with open("OutputNext.txt", "a") as text_file:
                    text_file.write(myList[entry].get_attribute("href"))
                    text_file.write("\n")
        except:
            traceback.print_exc()
            pass

driver = webdriver.Firefox()


for area_page in range(34, len(url_first)):
    driver.get(url_base + url_first[area_page] + "1" + url_second[area_page])
    time.sleep(4)
    print "##### " + str(url_first[area_page])+ str(url_second[area_page]) + "   " +str(driver.find_element_by_css_selector("div.showing").text)
    time.sleep(4)
    number_of_adds = driver.find_element_by_css_selector("div.showing").text
    int_adds = number_of_adds.replace(",", "")
    int_adds = int_adds.split("of ")[1]
    int_adds = int_adds.split(" Ads")[0]
    int_adds = int(int_adds)
    pages_to_scrape = (int(int_adds)/int(20))+1
    print int_adds
    print pages_to_scrape
    get_listing(pages_to_scrape, area_page)




