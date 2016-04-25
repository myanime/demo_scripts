# -*- coding: utf-8 -*-

from selenium import webdriver
import lxml.html
import time

browser = webdriver.Firefox()

def dateWriter():
    #for x in range (1, 50):    
    pass

def lxmlLegalScraper():
    ###################### The Setup section #########################
    
    print "Starting a Legal Scraper"

    url = "http://www.cobbsuperiorcourtclerk.org/scripts/CourtsCV.dll/CivilSearchByType"
    browser.get(url)

    #Choose 2 years
    browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody[2]/tr[2]/td/font/table/tbody/tr/td/font[1]/select/option[6]").click()
    browser.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody[2]/tr[6]/td/table/tbody/tr[2]/td[1]/input").click()

    html = lxml.html.fromstring(browser.page_source)
    print html.xpath("/html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[4]//text()")
"""
    import lxml.html
    root = lxml.html.fromstring(doc)
    root.xpath('//tr/td//text()')
    for tbl in root.xpath('//table'):
         elements = tbl.xpath('.//tr/td//text()')
         print elements

    #print browser.find_element_by_xpath("/html/body/form/table/tbody").text

    
    /html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[4]
    /html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[5]
    /html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[7]
    /html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[3]/td[1]

    
    /html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[16]/td[1]
    

    #This is the cell selector for lxml version
    def cellSelector(rowNumber, colNumber):
        #return ".//table/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) +"]/text()"
        
        #return ".//table/tbody/tr[" + str(rowNumber) + "]/td/font/table/tbody/tr[" + str(rowNumber) + "]/td" + str(colNumber) +"]/text()"
        return ".//table/tbody/tr[2]/td[4]/text()"
    
        #/html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[2]
        #/html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[5]
    fullText = ""
    
    for pageNumber in range (1, 2):
        html = lxml.html.fromstring(browser.page_source)
        for x in range (2, 7):
            #This calls the cellSelector method, but it has to be slightly modified, depending on the year
            #In 1975 for example there are only 14 (have to add 1, 14 ->15) there are 26. Its because of photos, and
            #stuff like that, in 1975 there were probably not as many digital cammeras and iphones.
            
            for y in range (2, 27):
                listItem = html.xpath((cellSelector(x, y)))
                myText = str(listItem)
                print myText
                fullText = fullText + myText + ", "
            #print "Copying row number " + str(x)
            myFileName = "LEGAL"
            
            fullText = fullText + "\n"
            #Writes to a text file
            xText = fullText.encode('utf-8')
            f = open(myFileName, 'a')
            f.write(xText)
            f.close()
            #Clears the text and moves on to the next row
            fullText = ""
            myText = ""


    
    ###################### The Copying section #########################

                   
    #This is the cell selector for lxml version
    def cellSelector(rowNumber, colNumber):
        #return ".//table/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) +"]/text()"
        return ".//table/tbody/tr[" + str(rowNumber) + "]/td/font/table/tbody/tr[" + str(rowNumber) + "]/td" + str(colNumber) +"]/text()"
        #/html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[2]
        #/html/body/form/table/tbody/tr[2]/td/font/table/tbody/tr[2]/td[5]
    fullText = ""
    try:
        for pageNumber in range (1, 2):
            html = lxml.html.fromstring(browser.page_source)
            for x in range (2, 7):
                #This calls the cellSelector method, but it has to be slightly modified, depending on the year
                #In 1975 for example there are only 14 (have to add 1, 14 ->15) there are 26. Its because of photos, and
                #stuff like that, in 1975 there were probably not as many digital cammeras and iphones.
                try:
                    for y in range (2, 27):
                        listItem = html.xpath((cellSelector(x, y)))
                        myText = str(listItem)
                        fullText = fullText + myText + ", "
                    #print "Copying row number " + str(x)
                    myFileName = "LEGAL"
                    
                    fullText = fullText + "\n"
                    #Writes to a text file
                    xText = fullText.encode('utf-8')
                    f = open(myFileName, 'a')
                    f.write(xText)
                    f.close()
                    #Clears the text and moves on to the next row
                    fullText = ""
                    myText = ""
                except:
                    print "There are only " +str(y) + " columns in this years data"
            #This clicks the next 100 button
            #browser.find_element_by_xpath("//input[@value='Next 100 >']").submit()
            #print "We are now on the " + str(pageNumber) + " page"
    except:
        print "EXCEPTIONpageNumber"
        print pageNumber
    print "END"
"""

