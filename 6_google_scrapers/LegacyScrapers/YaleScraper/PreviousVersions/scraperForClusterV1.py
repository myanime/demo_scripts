#CHANGE LINE 287, 425, change main method and check your urls in splitURLS
# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import time
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import threading
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
#import logging

#You get a log output with all your URLS, which you then copy and paste to your scraper.
#logging.basicConfig(level=logging.INFO, filename="myLog.log")

##############################################################
###############CHANGE THESE VALUES ###########################
##############################################################

#This is probably what you were looking for yesterday, sorry this is taking so long
#YOu can scrape everything, or selected states.

#To get your interval for a state, set your stateNumber and set myStartPage to 0 and myEndPage to 1. Then run multiThreading
#This will open a single search. Check how many pages there are. For maryland there were 989. I want to run 5 browsers,
#so i put the interval at 200, going from 0 to 5. (Its starts at 0, and goes to 5, ie 0, 1, 2, 3, 4
# this will give me 1000 pages, 4*200 = 800, and it scrapes from 800 to 1000
#after you know your interval, put it in, and change your myEndPage to what you want, then read the instructions in main()

#NB I set up a new folder path - everything from this scraper will download to .../2_SummerPaper/Data/myScraper/selectedState/

myStartPage = 0 
myEndPage = 30
#If you restart and 100 pages have already been downloaded change the interval to 100
myInterval = 1000
apple = False

#If you want to select all states change to True
selectAllStates = True

stateNumber = None
state2 = None
state3 = None
state4 = None
state5 = None
state6 = None
state7 = None
state8 = None
state9 = None
state10 = None
state11 = None
state12 = None
state13 = None
state14 = None
state15 = None
state16 = None
state17 = None
state18 = None
state19 = None
state20 = None


#For All states change this to None
#stateNumber = None

##############################################################
##############################################################
##############################################################


#################################################################
def main():
    #Instructions: First run getUrl. Copy the URLs. Then Run the mainHelper, paste the output into the header space below
    #Copy your URLs that you just got to the splitURLS sections. Now run the createFolders. Then the multiThreading.
    #You only have to change the values above. I  have included checkURL just incase, you dont really have to run it
    #getURL()
    #mainHelper()
    createFolders()
    multiThreading()
    #checkURL()

    
#################################################################

################################## HEADER ##################################

