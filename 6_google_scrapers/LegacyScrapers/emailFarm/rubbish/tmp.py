from selenium import webdriver
import time
import lxml.html
import traceback
import itertools
import csv
import codecs
import time

def getURL():
    driver = webdriver.Firefox()
    with open ("myList.csv", 'rb') as searchList:
        myCSV = csv.reader(searchList, delimiter='|', quotechar='"')
        start = 210
        stop = 1000
        for company in itertools.islice(myCSV, start, stop):
            time.sleep(1)
            text = company[3].decode('utf-8')
            driver.implicitly_wait(20)
            time.sleep(.3)
            driver.get("file:///home/myanime/Desktop/webScrapers/webForum/google/Google.html")
            time.sleep(.3)
            searchbox = driver.find_element_by_xpath('//*[@id="lst-ib"]')
            searchbox.send_keys(text)
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]').click()
            driver.implicitly_wait(20)
            time.sleep(6)
            #driver.find_element_by_xpath('//*[@id="rso"]/div/div[1]/div/h3/a').click()
            time.sleep(2)
