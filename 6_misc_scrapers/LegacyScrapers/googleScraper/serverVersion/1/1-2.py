# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import *
import threading
import time
import itertools
import csv
import urllib2
import socket
import random
import logging
import sys
import codecs
import io
import shutil
import sys

sys.setrecursionlimit(10000)




logging.basicConfig(level=logging.INFO, filename="googleScraper.log")

listLoad = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv", "8.csv", "9.csv", "10.csv", "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv", "21.csv", "22.csv", "23.csv", "24.csv", "25.csv"]
listSave = ["phone1.txt", "phone2.txt", "phone3.txt", "phone4.txt", "phone5.txt", "phone6.txt", "phone7.txt", "phone8.txt", "phone9.txt", "phone10.txt", "phone11.txt", "phone12.txt", "phone13.txt", "phone14.txt", "phone15.txt", "phone16.txt", "phone17.txt", "phone18.txt", "phone19.txt", "phone20.txt","phone21.txt", "phone22.txt", "phone23.txt", "phone24.txt", "phone25.txt"]
listNumber = ["Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25"]
currentRowInSearchListArray = [\
    #1
    0,\
    #2
    7929,\
    #3
    0,\
    #4
    0,\
    #5
    0,\
    #6
    0,\
    #7
    0,\
    #8
    0,\
    #9
    0,\
    #10
    0,\
    #11
    0,\
    #12
    0,\
    #13
    0,\
    #14
    0,\
    #15
    0,\
    #16
    0,\
    #17
    0,\
    #18
    0,\
    #19
    0,\
    #20
    0,\
    #21
    0,\
    #22
    0,\
    #23
    0,\
    #24
    0,\
    #25
    0,]
google = True

def main():
    if google == True:
        multiThreading()
    
def myFarmer(myFileName, myFileNameLoad, threadNumber, currentRowInSearchList):
    farmThread = Farmer(myFileName, myFileNameLoad, threadNumber, currentRowInSearchList)  

def multiThreading():
    for number in range (1, 2):
        
        try:
            print "multiThreading Started"
            myFileNameSave = "./phonenumbers/" + listSave[number]
            myFileNameLoad = "./csv/" + listLoad[number]
            myThreadNumber = listNumber[number]
            currentRowInSearchList = currentRowInSearchListArray[number]
            t = threading.Thread(target=myFarmer, args = (myFileNameSave, myFileNameLoad, myThreadNumber, currentRowInSearchList))
            t.start()
            time.sleep(15)
        except Exception, detail:
                print "ERROR:", detail