def lxmlMarathonScraper():
    ###################### The Setup section #########################
    for yearNo in range (2, 3):
        print "Starting a New year"

        url = "http://web2.nyrrc.org/cgi-bin/start.cgi/mar-programs/archive/archive_search.html"
        browser.get(url)

        #Change the number in the option[x] box for the preferred date. 1975 is 39, 2014 is 1
        browser.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[7]/td[2]/select/option[" + str(yearNo) + "]").click()
        #This clicks the radio button
        browser.find_elements_by_css_selector("input[type='radio'][value='search.age']")[0].click()
        #This enters the age
        ageBox = browser.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[18]/td[2]/input[1]')
        ageBox.clear()
        ageBox.send_keys('18')
        ageBox2 = browser.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[18]/td[2]/input[2]')
        ageBox2.clear()
        ageBox2.send_keys('99')
        #Clicks the submit button
        browser.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[32]/td[2]/input").click()


        ###################### The Copying section #########################

                       
        #This is the cell selector for lxml version
        def cellSelector(rowNumber, colNumber):
            return ".//table[1]/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) +"]/text()"

        fullText = ""
        try:
            for pageNumber in range (1, 600):
                html = lxml.html.fromstring(browser.page_source)
                for x in range (2, 102):
                    #This calls the cellSelector method, but it has to be slightly modified, depending on the year
                    #In 1975 for example there are only 14 (have to add 1, 14 ->15) there are 26. Its because of photos, and
                    #stuff like that, in 1975 there were probably not as many digital cammeras and iphones.
                    try:
                        for y in range (1, 27):
                            listItem = html.xpath((cellSelector(x, y)))
                            myText = str(listItem)
                            fullText = fullText + myText + ", "
                        #print "Copying row number " + str(x)
                        myFileName = "OCTATOK" + str(2014 - yearNo + 1)
                        myYear = str(2014 - yearNo + 1) + ", "
                        
                        fullText = myYear + fullText + "\n"
                        #Writes to a text file
                        xText = fullText.encode('utf-8')
                        f = open(myFileName, 'a')
                        f.write(xText)
                        f.close()
                        #Clears the text and moves on to the next row
                        fullText = ""
                        myText = ""
                    except:
                        print "There are only " +str(y) + " columns in this years data"
                #This clicks the next 100 button
                browser.find_element_by_xpath("//input[@value='Next 100 >']").submit()
                print "We are now on the " + str(pageNumber) + " page"
        except:
            print "pageNumber"
            print pageNumber
            print "yearNo"
            print yearNo
            print "Year finished"
        
