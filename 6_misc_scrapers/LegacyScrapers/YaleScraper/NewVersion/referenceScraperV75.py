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
import traceback
import csv
import itertools
import fileinput
import random

#import logging
#logging.basicConfig(level=logging.INFO, filename="myLog.log")

##############################################################
###############CHANGE THESE VALUES ###########################
##############################################################


myStartPage = 0 
myEndPage = 9
#If you restart and 100 pages have already been downloaded change the interval to 100
myInterval = 200
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


#This info is for the helper methods
stateName = '/all30000-60000.csv'
completeFile = "/Users/shuzhang/researchScraper/" + str(stateNumber) + stateName
numberOfDirectories = myEndPage - myStartPage


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
    
    #helperRename()
    #helperJoin()
    #helperDuplicateRemover()
    #helperCommaRemover()
    #helperCounter()

    
#################################################################

################################## HEADER ##################################
directoryArray = [\
"/Users/shuzhang/researchScraper/sNoState/30000",\
"/Users/shuzhang/researchScraper/sNoState/33000",\
"/Users/shuzhang/researchScraper/sNoState/36000",\
"/Users/shuzhang/researchScraper/sNoState/39000",\
"/Users/shuzhang/researchScraper/sNoState/42000",\
"/Users/shuzhang/researchScraper/sNoState/45000",\
"/Users/shuzhang/researchScraper/sNoState/48000",\
"/Users/shuzhang/researchScraper/sNoState/51000",\
"/Users/shuzhang/researchScraper/sNoState/54000",\
"/Users/shuzhang/researchScraper/sNoState/57000",\
]

listNumber = ["Thread 0", "Thread 1", "Thread 2", "Thread 3", "Thread 4", "Thread 5", "Thread 6", "Thread 7", "Thread 8", "Thread 9", "Thread 10", "Thread 11", "Thread 12", "Thread 13", "Thread 14", "Thread 15", "Thread 16", "Thread 17", "Thread 18", "Thread 19", "Thread 20", "Thread 21", "Thread 22", "Thread 23", "Thread 24", "Thread 25", "Thread 26", "Thread 27", "Thread 28", "Thread 29", "Thread 30", "Thread 31", "Thread 32", "Thread 33", "Thread 34", "Thread 35", "Thread 36", "Thread 37", "Thread 38", "Thread 39", "Thread 40", "Thread 41", "Thread 42", "Thread 43", "Thread 44", "Thread 45", "Thread 46", "Thread 47", "Thread 48", "Thread 49", "Thread 50", "Thread 51", "Thread 52", "Thread 53", "Thread 54", "Thread 55", "Thread 56", "Thread 57", "Thread 58", "Thread 59"]

myCurrentPage = [\
#10
32954,\
#11
35957,\
#12
388936,\
#13
41936,\
#14
44936,\
#15
47937,\
#16
50932,\
#17
53917,\
#18
56921,\
#19DONE!!!!!!!!!!!!!!!!!!!
59910,\
]

splitURLS = [\
#30000
None,\
#33000
None,\
#36000
None,\
#39000
None,\
#42000
None,\
#45000
None,\
#48000
None,\
#51000
None,\
#54000
None,\
#57000
None]
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
            time.sleep(15)
        except Exception, detail:
                print "ERROR:", detail
                print "Mutlit"
                traceback.print_exc()

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
    