class Farmer:
    def __init__(self, myFileNameSave, myFileNameLoad, threadNumber, currentRowInSearchList):
        print "Constructor Started"
        self.fullText = ""
        self.currentRowInSearchList = currentRowInSearchList
        self.farmNumber = currentRowInSearchList
        self.myFileNameSave = myFileNameSave
        self.myFileNameLoad = myFileNameLoad
        self.threadNumber = threadNumber
        self.startScraper(self.threadNumber)
        
        
    def startScraper(self, threadNumber):
        print "Logfile Created"
        logging.info('Log file for ' + str(threadNumber) +  " " + str(time.ctime()))
        print "Starting Scraper"
        self.loadGoogle()

    def loadGoogle(self):
        try:
            logging.info("LoadGoogle: ," + str(self.threadNumber) + str(time.ctime()))
            self.browser = webdriver.Firefox()
            self.goFarm()
        except Exception, detail:
            print "ERROR:", detail
            time.sleep(15)
            print "######################RESTARTING" +  self.threadNumber +"#######################"
            try:
                self.browser.quit()
            except:
                pass
            myFarmer(self.myFileNameSave, self.myFileNameLoad, self.threadNumber, self.currentRowInSearchList)
            

    def goFarm(self):
        startRow = self.currentRowInSearchList
        for self.currentRowInSearchList in range (startRow, 10000):
            
            #######################Gets the Phone number from Goodle##################################
            with open(self.myFileNameLoad, 'rb') as self.myList:
                self.spamreader = csv.reader(self.myList, delimiter=',', quotechar='|')
                for row in itertools.islice(self.spamreader, self.farmNumber, self.farmNumber + 1):
                    #self.myFirstString = ', '.join(row)
                    self.myFirstString = row[0]
                    self.businessName = self.myFirstString
                    #print self.myFirstString
                    try:
                        #Open Google with 10sec load
                        self.browser.implicitly_wait(20)
                        self.browser.get("http://www.google.de")
                        time.sleep(1)
                      
                    except:
                        ###################
                        print "Proxy too slow"
                        #logging.info(str(self.threadNumber) + ",Proxy too slow goFarm," + ",currentRowInSearchList:," + str(self.currentRowInSearchList) + "," + str(time.ctime()))
                        ###################
                        self.moveOnToNextProxy()
                    try:
                        self.browser.implicitly_wait(20)
                        self.searchBox = self.browser.find_element_by_xpath('//*[@id="lst-ib"]')
                        self.searchBox.send_keys(self.myFirstString.decode('utf-8'))
                        self.searchBox.submit()
                    except:
                        ###############################
                        print "Problem Loading Google"
                        #logging.info(str(self.threadNumber) + ",Problem loading google goFarm," + ",currentRowInSearchList:," + str(self.currentRowInSearchList) + "," + str(time.ctime()))
                        ###############################
                        self.moveOnToNextProxy()

                    try:
                        self.browser.implicitly_wait(10)
                        self.myBusinessName = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/div[2]/div/div[2]').text
                        try:
                            self.myBusinessDescription = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/div[3]').text
                        except:
                            self.myBusinessDescription = "No Business Description"
                        try:
                            self.myAddress = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/div[7]/div/div[1]/span[2]').text
                        except:
                            self.myAddress = "No Address"
                        self.phoneNumber = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/div[7]/div/div[2]/span[2]').text



                        ############################################
                        #logging.info(str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",BusinessName:," + self.myBusinessName + ",Phone:," + str(self.phoneNumber) + "," + str(time.ctime()))
                        print str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",BusinessName:," + self.myBusinessName + ",Phone:," + str(self.phoneNumber) + "," +str(time.ctime())
                        ############################################
                           
                    except:
                        #No Phone, Bad proxy or Google capcha"
                        self.seleniumProxyChecker()
                        self.myBusinessName = "No Business Name"
                        self.phoneNumber = "None"
                        self.myBusinessDescription = "No Business Description"
                        self.myAddress = "No Address"
                        
                        ############################################
                        print str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone: NONE," + str(time.ctime())
                        #logging.info(str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone: NONE," + str(time.ctime()))
                        ############################################

                    ############# Write phone number to Text file ##################
                    self.stringToWrite = "," + self.phoneNumber 
                    self.xText = self.stringToWrite.encode('utf-8')
                    
                    self.myFile = open(self.myFileNameSave, 'a')
                    self.myFile.write(row[0])
                    self.myFile.write(", ")
                    self.myFile.write(row[1])
                    self.myFile.write(", ")
                    self.myFile.write(row[2])
                    self.myFile.write(", ")
                    self.myFile.write(row[3])
                    self.myFile.write(", ")
                    self.myFile.write(row[4])
                    self.myFile.write(", ")
                    self.myFile.write(row[5])
                    self.myFile.write(", ")
                    self.myFile.write(row[6])

                    self.myFile.write(", ")
                    self.myFile.write(str(self.farmNumber))
                    self.myFile.write(', "')
                    self.myFile.write(self.myBusinessName.encode('utf-8'))
                    self.myFile.write('", ')
                    self.myFile.write(self.phoneNumber.encode('utf-8'))
                    self.myFile.write(', "')
                    self.myFile.write(self.myBusinessDescription.encode('utf-8'))
                    self.myFile.write('", "')
                    self.myFile.write(self.myAddress.encode('utf-8'))
                    self.myFile.write('"\n') 
                    
                    self.myFile.close()
                    #Clears the text and moves on to the next row
                    self.xText = ""
                    #################################################################

                    myNumber = random.randrange(2, 5, 1)
                    time.sleep(myNumber)
                    self.farmNumber = self.farmNumber + 1
                
    def moveOnToNextProxy(self):
        self.browser.quit()
        time.sleep(1)
        self.loadGoogle()
        
        

    ###################Selenium Proxy Checker########################

    def seleniumProxyChecker(self):
        errorSource = self.browser.page_source 
        if "The connection has timed out" or "The proxy server is refusing" or "type the characters" or "computer or network may be sending"  or "Our systems have detected unusual traffic from your computer" in errorSource:
            if "The connection has timed out" in errorSource:
                ##############
                print "gotSlowConnection"
                logging.info("SELENIUM_PROXY_CHECKER," + str(self.threadNumber) + ",gotSlowConnection," + str(time.ctime()))
                ##############
                self.moveOnToNextProxy()
            elif "The proxy server is refusing" in errorSource:
                ##############
                print "gotBadProxy"
                logging.info("SELENIUM_PROXY_CHECKER," + str(self.threadNumber) + ",gotBadProxy," + str(time.ctime()))
                ##############
                self.moveOnToNextProxy()
            elif "type the characters" in errorSource:
                ##############
                print "gotEbaniCaptcha"
                logging.info("SELENIUM_PROXY_CHECKER," + str(self.threadNumber) + ",gotEbaniCaptcha," + str(time.ctime()))
                ##############
                time.sleep(86000)
                self.moveOnToNextProxy()
            elif "computer or network may be sending" in errorSource:
                ##############
                print "GOOGLE BAN"
                logging.info("SELENIUM_PROXY_CHECKER," + str(self.threadNumber) + ",GOOGLEBAN," + str(time.ctime()))
                ##############
                self.moveOnToNextProxy()
            elif "Our systems have detected unusual traffic from your computer" in errorSource:
                 ##############
                print "GOOGLE BAN 2"
                logging.info("SELENIUM_PROXY_CHECKER," + str(self.threadNumber) + ",GOOGLEBAN 2," + str(time.ctime()))
                ##############
                self.moveOnToNextProxy()
            else:
                #print "Simply no telephone :-) "
                pass
        else:
            pass

  
            
    ##################################################################

if __name__ == '__main__':
    main()
