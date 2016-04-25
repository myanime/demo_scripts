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


logging.basicConfig(level=logging.INFO, filename="googleScraper.log")

listLoad = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv", "8.csv", "9.csv", "10.csv", "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv", "21.csv", "22.csv", "23.csv", "24.csv", "25.csv"]
listSave = ["phone1.txt", "phone2.txt", "phone3.txt", "phone4.txt", "phone5.txt", "phone6.txt", "phone7.txt", "phone8.txt", "phone9.txt", "phone10.txt", "phone11.txt", "phone12.txt", "phone13.txt", "phone14.txt", "phone15.txt", "phone16.txt", "phone17.txt", "phone18.txt", "phone19.txt", "phone20.txt","phone21.txt", "phone22.txt", "phone23.txt", "phone24.txt", "phone25.txt"]
listNumber = ["Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25"]
threadInt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
proxyStartNumber = [38, 85, 145, 205, 265, 325, 385, 445, 505, 565, 625, 685, 745, 805, 865, 925, 985, 1045, 1105, 1165, 1225, 1285, 1345, 1405, 1465, 1525, 475, 295]
currentRowInSearchListArray = [2271, 1396, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

restartModule = [None] * 25
google = True

def main():
    if google == True:
        multiThreading()
    
def myFarmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber, currentRowInSearchList):
    farmThread = Farmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber, currentRowInSearchList)  

def multiThreading():
    for number in range (2, 4):
        
        try:
            print "multiThreading Started"
            myFileNameSave = "./phonenumbers/" + listSave[number]
            myFileNameLoad = "./csv/" + listLoad[number]
            myThreadNumber = listNumber[number]
            wantedProxyNumber = proxyStartNumber[number]
            currentRowInSearchList = currentRowInSearchListArray[number]
            t = threading.Thread(target=myFarmer, args = (myFileNameSave, myFileNameLoad, myThreadNumber, wantedProxyNumber, currentRowInSearchList))
            t.start()
            time.sleep(15)
        except Exception, detail:
                print "ERROR:", detail


###############################################################


#######################PROXY CHECK#############################

def myChecker():
    myFileName = "./phonenumbers/" + listSave[1]
    myFileNameLoad = "./csv/" + listLoad[1]
    threadNumber = listNumber[0]
    wantedProxyNumber = 0

def c():
    farmThread = Farmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber)
    for x in range (0, 30):
        print farmThread.myProxyArray[x]
        
def checker():
    farmThread = Farmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber)
    for x in range (0, 20):
        print farmThread.quickCheck(x)
        

#############Scraper with automatic proxy checker############