def resetList(browser, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage):
    time.sleep(25)                            
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
        time.sleep(25)
    except:
        print "########################################ERROR RESETTING PAGE: Restarting #############################"
        time.sleep(2)
        searchURL = autoCreateCommands(browser, 1, "http://referenceusa.com/")
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
        if searchURL == None:
            time.sleep(5)
            searchURL = autoCreateCommands(browser, currentPage, "http://referenceusa.com/")
            #browser.get(searchURL)
            time.sleep(60)
        else:
            time.sleep(5)
            browser.get(searchURL)
            time.sleep(25)
            resetList(browser, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage)
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
                time.sleep(2)
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
                    resetList(browser, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage)
                    browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[1]').click()
                    time.sleep(15)
                    
            time.sleep(1)
            
            browser.implicitly_wait(1)
            #moves to next page
            browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/div[1]/div[2]/div[3]').click()
            #This was the problem 
            time.sleep(20)
            listCheckbox = browser.find_element_by_xpath('//*[@id="checkboxCol"]')
            if listCheckbox.is_selected() == False:
                listCheckbox.click()
            else:
                print myThreadNumber + ":Allready clicked checkbox"
                resetList(browser, currentPage, SAVE_TO_DIRECTORY, myThreadNumber, threadEndPage)
            time.sleep(1)
            
            browser.implicitly_wait(10)
            browser.find_element_by_xpath('//*[@id="searchResults"]/div[1]/div/ul/li[5]/a').click()
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="detailDetail"]').click()
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="downloadForm"]/div[2]/a[1]/span/span').click()
            time.sleep(1)
            #csvRenamer(currentPage, SAVE_TO_DIRECTORY)            
    except Exception, detail:
        print "ERROR:", detail
        traceback.print_exc()
        #logging.info(myThreadNumber)
        #logging.info(currentPage)
        time.sleep(5)
        myNumber1 = random.randrange(5, 20, 1)
        time.sleep(myNumber1)
        try:
            browser.quit()
        except:
            pass
        myNumber = random.randrange(60, 180, 1)
        print "Waiting " + str(myNumber) + " seconds"
        time.sleep(myNumber)
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
    driver.find_element_by_link_text("Advanced Search").click()
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
    '''
    if apple == True:
        body.send_keys(Keys.COMMAND + 't')
    else:
        body.send_keys(Keys.CONTROL + 't')
    '''
    print "#" + str(startNumber) 
    print '"' + urlText + '",\\'
    return urlText
    

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
            myText = '"Users/shuzhang/researchScraper/" + str(stateNumber) + "/'+ str(x*myInterval) + '",\\'
            
            print myText
            #fulltext = fulltext + myText + ", "
        print fulltext + ']'
    else:
        fulltext = ""
        print 'directoryArray = [\\'
        for x in range (myStartPage, myEndPage):

            myText = '"/Users/shuzhang/researchScraper/NoState/'+ str(x*myInterval) + '",\\'

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


def helperRename():
    for directory in range (0, numberOfDirectories):    
        for x in range (0, 600):
            try:
                docName = str(x)
                os.chdir(directoryArray[directory])
                files = filter(os.path.isfile, os.listdir(directoryArray[directory]))
                files = [os.path.join(directoryArray[directory], f) for f in files] # add path to each file
                files.sort(key=lambda x: os.path.getmtime(x))
                newest_file = files[x]
                os.rename(newest_file, docName+".csv")
            except:
                #print "Finished Renaming"
                #traceback.print_exc()
                pass
        print "Done Renaming"
        
def helperJoin():
    listLoad = [None] * 1000
    for x in range (0, 1000):
        listLoad[x] = str(x) + ".csv"
    for directory in range (0, numberOfDirectories):
        for renamedfile in range (0, 1000):
            try:
                print listLoad[renamedfile]
                myFileNameLoad = directoryArray[directory] +'/' + listLoad[renamedfile]
                
                #this loops through your renamed files
                

                with open(myFileNameLoad, 'rb') as pageList:
                    stateReader = csv.reader(pageList, delimiter=',', quotechar='|')
                    #this is for the rows in your downloaded file
                    start = 1
                    end = 1000
                    for row in itertools.islice(stateReader, start, end):
                        saveRow = ', '.join(row)
                        #this saves the row into the common csv file
                        saveFile = open(completeFile, 'a')
                        saveFile.write(saveRow)
                        saveFile.write("\n")
                        saveFile.close()
                    print myFileNameLoad
                    print "Work in progress..."
            except:
                #traceback.print_exc()
                pass
                
        print "Finished Joining"

def helperDuplicateRemover():       
    seen = set() # set for fast O(1) amortized lookup
    for line in fileinput.FileInput(completeFile, inplace=1):
        if line in seen: continue # skip duplicate
        seen.add(line)
        print line, # standard output is now redirected to the file
        
def helperCommaRemover():
    with open(completeFile) as infile, open(completeFile + "NoCommas.csv", "w") as outfile:
        for line in infile:
            outfile.write(line.replace('"', ''))
    print "Finished Removing Commas"

def helperCounter():
    x = 0
    print "start"
    with open(completeFile,'r') as out_file:
        for line in out_file:
            x = x + 1
    print "NumberOfLines"
    print x

    


if __name__ == '__main__':
    main()
