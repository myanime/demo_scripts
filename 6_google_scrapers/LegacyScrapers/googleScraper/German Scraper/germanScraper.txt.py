# -*- coding: utf-8 -*-
# https://www.upwork.com/jobs/Crawling-job-for-publicly-available-information_~01a8f0b86113638bbd

from selenium import webdriver
import lxml.html
import time
import itertools
import csv


browser = webdriver.Firefox()
fullText = ""
farmNumber = 0
for x in range(0, 33):
    with open('myList.csv', 'rb') as myList:
        spamreader = csv.reader(myList, delimiter=',', quotechar='|')
        for row in itertools.islice(spamreader, farmNumber, farmNumber + 1):
            myFirstString = ', '.join(row)
            print myFirstString

            browser.get("http://www.google.de")
            searchBox = browser.find_element_by_xpath('//*[@id="lst-ib"]')
            searchBox.send_keys(myFirstString.decode('latin-1'))
            searchBox.submit()
            time.sleep(2.5)
            try:
                print str(browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[6]/div/div[2]/span[1]').text)
                phoneNumber = browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[6]/div/div[2]/span[2]/span').text
                print phoneNumber
            except:
                print "No Phone"
                phoneNumber = "None"
            
            
            stringToWrite = str(farmNumber) + ", " + phoneNumber + "\n"
            xText = stringToWrite.encode('utf-8')
            myFile = open("phoneNumbers.txt", 'a')
            myFile.write(xText)
            myFile.close()
            #Clears the text and moves on to the next row
            xText = ""
            farmNumber = farmNumber + 1
