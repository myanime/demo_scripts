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


url_first = ['b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/gta-greater-toronto-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/ottawa-gatineau-area/page-','b-room-rental-roommate/barrie/page-','b-room-rental-roommate/belleville-area/page-','b-room-rental-roommate/brantford/page-','b-room-rental-roommate/brockville/page-','b-room-rental-roommate/chatham-kent/page-','b-room-rental-roommate/cornwall-on/page-','b-room-rental-roommate/guelph/page-','b-room-rental-roommate/hamilton/page-','b-room-rental-roommate/kapuskasing/page-','b-room-rental-roommate/kenora/page-','b-room-rental-roommate/kingston-area/page-','b-room-rental-roommate/kitchener-area/page-','b-room-rental-roommate/leamington/page-','b-room-rental-roommate/london/page-','b-room-rental-roommate/muskoka/page-','b-room-rental-roommate/norfolk-county/page-','b-room-rental-roommate/north-bay/page-','b-room-rental-roommate/owen-sound/page-','b-room-rental-roommate/peterborough-area/page-','b-room-rental-roommate/renfrew-county-area/page-','b-room-rental-roommate/sarnia-area/page-','b-room-rental-roommate/sault-ste-marie/page-','b-room-rental-roommate/st-catharines/page-','b-room-rental-roommate/sudbury/page-','b-room-rental-roommate/thunder-bay/page-','b-room-rental-roommate/timmins/page-','b-room-rental-roommate/windsor-area-on/page-','b-room-rental-roommate/woodstock-on/page-']
url_second = ['/c36l1700272?price=0__200','/c36l1700272?price=150__200','/c36l1700272?price=200__250','/c36l1700272?price=250__300','/c36l1700272?price=300__350','/c36l1700272?price=350__400','/c36l1700272?price=400__450','/c36l1700272?price=450__500','/c36l1700272?price=500__550','/c36l1700272?price=550__600','/c36l1700272?price=600__650','/c36l1700272?price=650__700','/c36l1700272?price=700__8000','/c36l1700184?price=0__200','/c36l1700184?price=150__200','/c36l1700184?price=200__250','/c36l1700184?price=250__300','/c36l1700184?price=300__350','/c36l1700184?price=350__400','/c36l1700184?price=400__450','/c36l1700184?price=450__500','/c36l1700184?price=500__550','/c36l1700184?price=550__600','/c36l1700184?price=600__650','/c36l1700184?price=650__700','/c36l1700184?price=700__8000','c36l1700006','/c36l1700129','/c36l1700206','/c36l1700247','/c36l1700239','/c36l1700133','/c36l1700242','/c36l80014','/c36l1700237','/c36l1700249','/c36l1700181','/c36l1700209','/c36l1700240','/c36l1700214','/c36l1700078','/c36l1700248','/c36l1700243','/c36l1700187','/c36l1700217','/c36l1700074','/c36l1700189','/c36l1700244','/c36l80016','/c36l1700245','/c36l1700126','/c36l1700238','/c36l1700220','/c36l1700241']
url_base = "http://www.kijiji.ca/"
print len(url_first)
print len(url_second)

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
                
                with open("roomnew", "a") as text_file:
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




