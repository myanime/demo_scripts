# -*- coding: utf-8 -*-

from selenium import webdriver
import lxml.html
import time
import itertools
import csv


class Farmer:
    def __init__(self, myFileNameSave, myFileNameLoad, threadNumber):
        self.browser = webdriver.Firefox()
        self.fullText = ""
        self.farmNumber = 0
        self.myFileNameSave = myFileNameSave
        self.myFileNameLoad = myFileNameLoad
        self.threadNumber = threadNumber
    
    def goFarm(self):
        for self.x in range(0, 33):
            with open(self.myFileNameLoad, 'rb') as self.myList:
                self.spamreader = csv.reader(self.myList, delimiter=',', quotechar='|')
                for row in itertools.islice(self.spamreader, self.farmNumber, self.farmNumber + 1):
                    self.myFirstString = ', '.join(row)
                    print self.threadNumber
                    #print self.myFirstString
                    

                    self.browser.get("http://www.google.de")
                    self.searchBox = self.browser.find_element_by_xpath('//*[@id="lst-ib"]')
                    self.searchBox.send_keys(self.myFirstString.decode('latin-1'))
                    self.searchBox.submit()
                    try:
                        self.browser.implicitly_wait(2)
                        #print str(self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[6]/div/div[2]/span[1]').text)
                        self.phoneNumber = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[6]/div/div[2]/span[2]/span').text
                        #print self.phoneNumber
                    except:
                        print "No Phone"
                        self.phoneNumber = "None"
                    
                    
                    self.stringToWrite = str(self.farmNumber) + ", " + self.phoneNumber + "\n"
                    self.xText = self.stringToWrite.encode('utf-8')
                    self.myFile = open(self.myFileNameSave, 'a')
                    self.myFile.write(self.xText)
                    self.myFile.close()
                    #Clears the text and moves on to the next row
                    self.xText = ""
                    self.farmNumber = self.farmNumber + 1
