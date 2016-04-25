# -*- coding: utf-8 -*-
#! /usr/local/lib/python2.7

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
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages')
sys.path.append('/usr/lib/python2.7/dist-packages/selenium-2.47.3/py/selenium/')

logging.basicConfig(level=logging.INFO, filename="googleScraper.log")

listLoad = ["1.csv", "2.csv", "3.csv", "4.csv", "5.csv", "6.csv", "7.csv", "8.csv", "9.csv", "10.csv", "11.csv", "12.csv", "13.csv", "14.csv", "15.csv", "16.csv", "17.csv", "18.csv", "19.csv", "20.csv", "21.csv", "22.csv", "23.csv", "24.csv", "25.csv"]
listSave = ["phone1.txt", "phone2.txt", "phone3.txt", "phone4.txt", "phone5.txt", "phone6.txt", "phone7.txt", "phone8.txt", "phone9.txt", "phone10.txt", "phone11.txt", "phone12.txt", "phone13.txt", "phone14.txt", "phone15.txt", "phone16.txt", "phone17.txt", "phone18.txt", "phone19.txt", "phone20.txt","phone21.txt", "phone22.txt", "phone23.txt", "phone24.txt", "phone25.txt"]
listNumber = ["Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25"]
threadInt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
proxyStartNumber = [416, 49, 617, 60, 80, 100, 220, 140, 160, 180]
currentRowInSearchListArray = [5000 , 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000]

restartModule = [None] * 25



def startx2():
    print "quit"
def startx():
    
    for number in range (0, 5):
        
        try:
            myFileNameSave = "./phonenumbers/" + listSave[number]
            myFileNameLoad = "./csv/" + listLoad[number]
            myThreadNumber = listNumber[number]
            iterationNumber = currentRowInSearchListArray[number]
            print myThreadNumber + " starting..."

            t = threading.Thread(target=simpleScraper, args = (myFileNameSave, myFileNameLoad, myThreadNumber, iterationNumber, threadInt))
            t.start()
            time.sleep(30)
        except Exception, detail:
                print "ERROR:", detail
                print "########################RESTART######################"
                threadRestart(myFileNameSave, myFileNameLoad, myThreadNumber, iterationNumber, threadInt)

                

def threadRestart(myFileNameSave, myFileNameLoad, myThreadNumber, iterationNumber, threadInt):
    simpleScraper(myFileNameSave, myFileNameLoad, myThreadNumber, iterationNumber, threadInt)

