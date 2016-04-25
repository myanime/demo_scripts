# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import traceback
import itertools
import csv
import codecs
import time
import random
import threading

#listType = "people"
listType = "company"

searchEngine = "DUCK"

if searchEngine == "BING":
    engineURL = "http://www.bing.de"
    inputBox = '//*[@id="sb_form_q"]'
    searchButon = '//*[@id="sb_form_go"]'
    firstElement = '//*[@id="b_results"]/li[1]/div[1]/h2/a'
elif searchEngine == "GOOGLE":
    engineURL = "http://www.google.de"
    inputBox = '//*[@id="lst-ib"]'
    searchButon = '//*[@id="sblsbb"]/button/span'
    firstElement = '//*[@id="rso"]/div/div[1]/div/h3/a'
elif searchEngine == "DUCK":
    engineURL = 'https://duckduckgo.com/'
    inputBox = '//*[@id="search_form_input_homepage"]'
    searchButon = '//*[@id="search_button_homepage"]'
    firstElement = '//*[@id="r1-0"]/div/h2/a[1]'
######
papka = 7
thread1start = 5000 * papka
myInterval = 5000
thread2start = 10000
########
if listType == "people":
    listLoad = "myListPeople.csv"
else:
    listLoad = "myListCompany.csv"

listNumber = ["Thread_1", "Thread_2"]
startArray = [thread1start, thread2start]


def main():
    multiThreading()


def searchChecker(browser):
    return False
'''
    if searchEngine == "GOOGLE":
        errorSource = browser.page_source
        if "Achten Sie darauf," in errorSource:
            ##############
            print "No info found on google.com"
            ##############
            myWait = random.randrange(1, 3, 1)
            time.sleep(myWait)
            return True
        else:
            return False
        
    elif searchEngine == "DUCK":
        errorSource = browser.page_source
        if "No more results." in errorSource:
            ##############
            print "No info found on duck"
            ##############
            myWait = random.randrange(1, 3, 1)
            time.sleep(myWait)
            return True
        else:
            return False
    else:
        return False
'''
    
  
def multiThreading():
    for number in range (0, 1):
        
        try:
            print "multiThreading Started"
            myFileNameLoad = listLoad
            myThreadNumber = listNumber[number]
            myStart = startArray[number]
            myStop = myStart + myInterval
            modifier = "_" + str(myStart) + "-" + str(myStop)
            myFileNameSave = myThreadNumber + searchEngine + modifier + "scrapedList.csv"
            t = threading.Thread(target=getURL, args = (myFileNameSave, myFileNameLoad, myThreadNumber, myStart, myStop))
            t.start()
            time.sleep(60)
        except Exception, detail:
                print "ERROR:", detail

def errorLog(company):
    try:
        with open ("error.log", "a") as file:
            file.write(company[0])
            file.write("~")
            file.write(company[1])
            file.write("~")
            file.write(company[2])
            file.write("~")
            file.write(company[3])
            file.write("~")
            file.write(company[4])
            file.write("~")
            file.write(company[5])
            file.write("~")
            file.write(company[6])
            if listType == "company":
                file.write("~")
                file.write(company[7])
                file.write("~")
                file.write(company[8])
                file.write("~")
                file.write(company[9])
                file.write("~")
                file.write(company[10])
                file.write("~")
                file.write(company[11])
                file.write("~")
                file.write(company[12])
                file.write("~")
                file.write(company[13])
                file.write("\n")
            else:
                file.write("\n")
    except:
        traceback.print_exc()
        time.sleep(5)
        
def getURL(myFileNameSave, myFileNameLoad, myThreadNumber, myStart, myStop):
    driver = webdriver.Firefox()
    finishFlag = 1
    with open (myFileNameLoad, 'rb') as searchList:
        myCSV = csv.reader(searchList, delimiter='|', quotechar='"')
        start = myStart
        stop = myStop
        for company in itertools.islice(myCSV, start, stop):
            finishFlag = 1
            try:
                time.sleep(1)
                text = company[3].decode('utf-8')
                driver.implicitly_wait(20)
                time.sleep(.3)
                driver.get(engineURL)
                time.sleep(.3)
                searchbox = driver.find_element_by_xpath(inputBox)
                searchbox.send_keys(text + " site:http://www.firmenwissen.de/")
                time.sleep(1)
                driver.find_element_by_xpath(searchButon).click()
                time.sleep(1.5)
                if searchChecker(driver) != True:
                    driver.implicitly_wait(20)
                    try:
                        driver.find_element_by_xpath(firstElement).click()
                    except:
                        if finishFlag == 1:
                            errorLog(company)
                            start = start + 1
                            finishFlag = 0
                        else:
                            pass
                    time.sleep(2)
                    urlText = driver.current_url
                    #print str(start) + ": " + urlText
                    
                    try:
                        name = '//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/h1'
                        address = '//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[1]'
                        telephone = '//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]'
                        
                        nameText = driver.find_element_by_xpath(name).text
                        addressText = driver.find_element_by_xpath(address).text
                        telephoneText = driver.find_element_by_xpath(telephone).text


                        try:
                            searchbox = driver.find_element_by_xpath('//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]/a')
                            searchbox.click()
                            email = driver.find_element_by_xpath('//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]/a').text
                            myWait = random.randrange(1, 2, 1)
                            time.sleep(myWait)
                            #print str(start) +": " + email + " wait: " + str(myWait)
                        except:
                            myWait = random.randrange(1, 2, 1)
                            time.sleep(myWait)
                            #print str(start) +": " + "No email" + " wait: " + str(myWait)
                            email = "None"

                        with open (myFileNameSave, "a") as file:
                            file.write(company[0])
                            file.write("~")
                            file.write(company[1])
                            file.write("~")
                            file.write(company[2])
                            file.write("~")
                            file.write(company[3])
                            file.write("~")
                            file.write(company[4])
                            file.write("~")
                            file.write(company[5])
                            file.write("~")
                            file.write(company[6])
                            if listType == "company":
                                file.write("~")
                                file.write(company[7])
                                file.write("~")
                                file.write(company[8])
                                file.write("~")
                                file.write(company[9])
                                file.write("~")
                                file.write(company[10])
                                file.write("~")
                                file.write(company[11])
                                file.write("~")
                                file.write(company[12])
                                file.write("~")
                                file.write(company[13])
                            file.write("~")
                            file.write(urlText.encode('utf-8'))
                            file.write("~")
                            file.write(email.encode('utf-8'))
                            file.write("~")
                            file.write(nameText.encode('utf-8'))
                            file.write("~")
                            file.write('*')
                            file.write(addressText.encode('utf-8'))
                            file.write('*')
                            file.write("~")
                            file.write('*')
                            file.write(telephoneText.encode('utf-8'))
                            file.write('*')
                            file.write("\n")
                            print myThreadNumber + ": " + str(start)
                            start = start + 1
                    except:
                        if finishFlag == 1:
                            errorLog(company)
                            start = start + 1
                            finishFlag = 0
                        else:
                            pass
                else:
                    if finishFlag == 1:
                        errorLog(company)
                        start = start + 1
                        finishFlag = 0
                    else:
                        pass
            except:
                traceback.print_exc()
                time.sleep(5)
                driver.quit()
                if finishFlag == 1:
                    errorLog(company)
                    start = start + 1
                    finishFlag = 0
                else:
                    pass
                getURL(myFileNameSave, myFileNameLoad, myThreadNumber, start, myStop)
                
if __name__ == '__main__':
    main()

                