directoryArray = [\
"/home/shuzhang/researchScraper/NoState/0",\
"/home/shuzhang/researchScraper/NoState/1000",\
"/home/shuzhang/researchScraper/NoState/2000",\
"/home/shuzhang/researchScraper/NoState/3000",\
"/home/shuzhang/researchScraper/NoState/4000",\
"/home/shuzhang/researchScraper/NoState/5000",\
"/home/shuzhang/researchScraper/NoState/6000",\
"/home/shuzhang/researchScraper/NoState/7000",\
"/home/shuzhang/researchScraper/NoState/8000",\
"/home/shuzhang/researchScraper/NoState/9000",\
"/home/shuzhang/researchScraper/NoState/10000",\
"/home/shuzhang/researchScraper/NoState/11000",\
"/home/shuzhang/researchScraper/NoState/12000",\
"/home/shuzhang/researchScraper/NoState/13000",\
"/home/shuzhang/researchScraper/NoState/14000",\
"/home/shuzhang/researchScraper/NoState/15000",\
"/home/shuzhang/researchScraper/NoState/16000",\
"/home/shuzhang/researchScraper/NoState/17000",\
"/home/shuzhang/researchScraper/NoState/18000",\
"/home/shuzhang/researchScraper/NoState/19000",\
"/home/shuzhang/researchScraper/NoState/20000",\
"/home/shuzhang/researchScraper/NoState/21000",\
"/home/shuzhang/researchScraper/NoState/22000",\
"/home/shuzhang/researchScraper/NoState/23000",\
"/home/shuzhang/researchScraper/NoState/24000",\
"/home/shuzhang/researchScraper/NoState/25000",\
"/home/shuzhang/researchScraper/NoState/26000",\
"/home/shuzhang/researchScraper/NoState/27000",\
"/home/shuzhang/researchScraper/NoState/28000",\
"/home/shuzhang/researchScraper/NoState/29000",\
"/home/shuzhang/researchScraper/NoState/30000",\
"/home/shuzhang/researchScraper/NoState/31000",\
"/home/shuzhang/researchScraper/NoState/32000",\
"/home/shuzhang/researchScraper/NoState/33000",\
"/home/shuzhang/researchScraper/NoState/34000",\
"/home/shuzhang/researchScraper/NoState/35000",\
"/home/shuzhang/researchScraper/NoState/36000",\
"/home/shuzhang/researchScraper/NoState/37000",\
"/home/shuzhang/researchScraper/NoState/38000",\
"/home/shuzhang/researchScraper/NoState/39000",\
"/home/shuzhang/researchScraper/NoState/40000",\
"/home/shuzhang/researchScraper/NoState/41000",\
"/home/shuzhang/researchScraper/NoState/42000",\
"/home/shuzhang/researchScraper/NoState/43000",\
"/home/shuzhang/researchScraper/NoState/44000",\
"/home/shuzhang/researchScraper/NoState/45000",\
"/home/shuzhang/researchScraper/NoState/46000",\
"/home/shuzhang/researchScraper/NoState/47000",\
"/home/shuzhang/researchScraper/NoState/48000",\
"/home/shuzhang/researchScraper/NoState/49000",\
"/home/shuzhang/researchScraper/NoState/50000",\
"/home/shuzhang/researchScraper/NoState/51000",\
"/home/shuzhang/researchScraper/NoState/52000",\
"/home/shuzhang/researchScraper/NoState/53000",\
"/home/shuzhang/researchScraper/NoState/54000",\
"/home/shuzhang/researchScraper/NoState/55000",\
"/home/shuzhang/researchScraper/NoState/56000",\
"/home/shuzhang/researchScraper/NoState/57000",\
"/home/shuzhang/researchScraper/NoState/58000",\
"/home/shuzhang/researchScraper/NoState/59000",\
]

listNumber = ["Thread 0", "Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25", "Thread 26", "Thread 27", "Thread 28", "Thread 29", "Thread 30", "Thread 31", "Thread 32", "Thread 33", "Thread 34", "Thread 35", "Thread 36", "Thread 37", "Thread 38", "Thread 39", "Thread 40", "Thread 41", "Thread 42", "Thread 43", "Thread 44", "Thread 45", "Thread 46", "Thread 47", "Thread 48", "Thread 49", "Thread 50", "Thread 51", "Thread 52", "Thread 53", "Thread 54", "Thread 55", "Thread 56", "Thread 57", "Thread 58", "Thread 59"]

myCurrentPage = [\
#0
0,\
#1
1000,\
#2
2000,\
#3
3000,\
#4
4000,\
#5
5000,\
#6
6000,\
#7
7000,\
#8
8000,\
#9
9000,\
#10
10000,\
#11
11000,\
#12
12000,\
#13
13000,\
#14
14000,\
#15
15000,\
#16
16000,\
#17
17000,\
#18
18000,\
#19
19000,\
#20
20000,\
#21
21000,\
#22
22000,\
#23
23000,\
#24
24000,\
#25
25000,\
#26
26000,\
#27
27000,\
#28
28000,\
#29
29000,\
#30
30000,\
#31
31000,\
#32
32000,\
#33
33000,\
#34
34000,\
#35
35000,\
#36
36000,\
#37
37000,\
#38
38000,\
#39
39000,\
#40
40000,\
#41
41000,\
#42
42000,\
#43
43000,\
#44
44000,\
#45
45000,\
#46
46000,\
#47
47000,\
#48
48000,\
#49
49000,\
#50
50000,\
#51
51000,\
#52
52000,\
#53
53000,\
#54
54000,\
#55
55000,\
#56
56000,\
#57
57000,\
#58
58000,\
#59
59000,\
]