def simpleScraper(myFileNameSave, myFileNameLoad, myThreadNumber, iterationNumber, threadInt):
    try:
        #driver = webdriver.PhantomJS()  
        driver = webdriver.Firefox()
        with open(myFileNameLoad, 'rb') as myList:
            myCSV = csv.reader(myList, delimiter=',', quotechar='|')
            for nameAndPostCode in itertools.islice(myCSV, iterationNumber, 10000):
                """
                try:
                    restartModuleFile = open("restartModuleFile.txt", 'a')
                    restartModuleFile.write(str(myThreadNumber))
                    restartModuleFile.write(",")
                    restartModuleFile.write(str(iterationNumber))
                    restartModuleFile.write("\n")
                    restartModuleFile.close()
                except Exception, detail:
                    print "ERROR:", detail
                    print "#############################FILE ERROR##############################"
                """
                #when using firefox driver for some reason need to reopen every time browser
                
                driver.implicitly_wait(5)
                driver.get("http://www.dastelefonbuch.de/")
                #driver.save_screenshot('screen.png') 
                nameButton = driver.find_element_by_xpath('//*[@id="what"]')
                plzButton = driver.find_element_by_xpath('//*[@id="where"]')
                submitButton = driver.find_element_by_xpath('//*[@id="searchButton"]') 

                originalName = nameAndPostCode[0].decode('latin-1')
                postCode = nameAndPostCode[1].decode('latin-1')
                
                nameButton.send_keys(originalName)
                plzButton.send_keys(postCode)
                driver.implicitly_wait(5)
                submitButton.click()
                driver.implicitly_wait(5)
                
                #There are 2 formatting ways used  on das telephone buch
                #MEDTHOD1

                nameText1a, numberText1a = getPhone1(driver)
                #print nameText1a, numberText1a 
                numberText1b = getPhone2(driver)
                #print numberText1b, "trace1"
                nameText1d, numberText1d = getPhone4(driver)
                #print nameText1d, numberText1d, "trace3"
                nameText2, numberText2, secondNameRun = secondName(driver)
                #print nameText2, numberText2, secondNameRun, "trace4"
                
                if len(numberText1a) > len(numberText1b) and len(numberText1d):
                    numberText1 = numberText1a
                elif len(numberText1b) > len(numberText1d):
                    numberText1 = numberText1b
                else:
                    numberText1 = numberText1d

                if len(nameText1a) > len(nameText1d):
                    nameText1 = nameText1a
                else:
                    nameText1 = nameText1d

                print myThreadNumber, nameText1, numberText1
                #print nameText2, numberText2
                
                """
                #nameArrayValues = [nameText1a, nameText1b, nameText1c, nameText1d]
                numberArrayValues = [numberText1a, numberText1b, numberText1c, numberText1d]

                numberArray = [len(numberText1a), len(numberText1b), len(numberText1c), len(numberText1d)]
                maxNumber = max(numberArray)

                for x in range (0, 4):
                    if numberArray[x]== maxNumber:
                        print numberArrayValues[x]
                        numberText1 = numberArrayValues[x]
                    else:
                        print "SOmethinks roeng"
                
                
                print myThreadNumber, nameText1a, numberText1
                
                nameText2, numberText2, secondNameRun = secondName(driver)

                if secondNameRun == False:
                    nameText2, numberText2, secondNameRun = secondName(driver)
                    #print nameText2, numberText2, secondNameRun

                #if numberText2 != "None":
                    #getRawData(driver)
                #MEDTHOD Raw Data
                """
                #driver.quit()
                    
                myWrite(iterationNumber, originalName, postCode, nameAndPostCode[2], nameText1, numberText1, nameText2, numberText2, myFileNameSave)
                iterationNumber = iterationNumber + 1
    except Exception, detail:
        print "############" + str(myThreadNumber) + "############"
        print "ERROR loading firefox"
        try:
            driver.quit()
        except:
            pass
        print "##############################################"
        
        time.sleep(random.randrange(10, 30, 1))
        threadRestart(myFileNameSave, myFileNameLoad, myThreadNumber, iterationNumber, threadInt)
        
        
def getRawData(driver):
    try:
        data = driver.find_element_by_xpath('//*[@id="content"]').text
        rawData = open("rawData.txt", 'a')    
        rawData.write(data.encode('latin-1'))
        rawData.close()
    except:
        pass
def getPhone1(driver):
    try:
        secondNameRun = False
        firstName = driver.find_element_by_xpath('//*[@id="entry_1"]/div[1]/a/span').text
        firstNumber = driver.find_element_by_xpath('//*[@id="entry_1"]/div[3]/div/span/span').text
    except:
        firstName = "NONM1"
        firstNumber = "None"
    return firstName, firstNumber
def getPhone2(driver):
    try:
        firstNumber = driver.find_element_by_xpath('//*[@id="entry_1"]/div[3]/div/span').text
    except:
        firstNumber = "None2"
    return firstNumber
def getPhone3(driver):
    try:
        firstNumber = driver.find_element_by_xpath('//*[@id="entry_1"]/div[3]').text
    except:
        firstNumber = "None3"
    return firstNumber

def getPhone4(driver):
    try:
        firstName = driver.find_element_by_xpath('//*[@id="entry_1"]/div[2]/div[1]/a/span').text
        firstNumber = driver.find_element_by_xpath('//*[@id="entry_1"]/div[2]/div[3]/span').text
    except:
        firstName = "NONM4"
        firstNumber = "None"
    return firstName, firstNumber
        