def lxmlMarathonScraper2():
    ###################### The Setup section #########################

    url = "http://web2.nyrrc.org/cgi-bin/start.cgi/mar-programs/archive/archive_search.html"
    browser.get(url)

    #Change the number in the option[x] box for the preferred date. 1975 is 39, 2014 is 1
    browser.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[7]/td[2]/select/option[29]").click()
    #This clicks the radio button
    browser.find_elements_by_css_selector("input[type='radio'][value='search.age']")[0].click()
    #This enters the age
    ageBox = browser.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[18]/td[2]/input[1]')
    ageBox.clear()
    ageBox.send_keys('18')
    ageBox2 = browser.find_element_by_xpath('/html/body/div[2]/form/table/tbody/tr[18]/td[2]/input[2]')
    ageBox2.clear()
    ageBox2.send_keys('99')
    #Clicks the submit button
    browser.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[32]/td[2]/input").click()


    ###################### The Copying section #########################

                   
    #This is the cell selector for lxml version
    def cellSelector(rowNumber, colNumber):
        return ".//table[1]/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) +"]/text()"

    fullText = ""
    for pageNumber in range (1, 1000):
        html = lxml.html.fromstring(browser.page_source)
        for x in range (2, 102):
            #This calls the cellSelector method, but it has to be slightly modified, depending on the year
            #In 1975 for example there are only 14 (have to add 1, 14 ->15) there are 26. Its because of photos, and
            #stuff like that, in 1975 there were probably not as many digital cammeras and iphones.
            try:
                for y in range (1, 27):
                    listItem = html.xpath((cellSelector(x, y)))
                    myText = str(listItem)
                    fullText = fullText + myText + ", "
                #print "Copying row number " + str(x)
                fullText = fullText + "\n"
                #Writes to a text file
                xText = fullText.encode('utf-8')
                f = open('myCSVFile1985', 'a')
                f.write(xText)
                f.close()
                #Clears the text and moves on to the next row
                fullText = ""
                myText = ""
            except:
                print "There are only " +str(y) + " columns in this years data"
        #This clicks the next 100 button
        browser.find_element_by_xpath("//input[@value='Next 100 >']").submit()
        print "We are now on the " + str(pageNumber) + " page"

def demoOfLxml():
    root = lxml.html.fromstring(browser.page_source)
    for row in root.xpath('.//table[1]/tbody/tr'):
        cells = row.xpath('.//td/text()')
        print cells

def seleniumMarathonScraper():
    #Original Scraper without lxml library
    def originalScraperForMarathon():
        fullText = ""
        for pageNumber in range (1, 10000):
            for x in range (2, 102):
                #This calls the cellSelector method, but it has to be slightly modified, depending on the year
                #In 1975 for example there are only 14 (have to add 1, 14 ->15) there are 26. Its because of photos, and
                #stuff like that, in 1975 there were probably not as many digital cammeras and iphones.
                for y in range (1, 27):
                    myText = browser.find_element_by_xpath(cellSelector(x, y)).text
                    fullText = fullText + myText + ", "
                print "Copying row number " + str(x)
                fullText = fullText + "\n"
                #Writes to a text file
                xText = fullText.encode('utf-8')
                f = open('myCSVFile', 'a')
                f.write(xText)
                f.close()
                #Clears the text and moves on to the next row
                fullText = ""
                myText = ""
            #This clicks the next 100 button
            browser.find_element_by_xpath("//input[@value='Next 100 >']").submit()
            print "We are now on the " + str(pageNumber) + " page"

    #This is a method that sets up the cell from which will be coppied for rowX selenium version
    def cellSelector(rowNumber, colNumber):
        return "/html/body/div[2]/p[5]/table[1]/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) + "]"

################### Some tuning ###################

def alabamaScraper():
    for stateNumber in range (2, 54):
        url = "http://www.nahu.org/consumer/findagent2.cfm"
        browser.get(url)
        browser.find_element_by_xpath("/html/body/div/div[5]/form/table/tbody/tr[8]/td[2]/select/option[" +str(stateNumber) +"]").click()

        browser.find_element_by_xpath("/html/body/div/div[5]/form/table/tbody/tr[11]/td[2]/nobr[5]/input").click()
        browser.find_element_by_xpath("/html/body/div/div[5]/form/table/tbody/tr[11]/td[2]/nobr[12]/input").click()
        browser.find_element_by_xpath("/html/body/div/div[5]/form/table/tbody/tr[12]/td[2]/input[2]").click()
        def cellSelector(number):
            return "/html/body/div/div[5]/div[" + str(number) + "]"

        for number in range (1, 100):
            try:
                xText = str(browser.find_element_by_xpath(cellSelector(number)).text)
                #Writes to a text file
                xText = xText.encode('utf-8')
                f = open('alabamaFile', 'a')
                f.write(xText)
                f.close()
                xText = ''
            except:
                print 'end of list'
                print number