splitURLS = [\
#1
"http://referenceusa.com/UsHistoricalBusiness/Result/f3e7cabe03f04c7a9adc125071aba8b4",\
#1000
"http://referenceusa.com/UsHistoricalBusiness/Result/7be6dd3caec84c45b4ca8e62243b4a9c",\
#2000
"http://referenceusa.com/UsHistoricalBusiness/Result/2921a00485864468aafcae03bcddb77e",\
#3000
"http://referenceusa.com/UsHistoricalBusiness/Result/4d450b158b064cb0adce1890c29abeca",\
#4000
"http://referenceusa.com/UsHistoricalBusiness/Result/dbc997741756454f8eee6324a8e04e25",\
#5000
"http://referenceusa.com/UsHistoricalBusiness/Result/8351f8b81c15450b849b9aab09338142",\
#6000
"http://referenceusa.com/UsHistoricalBusiness/Result/d8550f4003d64b97891c69ebeb5f5d72",\
#7000
"http://referenceusa.com/UsHistoricalBusiness/Result/6be59ce2e8e54728ac27ca7de48dc753",\
#8000
"http://referenceusa.com/UsHistoricalBusiness/Result/b3e7811deddf4617a0ce21b79cb79a19",\
#9000
"http://referenceusa.com/UsHistoricalBusiness/Result/a9e2ef72344b48878a127115ae1d2966",\
#10000
"http://referenceusa.com/UsHistoricalBusiness/Result/6666c1bbde9347358e9118ea67d82d7d",\
#11000
"http://referenceusa.com/UsHistoricalBusiness/Result/a48c2c3bf0a442499fdf8bc33d7c2bd6",\
#12000
"http://referenceusa.com/UsHistoricalBusiness/Result/cb3f86c5b67e4d11a250c9e2db29635d",\
#13000
"http://referenceusa.com/UsHistoricalBusiness/Result/0b403e0c0f67493182a22c0a7895c7f5",\
#14000
"http://referenceusa.com/UsHistoricalBusiness/Result/b835fd5f85da45eca80735ea8460ffee",\
#15000
"http://referenceusa.com/UsHistoricalBusiness/Result/a310e7f03bfc4abe99acbad1948cb072",\
#16000
"http://referenceusa.com/UsHistoricalBusiness/Result/4909778847b34543b76111e13195a8ef",\
#17000
"http://referenceusa.com/UsHistoricalBusiness/Result/9bd9dae996a7406e8389d75a8cd3a754",\
#18000
"http://referenceusa.com/UsHistoricalBusiness/Result/6026494737244546bd55c576d78f9b83",\
#19000
"http://referenceusa.com/UsHistoricalBusiness/Result/9bad3e96f9d94efabfb1340d2d554a8a",\
#20000
"http://referenceusa.com/UsHistoricalBusiness/Result/d0c019acf91d475eb1344952690f9ad3",\
#21000
"http://referenceusa.com/UsHistoricalBusiness/Result/2d929c15a9bb419d94ce7ccfe1bdc724",\
#22000
"http://referenceusa.com/UsHistoricalBusiness/Result/01a7751d287e422fa1c8db2af7b6c424",\
#23000
"http://referenceusa.com/UsHistoricalBusiness/Result/a1a87df265d5402f85cb1b883ec84faa",\
#24000
"http://referenceusa.com/UsHistoricalBusiness/Result/fbc619abe31b4cd4bc5a109e2545aecb",\
#25000
"http://referenceusa.com/UsHistoricalBusiness/Result/ccbb049ba8f04d3a8c24a0297cfd2936",\
#26000
"http://referenceusa.com/UsHistoricalBusiness/Result/376d9bded5dc47fa992cc41368f35842",\
#27000
"http://referenceusa.com/UsHistoricalBusiness/Result/c46d0fab2f2e46309cf2786c02ec517a",\
#28000
"http://referenceusa.com/UsHistoricalBusiness/Result/ac45af76adee4a7b8f328c54a1998356",\
#29000
"http://referenceusa.com/UsHistoricalBusiness/Result/5e49732fac7a48f394833e2b780b4a8e",\
#30000
"http://referenceusa.com/UsHistoricalBusiness/Result/62caf17700d54b0bab7cf2d2c6ce4b83",\
#31000
"http://referenceusa.com/UsHistoricalBusiness/Result/426a03046b8448978a4606e39db91ccf",\
#32000
"http://referenceusa.com/UsHistoricalBusiness/Result/f61f75f9406847118a991a4a188ada47"]

