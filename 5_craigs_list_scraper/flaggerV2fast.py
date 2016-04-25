# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import *
import threading
import time
import itertools
import random
import csv
import urllib2
import socket
import random
import logging
import sys
import codecs
import traceback
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

logging.basicConfig(level=logging.INFO, filename="flaggerScraper.log")

#Change this to the number of proxies in your list
numberOfProxiesInList = 500
proxyListName = "proxylist.csv"
myFileNameLoad = "flaglist.csv"


##########Loads Proxy List into Array################
proxyArray = [None] * numberOfProxiesInList
x = 0
with open(proxyListName, 'rb') as myList:
    proxyCSVObject = csv.reader(myList, delimiter=',', quotechar='|')
    for row in itertools.islice(proxyCSVObject, 0, numberOfProxiesInList):
        proxyArray[x] = str(row[0])
        #print proxyArray[x]
        x = x + 1

#####################################################


threadArray = ["Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10"]
#change the number corresponding to the thread, if you want for some reason to start at a different proxy number
proxyStartNumberArray = [10, 0, 0, 0, 5, 6, 7, 8, 9, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#choose to select the post to delete(it your flaglist.csv)
addFlagNumberArray = [0, 0, 0]

def main():
    multiThreading()

def multiThreading():
    for number in range (0, 1):
        
        try:
            print "multiThreading Started"
            myThreadNumber = threadArray[number]
            goodProxyNumber = proxyStartNumberArray[number]
            addFlagNumber = addFlagNumberArray[number]
            t = threading.Thread(target=startScraper, args = (myThreadNumber, goodProxyNumber, addFlagNumber))
            t.start()
            time.sleep(30)
        except Exception, detail:
                traceback.print_exc()
                print "ERROR:", detail
        
        
def startScraper(threadNumber, goodProxyNumber, addFlagNumber):
    print "Logfile Created"
    logging.info('Log file for ' + str(threadNumber) +  " " + str(time.ctime()))
    print "Starting Scraper"
    loadScraper(goodProxyNumber, addFlagNumber, threadNumber)


def loadScraper(goodProxyNumber, addFlagNumber, threadNumber):
    try:
        myProxy = proxyArray[goodProxyNumber]
        #print goodProxyNumber
        #print proxyArray[goodProxyNumber]
        #print "using proxy number " + str(useProxyNumber) + " " + str(myProxy[x])
        
        profile = webdriver.FirefoxProfile()
        #you can change the 0 to 2 to make things go quicker 
        profile.set_preference('permissions.default.stylesheet', 2)
        profile.set_preference('permissions.default.image', 2)

        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': myProxy,
            'ftpProxy': myProxy,
            'sslProxy': myProxy,
            'noProxy': '' # set this value as desired
            })
        print "THREAD: " + str(threadNumber) + " Using proxy number: ["  + str(goodProxyNumber) + "] " + str(myProxy)
        logging.info("PROXY, loadGoogle: ," + str(threadNumber) + ", Using proxy number: ,"  + str(goodProxyNumber) + "," + str(myProxy) + "," + str(time.ctime()))
        browser = webdriver.Firefox(proxy=proxy, firefox_profile=profile)
        
        goFarm(browser, goodProxyNumber, addFlagNumber, threadNumber)
    except:
        time.sleep(15)
        traceback.print_exc()
        print "######################RESTARTING " + threadNumber +" #######################"
        #think about putting proxy advance here goodProxyNumber = goodProxyNumber + 1
        try:
            browser.quit()
        except:
            pass
        startScraper(threadNumber, goodProxyNumber, addFlagNumber)
        

def goFarm(browser, goodProxyNumber, addFlagNumber, threadNumber):
    startAddFlag = addFlagNumber
    endAddFlag = addFlagNumber + 1
    
    with open(myFileNameLoad, 'rb') as myList:
        myAddToBeFlaggedList = csv.reader(myList, delimiter=',', quotechar='|')
        for addToBeFlagged in itertools.islice(myAddToBeFlaggedList, startAddFlag, endAddFlag):
            addToBeFlaggedString = addToBeFlagged[0]
            #print addToBeFlaggedString
            try:
                #browser.implicitly_wait(20)
                try:
                    browser.set_page_load_timeout(12)
                    browser.get(addToBeFlaggedString)
                except:
                    pass
                time.sleep(1)
                seleniumProxyChecker(browser, goodProxyNumber, addFlagNumber, threadNumber)

            except:
                ###################
                print "Proxy too not working, moving to next proxy"
                #logging.info(str(threadNumber) + ",Proxy too slow goFarm," + "," + str(time.ctime()))
                ###################
                moveOnToNextProxy(browser, goodProxyNumber, addFlagNumber, threadNumber)
            try:

                prohibitedButton = browser.find_elements_by_xpath('//*[@id="pagecontainer"]/section/header/aside/a/span[2]')[0]
                action = webdriver.common.action_chains.ActionChains(browser)
                action.move_to_element_with_offset(prohibitedButton, 5, 5)
                action.click()
                action.perform()
                
                time.sleep(2)
                #print str(threadNumber) + ": Using proxy number: ["  + str(goodProxyNumber) + "] " + str(myProxy) + " Button Pressed"
                time.sleep(10)

                moveOnToNextProxy(browser, goodProxyNumber, addFlagNumber, threadNumber)
                
            except:
                traceback.print_exc()
                ###############################
                print "Problem Loading Google"
                #logging.info(str(threadNumber) + ",Problem loading google goFarm," + str(time.ctime()))
                ###############################
                moveOnToNextProxy(browser, goodProxyNumber, addFlagNumber, threadNumber)
              