def secondName(driver):
    try:
        secondName = driver.find_element_by_xpath('//*[@id="entry_2"]/div[1]/a/span').text
        try:
            t1 = driver.find_element_by_xpath('//*[@id="entry_2"]/div[3]/div[2]/span').text
        except:
            t1 = ""
            pass
        try:
            t2 = driver.find_element_by_xpath('//*[@id="entry_2"]/div[3]/div/span/span').text
        except:
            t2 = ""
            pass
        if len(t1) > len(t2):
            secondNumber = t1
        else:
            secondNumber = t2
    except:
        secondName = "None"
        secondNumber = "None"
    secondNameRun = True

    return secondName, secondNumber, secondNameRun
    
            
def myWrite(iterationNumber, originalName, postCode, sortNumber, firstName, firstNumber, secondName, secondNumber, myFileNameSave):
    
    phoneList = open(myFileNameSave, 'a')
    #with codecs.open("newphonelist.txt", 'a', encoding='latin-1') as phoneList:    
    phoneList.write(str(iterationNumber))
    phoneList.write(",")
    phoneList.write(originalName.encode('latin-1'))
    phoneList.write(",")
    phoneList.write(postCode)
    phoneList.write(",")
    phoneList.write(sortNumber)
    phoneList.write(",")
    phoneList.write(firstName.encode('latin-1'))
    phoneList.write(",")
    phoneList.write(firstNumber)
    phoneList.write(",")
    phoneList.write(secondName.encode('latin-1'))
    phoneList.write(",")
    phoneList.write(secondNumber)
    phoneList.write("\n")
    phoneList.close()


################################ MULTI Thread Starter############################
def main():
    startx()
    #multiThreading()
    
def myFarmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber, currentRowInSearchList):
    farmThread = Farmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber, currentRowInSearchList)  