############################# End of HEADER ##################################

myFileNameSave = "./ALLPageNumber_"

def createFolders():
    try:
        for x in range (myStartPage, myEndPage):
            if not os.path.exists(directoryArray[x]):
                os.makedirs(directoryArray[x])
            print "Made"
    except:
        pass

def multiThreading():
    for number in range (myStartPage, myEndPage):
        try:
            threadEndPage = myCurrentPage[number] + myInterval + 50
            myThreadNumber = listNumber[number]
            searchURL = splitURLS[number] 
            currentPage = myCurrentPage[number]
            SAVE_TO_DIRECTORY = directoryArray[number]
            t = threading.Thread(target=yaleScraper, args = (searchURL, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage))
            t.start()
            print myThreadNumber + ": multiThreading Started"
            time.sleep(60)
        except Exception, detail:
                print "ERROR:", detail

def csvRenamer(currentPage, SAVE_TO_DIRECTORY):
    pass
    '''
    os.chdir(SAVE_TO_DIRECTORY)
    renameName = myFileNameSave + str(currentPage)
    files = filter(os.path.isfile, os.listdir(SAVE_TO_DIRECTORY))
    files = [os.path.join(SAVE_TO_DIRECTORY, f) for f in files]
    files.sort(key=lambda x: os.path.getmtime(x))
    newest_file = files[-1]
    os.rename(newest_file, renameName+".csv")
    '''
    
def resetList(browser, currentPage):
    time.sleep(15)                            
    refineSearch = browser.find_element_by_xpath('//*[@id="dbSelector"]/div/div[2]/div[1]/ul[2]/li[1]/a')
    refineSearch.click()
    time.sleep(15)

    greenSearchButton = '//*[@id="dbSelector"]/div/div[2]/div[1]/div[3]/div/a[1]'
    browser.find_element_by_xpath(greenSearchButton).click()
    time.sleep(30)
    try:
        numberBox = browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[2]')
        action = webdriver.common.action_chains.ActionChains(browser)
        action.move_to_element_with_offset(numberBox, 5, 5)
        action.click()
        action.send_keys(str(currentPage))
        action.send_keys(Keys.RETURN)
        action.perform()
        time.sleep(15)
    except:
        print "########################################ERROR RESETTING PAGE: Restarting #############################"
        time.sleep(20)
        try:
            browser.quit()
        except:
            pass
        yaleScraper(searchURL, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage)
    
    