def moveOnToNextProxy(browser, goodProxyNumber, addFlagNumber, threadNumber):
    browser.quit()
    myNumber = random.randrange(2, 5, 1)
    time.sleep(myNumber)
    goodProxyNumber = goodProxyNumber + 1
    loadScraper(goodProxyNumber, addFlagNumber, threadNumber)
    time.sleep(2)

def seleniumProxyChecker(browser, goodProxyNumber, addFlagNumber, threadNumber):
    "Selenium Proxy checker..."
    errorSource = browser.page_source
    if "This IP has been automatically blocked" in errorSource:
        ##############
        print "Craigs List has blocked this proxy"
        ##############
        moveOnToNextProxy(browser, goodProxyNumber, addFlagNumber, threadNumber)
    else:
        pass
    
    
'''
###################Selenium Proxy Checker########################

def seleniumProxyChecker():
    errorSource = browser.page_source
    if "The connection has timed out" in errorSource:
        ##############
        print "gotSlowConnection"
        logging.info("SELENIUM_PROXY_CHECKER," + str(threadNumber) + ",gotSlowConnection," + str(time.ctime()))
        ##############
        moveOnToNextProxy()
    elif "The proxy server is refusing" in errorSource:
        ##############
        print "gotBadProxy"
        logging.info("SELENIUM_PROXY_CHECKER," + str(threadNumber) + ",gotBadProxy," + str(time.ctime()))
        ##############
        moveOnToNextProxy()
    elif "type the characters" in errorSource:
        ##############
        print "gotEbaniCaptcha"
        logging.info("SELENIUM_PROXY_CHECKER," + str(threadNumber) + ",gotEbaniCaptcha," + str(time.ctime()))
        ##############
        moveOnToNextProxy()
    elif "computer or network may be sending" in errorSource:
        ##############
        print "GOOGLE BAN"
        logging.info("SELENIUM_PROXY_CHECKER," + str(threadNumber) + ",GOOGLEBAN," + str(time.ctime()))
        ##############
        moveOnToNextProxy()
    elif "Our systems have detected unusual traffic from your computer" in errorSource:
         ##############
        print "GOOGLE BAN 2"
        logging.info("SELENIUM_PROXY_CHECKER," + str(threadNumber) + ",GOOGLEBAN 2," + str(time.ctime()))
        ##############
        moveOnToNextProxy()
        
    else:
        #print "Simply no telephone :-) "
        pass


###################URLLIB Proxy Checker########################

                 
def myProxyListChecker(proxBeingChecked, threadNumber):
    if proxBeingChecked >= numberOfProxiesInList:
        proxBeingChecked = 1
        print "proxy List Finished Starting at the beginning"
        logging.info("PROXY, myProxyListChecker: ," + str(threadNumber) + ",LIST FINNISHED starting at beginning")
    while proxBeingChecked < numberOfProxiesInList:
        if quickCheck(proxBeingChecked):
            logging.info("PROXY, myProxyListChecker: ," + str(threadNumber) + ",USING PROXY: ," + str(x))
            return proxBeingChecked
        else:
            proxBeingChecked = proxBeingChecked + 1
    

def is_bad_proxy(pip):    
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

def quickCheck(wantedProxyNumber):
    
    socket.setdefaulttimeout(60)
    currentProxy = myProxyArray[wantedProxyNumber]
    
    if is_bad_proxy(currentProxy):
        #print "Bad Proxy %s" % (currentProxy)
        return False
    else:
        #print "%s is working" % (currentProxy)
        #return True
        return currentProxy

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

'''


if __name__ == '__main__':
    main()

 