def multiThreading():
    for number in range (0, 3):
        
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
        self.numberOfProxiesInList = 200

        ##########Loads Proxy List into Array################
        proxyArray = [None] * 200
        proxyNumber = 0
        for x in range (0, 200):
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
        self.goodProxyNumber = self.myProxyListChecker(wantedProxyNumber)
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
        myProxy = self.myProxyArray[goodProxyNumber]
        #print "using proxy number " + str(useProxyNumber) + " " + str(myProxy[x])
        self.proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myProxy,
            'ftpProxy': myProxy,
            'sslProxy': myProxy,
            'noProxy': '' # set this value as desired
            })
        print "THREAD: " + str(self.threadNumber) + " Using proxy number: ["  + str(goodProxyNumber) + "] " + str(myProxy)
        logging.info("PROXY, loadGoogle: ," + str(self.threadNumber) + ", Using proxy number: ,"  + str(goodProxyNumber) + "," + str(myProxy) + "," + str(time.ctime()))
        self.browser = webdriver.Firefox(proxy=self.proxy)
        self.goFarm() 
    

    def goFarm(self):
        startRow = self.currentRowInSearchList
        for self.currentRowInSearchList in range (startRow, 3000):
            
            #######################Gets the Phone number from Goodle##################################
            with open(self.myFileNameLoad, 'rb') as self.myList:
                self.spamreader = csv.reader(self.myList, delimiter=',', quotechar='|')
                for row in itertools.islice(self.spamreader, self.farmNumber, self.farmNumber + 1):
                    self.myFirstString = ', '.join(row)
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
                        self.phoneNumber = self.browser.find_element_by_xpath('//*[@id="rhs_block"]/ol/li/div[1]/div/div[1]/ol/li[6]/div/div[2]/span[2]/span').text

                        ############################################
                        logging.info(str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone:," + str(self.phoneNumber) + "," + str(time.ctime()))
                        print str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone:," + str(self.phoneNumber) + "," +str(time.ctime())
                        ############################################
                        
                    except:
                        #No Phone, Bad proxy or Google capcha"
                        self.seleniumProxyChecker()
                        self.phoneNumber = "None"
                        
                        ############################################
                        print str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone: NONE," + str(time.ctime())
                        logging.info(str(self.threadNumber) + ",currentRowInSearchList: goFarm," + str(self.currentRowInSearchList) + ",Phone: NONE," + str(time.ctime()))
                        ############################################
                    
                    ############# Write phone number to Text file ##################
                    self.stringToWrite = ", " + self.phoneNumber + "\n"
                    self.xText = self.stringToWrite.encode('latin-1')
                    self.myFile = open(self.myFileNameSave, 'a')
                    self.myFile.write(str(self.farmNumber))
                    self.myFile.write(", ")
                    self.myFile.write(self.businessName)
                    self.myFile.write(self.xText)
                    
                    self.myFile.close()
                    #Clears the text and moves on to the next row
                    self.xText = ""
                    #################################################################
                    
                    
                    myNumber = random.randrange(5, 10, 1)
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

    ############################### USELESS METHODS ###############
    def getProxyLoop(self, x):
        while x < 20:
            if self.quickCheck(x):
                return self.getProxy(x)
                x = x + 1


    def getProxyLoop2(self, x):
        x = self.wantedProxyNumber
        if x < y:
            while self.quickCheck(x) == False or x > 20:
                if self.quickCheck(x):
                    return self.getProxy(x)
                else:
                    x = x + 1
        else:
            while self.quickCheck(y) == False or y > 20:
                if self.quickCheck(y):
                    return self.getProxy(y)
                else:
                    y = y + 1


    def getProxy(self, wantedProxyNumber):
        proxyArray = [None] * 100
        proxyNumber = 0
        for x in range (0, 100):
            with open('proxylist.csv', 'rb') as myList:
                proxyCSVObject = csv.reader(myList, delimiter=',', quotechar='|')
                for row in itertools.islice(proxyCSVObject, proxyNumber, proxyNumber + 1):
                    proxyLineInTextFile = ', '.join(row)
                    proxyArray[proxyNumber] = str(proxyLineInTextFile)
                    proxyNumber = proxyNumber + 1           
        return proxyArray[wantedProxyNumber]
    

    def myFarmer2(self):
        farmThread = Farmer(myFileName, myFileNameLoad, threadNumber, wantedProxyNumber)
        farmThread.goFarm()
    
            
    def seleniumProxyChecker2(self, currentRowInSearchList):
        if self.gotSlowConnection():
            print "gotSlowConnection"
            self.moveOnToNextProxy(currentRowInSearchList)
        elif self.gotBadProxy():
            print "gotBadProxy"
            self.moveOnToNextProxy(currentRowInSearchList)
        elif self.gotEbaniCaptcha():
            print "gotEbaniCaptcha"
            self.moveOnToNextProxy(currentRowInSearchList)    
                
    def gotSlowConnection(self):
        if "The connection has timed out" in self.browser.page_source:
            return True
        else:
            return False
    def gotBadProxy(self):
        if "The proxy server is refusing" in self.browser.page_source:
            return True
        else:
            return False
    def gotEbaniCaptcha(self):
        if "type the characters" in self.browser.page_source:
            return True
        else:
            return False
"""
  def seleniumProxyCheckerLong(self, currentRowInSearchList):
        if self.gotEbaniCaptcha():
            print "gotEbaniCaptcha"
            self.moveOnToNextProxy(currentRowInSearchList)
            return
        elif self.gotSlowConnection():
            print "gotSlowConnection"
            self.moveOnToNextProxy(currentRowInSearchList)
            return
        elif self.gotBadProxy():
            print "gotBadProxy"
            self.moveOnToNextProxy(currentRowInSearchList)
            return
        else:
            print "Simply no telephone :-) "
            pass
                
    def gotSlowConnection(self):
        if "The connection has timed out" in self.browser.page_source:
            return True
        else:
            return False
    def gotBadProxy(self):
        if "The proxy server is refusing" in self.browser.page_source:
            return True
        else:
            return False
    def gotEbaniCaptcha(self):
        if "type the characters" in self.browser.page_source:
            return True
        else:
            return False
"""

    #########################################################################