def yaleScraper(searchURL, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage):
    #time.sleep(15)
    print myThreadNumber + ",CurrentPage:," + str(currentPage) + "\n"
    try:
        
        fp = webdriver.FirefoxProfile()
        fp.set_preference("browser.download.folderList",2)
        fp.set_preference("browser.download.manager.showWhenStarting",False)
        fp.set_preference("browser.download.dir", SAVE_TO_DIRECTORY)
        fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/comma-separated-values")

        browser = webdriver.Firefox(firefox_profile=fp)

        browser.implicitly_wait(20)

        browser.get(searchURL)
        time.sleep(5)
        resetList(browser, currentPage)
        time.sleep(5)
        listCheckbox = browser.find_element_by_xpath('//*[@id="checkboxCol"]')
        if listCheckbox.is_selected() == False:
                listCheckbox.click()
        else:
            print myThreadNumber + ":Allready clicked checkbox"
        time.sleep(10)

        browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/ul/li[5]/a').click()
        browser.find_element_by_xpath('//*[@id="detailDetail"]').click()
        browser.find_element_by_xpath('//*[@id="downloadForm"]/div[2]/a[1]/span/span').click()
        time.sleep(10)
        #//*[@id="dbSelector"]/div/div[2]/div[1]/ul/li[1]/a
        #csvRenamer(currentPage, SAVE_TO_DIRECTORY)
        currentPage = currentPage + 1
        
        for currentPage in range (currentPage, threadEndPage):
            time.sleep(1)
            print myThreadNumber + ",CurrentPage:" + str(currentPage) + "\n"
            browser.implicitly_wait(10)
            browser.get(searchURL)
            
            time.sleep(20)
            listCheckbox = browser.find_element_by_xpath('//*[@id="checkboxCol"]')
            if listCheckbox.is_selected() == True:
                time.sleep(5)
                listCheckbox.click()
                #double checks the checkbox was checked
                listCheckbox = browser.find_element_by_xpath('//*[@id="checkboxCol"]')
                if listCheckbox.is_selected() == True:
                    print "THE CHECKBOX WAS NOT DESELECTED"
                    time.sleep(5)
                    listCheckbox.click()
            else:
                print myThreadNumber + "The checkbox is taking a little longer than usual to load..."
                time.sleep(18)
                listCheckbox = browser.find_element_by_xpath('//*[@id="checkboxCol"]')
                if listCheckbox.is_selected() == True:
                    listCheckbox.click()
                else:
                    print myThreadNumber + ":The checkbox is already inactive"
                    resetList(browser, currentPage)
                    browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[1]').click()
                    
                    time.sleep(15)
                    
            time.sleep(4)
            
            browser.implicitly_wait(1)
            #moves to next page
            browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[3]').click()
            #This was the problem 
            time.sleep(25)
            listCheckbox = browser.find_element_by_xpath('//*[@id="checkboxCol"]')
            if listCheckbox.is_selected() == False:
                listCheckbox.click()
            else:
                print myThreadNumber + ":Allready clicked checkbox"
                resetList(browser, currentPage)
            time.sleep(1)
            
            browser.implicitly_wait(10)
            browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/ul/li[5]/a').click()
            browser.find_element_by_xpath('//*[@id="detailDetail"]').click()
            browser.find_element_by_xpath('//*[@id="downloadForm"]/div[2]/a[1]/span/span').click()
            time.sleep(1)
            #csvRenamer(currentPage, SAVE_TO_DIRECTORY)            
    except Exception, detail:
        print "ERROR:", detail
        #logging.info(myThreadNumber)
        #logging.info(currentPage)
        time.sleep(20)
        try:
            browser.quit()
        except:
            pass
        #currentPage = currentPage + 1
        yaleScraper(searchURL, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage)



def checkURL():
    driver = webdriver.Firefox()
    for x in range (myStartPage, myEndPage):
        driver.get(splitURLS[x])
        body = driver.find_element_by_tag_name("body")
        if apple == True:
            body.send_keys(Keys.COMMAND + 't')
        else:
            body.send_keys(Keys.CONTROL + 't')
        print "opened tab"
    print "Finished"