class Farmer:
    def __init__(self, myFileNameSave, myFileNameLoad, threadNumber, wantedProxyNumber, currentRowInSearchList):
        print "Constructor Started"
        self.numberOfProxiesInList = 100

        ##########Loads Proxy List into Array################
        proxyArray = [1] * 100
        proxyNumber = 0
        for x in range (0, 100):
            proxyListName = "./proxylist/proxylist.csv"
            with open(proxyListName, 'rb') as myList:
                proxyCSVObject = csv.reader(myList, delimiter=',', quotechar='|')
                for row in itertools.islice(proxyCSVObject, proxyNumber, proxyNumber + 1):
                    proxyLineInTextFile = ', '.join(row)
                    proxyArray[proxyNumber] = str(proxyLineInTextFile)
                    proxyNumber = proxyNumber + 1
        self.myProxyArray = proxyArray
        #####################################################


        self.fullText = ""
        self.currentRowInSearchList = currentRowInSearchList
        self.farmNumber = currentRowInSearchList
        self.myFileNameSave = myFileNameSave
        self.myFileNameLoad = myFileNameLoad
        self.threadNumber = threadNumber
        self.goodProxyNumber = 1
        self.startScraper(self.threadNumber, self.goodProxyNumber)
        
        
    def startScraper(self, threadNumber, goodProxyNumber):
        print "Logfile Created"
        logging.info('Log file for ' + str(threadNumber) +  " " + str(time.ctime()))
        print "Starting Scraper"
        self.loadGoogle(goodProxyNumber)
                     
    def myProxyListChecker(self, x):
        if x >= self.numberOfProxiesInList:
            x = 1
            print "proxy List Finished Starting at the beginning"
            logging.info("PROXY, myProxyListChecker: ," + str(self.threadNumber) + ",LIST FINNISHED starting at beginning")
        while x < self.numberOfProxiesInList:
            if self.quickCheck(x):
                logging.info("PROXY, myProxyListChecker: ," + str(self.threadNumber) + ",USING PROXY: ," + str(x))
                return x
            else:
                x = x + 1
        

    def is_bad_proxy(self, pip):    
        try:
            proxy_handler = urllib2.ProxyHandler({'http': pip})
            opener = urllib2.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib2.install_opener(opener)
            req=urllib2.Request('http://www.bild.de/')  # change the URL to test here
            sock=urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            #print 'Error code: ', e.code
            #return e.code
            return True
        except Exception, detail:
            #print "ERROR:", detail
            return True
        return False

    def quickCheck(self, wantedProxyNumber):
        
        socket.setdefaulttimeout(60)
        currentProxy = self.myProxyArray[wantedProxyNumber]
        
        if self.is_bad_proxy(currentProxy):
            #print "Bad Proxy %s" % (currentProxy)
            return False
        else:
            #print "%s is working" % (currentProxy)
            #return True
            return currentProxy
    

    def loadGoogle(self, goodProxyNumber):
        try:
            '''
            myProxy = self.myProxyArray[goodProxyNumber]
            #print "using proxy number " + str(useProxyNumber) + " " + str(myProxy[x])
            self.proxy = Proxy({
                'proxyType': ProxyType.MANUAL,
                'httpProxy': myProxy,
                'ftpProxy': myProxy,
                'sslProxy': myProxy,
                'noProxy': '' # set this value as desired
                })
            '''
            print "THREAD: " + str(self.threadNumber)
            logging.info("PROXY, loadGoogle: ," + str(self.threadNumber) + str(time.ctime()))

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
            myFarmer(self.myFileNameSave, self.myFileNameLoad, self.threadNumber, self.goodProxyNumber, self.currentRowInSearchList)
            

    def goFarm(self):
        startRow = self.currentRowInSearchList
        for self.currentRowInSearchList in range (startRow, 3000):
            
            #######################Gets the Phone number from Goodle##################################
            with open(self.myFileNameLoad, 'rb') as self.myList:
                self.spamreader = csv.reader(self.myList, delimiter=',', quotechar='|')
                for row in itertools.islice(self.spamreader, self.farmNumber, self.farmNumber + 1):
                    #self.myFirstString = ', '.join(row)
                    self.myFirstString = row[0] + " " +row[1]
                    self.businessName = self.myFirstString
                    #print self.myFirstString
                    try:
                        #Open Google with 10sec load
                        self.browser.implicitly_wait(20)
                        self.browser.get("http://www.google.de")
                        time.sleep(1)
                        self.seleniumProxyChecker()         
                    except:
                        ###################
                        print "Proxy too slow"
                        logging.info(str(self.threadNumber) + ",Proxy too slow goFarm," + ",currentRowInSearchList:," + str(self.currentRowInSearchList) + "," + str(time.ctime()))
                        ###################
                        self.moveOnToNextProxy()
                    try:   
                        self.searchBox = self.browser.find_element_by_xpath('//*[@id="lst-ib"]')
                        self.searchBox.send_keys(self.myFirstString.decode('latin-1'))
                        self.searchBox.submit()
                    except:
                        ###############################
                        print "Problem Loading Google"
                        logging.info(str(self.threadNumber) + ",Problem loading google goFarm," + ",currentRowInSearchList:," + str(self.currentRowInSearchList) + "," + str(time.ctime()))
                        ###############################
                        self.moveOnToNextProxy()

                    try:
                        self.browser.implicitly_wait(20)
                        self.myBusinessName = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[2]/div/div[2]').text
                        self.phoneNumber = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[6]/div/div[2]/span[2]/span').text

                        ############################################
                        logging.info(str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",BusinessName:," + self.myBusinessName + ",Phone:," + str(self.phoneNumber) + "," + str(time.ctime()))
                        print str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",BusinessName:," + self.myBusinessName + ",Phone:," + str(self.phoneNumber) + "," +str(time.ctime())
                        ############################################
                        
                    except:
                        #No Phone, Bad proxy or Google capcha"
                        self.seleniumProxyChecker()
                        self.myBusinessName = "No Business Name"
                        self.phoneNumber = "None"
                        
                        ############################################
                        print str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone: NONE," + str(time.ctime())
                        logging.info(str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone: NONE," + str(time.ctime()))
                        ############################################
                    
                    ############# Write phone number to Text file ##################
                    self.stringToWrite = "," + self.phoneNumber 
                    self.xText = self.stringToWrite.encode('latin-1')
                    self.myFile = open(self.myFileNameSave, 'a')
                    self.myFile.write(str(self.farmNumber))
                    self.myFile.write(", ")
                    self.myFile.write(self.businessName)
                    self.myFile.write(", ")
                    self.myFile.write(self.myBusinessName.encode('latin-1'))
                    self.myFile.write(self.xText)
                    self.myFile.write(", ")
                    self.myFile.write(row[2])
                    self.myFile.write("\n") 
                    
                    self.myFile.close()
                    #Clears the text and moves on to the next row
                    self.xText = ""
                    #################################################################
                    
                    
                    myNumber = random.randrange(2, 5, 1)
                    time.sleep(myNumber)
                    self.farmNumber = self.farmNumber + 1
                
    def moveOnToNextProxy(self):
        self.browser.quit()
        time.sleep(5)
        self.goodProxyNumber = self.goodProxyNumber + 1
        self.goodProxyNumber = self.myProxyListChecker(self.goodProxyNumber)
        self.loadGoogle(self.goodProxyNumber)
        time.sleep(5)
        
        

    ###################Selenium Proxy Checker########################

    def seleniumProxyChecker(self):
        errorSource = self.browser.page_source
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

  
            
    ##################################################################

if __name__ == '__main__':
    main()
