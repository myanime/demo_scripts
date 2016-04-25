# -*- coding: utf-8 -*-

from selenium import webdriver
import lxml.html
import time

browser = webdriver.Firefox()

#This is the cell selector for lxml version
def cellSelector(rowNumber, colNumber):
    
    return ".//table/tbody/tr[2]/td/font/table/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) +"]//text()"
    

def lxmlLegalScraper():
    ###################### The Setup section #########################
    
    print "Starting a Legal Scraper"

    url = "http://www.cobbsuperiorcourtclerk.org/scripts/CourtsCV.dll/CivilSearchByType"
    browser.get(url)

    #Choose 2 years
    browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody[2]/tr[2]/td/font/table/tbody/tr/td/font[1]/select/option[6]").click()
    browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody[2]/tr[6]/td/table/tbody/tr[2]/td[1]/input").click()
    #Change this to maybe 500, it tells you how many pages
    #you should put some error handling in here. Sometimes the site will not give you the data for the next page - you will get an error
    #in your exception handling write some code that hits the back button, then the forward button - that will fix the problem
    for x in range (0, 50):
        fullText = ""
        html = lxml.html.fromstring(browser.page_source)
        for x in range (2, 17):
            for y in range (2, 8):
                listItem = html.xpath((cellSelector(x, y)))
                myText = str(listItem)
                print myText
                fullText = fullText + myText + ", "
            myFileName = "rawOutput"
            
            fullText = fullText + "\n"
            #Writes to a text file
            xText = fullText.encode('utf-8')
            f = open(myFileName, 'a')
            f.write(xText)
            f.close()
            #Clears the text and moves on to the next row
            fullText = ""
            myText = ""
        print "moving to the next page"
        browser.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[3]/font/a").click()
        #This makes the script run slower - the site is a bit slow, if you dont slow the script down sometimes it will pull empty data(when I pulled the data, I pulled empty data for
        #page 3
        time.sleep(5)


    