def autoCreateCommands(driver, startNumber, base_url):
    if startNumber == 0:
        startNumber = startNumber + 1
    driver.get(base_url)
    time.sleep(20)
    USHistoricalBusiness ='//*[@id="dbSelector"]/div/ul/li[2]/h5'
    driver.find_element_by_xpath(USHistoricalBusiness).click()
    time.sleep(2)
    driver.find_element_by_link_text("Custom Search").click()
    time.sleep(6)
    driver.find_element_by_id("cs-YellowPageHeadingOrSic").click()
    time.sleep(6)
    
    ####################################################
    if selectAllStates == False:
        if stateNumber != None:
            driver.find_element_by_id("cs-State").click()
            time.sleep(3)
            selectState = '//*[@id="availableState"]/ul/li[' + str(stateNumber) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(2)
        if state2 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state2) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state3 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state3) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state4 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state4) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state5 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state5) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state6 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state6) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state7 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state7) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state8 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state8) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state9 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state9) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state10 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state10) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state11 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state11) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state12 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state12) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state13 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state13) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state14 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state14) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state15 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state15) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state16 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state16) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state17 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state17) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state18 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state18) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state19 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state19) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(1)
        if state20 != None:
            selectState = '//*[@id="availableState"]/ul/li[' + str(state120) +']'
            driver.find_element_by_xpath(selectState).click()
            time.sleep(5)
    

    ##################################################

    driver.find_element_by_id("naicsOptionId").click()
    driver.find_element_by_id("naicsLookupKeyword").clear()
    #You can play arround with this to create different searches
    driver.find_element_by_id("naicsLookupKeyword").send_keys("72251")
    time.sleep(5)
    
    el = driver.find_elements_by_xpath("//div[@id='naicsKeyword']/ul/li[2]/span")[0]
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 5, 5)
    action.click()
    action.perform()
    
    el = driver.find_elements_by_xpath("//div[@id='naicsKeyword']/ul/li[3]/span")[0]
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 5, 5)
    action.click()
    action.perform()

    el = driver.find_elements_by_xpath("//div[@id='naicsKeyword']/ul/li[4]/span")[0]
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(el, 5, 5)
    action.click()
    action.perform()

    greenSearchButton = '//*[@id="dbSelector"]/div/div[2]/div[1]/div[3]/div/a[1]'
    driver.find_element_by_xpath(greenSearchButton).click()
    
    time.sleep(25)
    try:
        numberBox = driver.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[2]')
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(numberBox, 5, 5)
        action.click()
        #this is what sends the keys to the numberbox - it depends on what is sent to it by the autocreate method (thats where startNumber comes from
        action.send_keys(str(startNumber))
        action.send_keys(Keys.RETURN)
        action.perform()
    except:
        print "######################ERROR SETTING UP PAGE###########################"
        pass
    
    time.sleep(5)
    body = driver.find_element_by_tag_name("body")
    urlText = driver.current_url
    #logging.info('"' + str(urlText) +  '",')
    endPageNumber = driver.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[1]/span[2]').text
    if apple == True:
        body.send_keys(Keys.COMMAND + 't')
    else:
        body.send_keys(Keys.CONTROL + 't')

    print "#" + str(startNumber) 
    print '"' + urlText + '",\\'
    

def getURL():
    driver = webdriver.Firefox()
    myNewStartPage = myStartPage
    if myStartPage == 0:
        myNewStartPage = 1
        searchURL = autoCreateCommands(driver, 1, "http://referenceusa.com/")
        
    for x in range (myNewStartPage, myEndPage):
        y = x * myInterval
        
        searchURL = autoCreateCommands(driver, y, "http://referenceusa.com/")

def mainHelper():
    if stateNumber != None:
        fulltext = ""
        print 'directoryArray = [\\'
        if myStartPage < 100:
                #print '"/Users/shuzhang/Dropbox/2_SummerPaper/Data/myScraper/selectedState/" + str(stateNumber) + "/'+ str(0) + '",\\'
                pass
        for x in range (myStartPage, myEndPage):
            myText = '"/home/shuzhang/researchScraper/" + str(stateNumber) + "/'+ str(x*myInterval) + '",\\'
            
            print myText
            #fulltext = fulltext + myText + ", "
        print fulltext + ']'
    else:
        fulltext = ""
        print 'directoryArray = [\\'
        for x in range (myStartPage, myEndPage):

            myText = '"/home/shuzhang/researchScraper/NoState/'+ str(x*myInterval) + '",\\'

            print myText
            #fulltext = fulltext + myText + ", "
        print fulltext + ']'
    print ""
    print 'listNumber = ["Thread 0", "Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25", "Thread 26", "Thread 27", "Thread 28", "Thread 29", "Thread 30", "Thread 31", "Thread 32", "Thread 33", "Thread 34", "Thread 35", "Thread 36", "Thread 37", "Thread 38", "Thread 39", "Thread 40", "Thread 41", "Thread 42", "Thread 43", "Thread 44", "Thread 45", "Thread 46", "Thread 47", "Thread 48", "Thread 49", "Thread 50", "Thread 51", "Thread 52", "Thread 53", "Thread 54", "Thread 55", "Thread 56", "Thread 57", "Thread 58", "Thread 59"]'
    print ""

    fulltext = ""
    print 'myCurrentPage = [\\'
    for x in range (myStartPage, myEndPage):
        

        myText = str(x*myInterval) + ',\\'
        print "#" + str(x)
        print myText
        
        #fulltext = fulltext + myText + ", "
    print fulltext + ']'
    
    print ""
    print 'splitURLS = [\\' + "\nCopy and Paste URLs Here\n" + ']'

if __name__ == '__main__':
    main()
