# -*- coding: utf-8 -*-

from selenium import webdriver

browser = webdriver.Firefox()

###################### The Setup section #########################

url = "http://web2.nyrrc.org/cgi-bin/start.cgi/mar-programs/archive/archive_search.html"
browser.get(url)

#Change the number in the option[x] box for the preferred date. 1975 is 39, 2014 is 1
browser.find_element_by_xpath("/html/body/div[2]/form/table/tbody/tr[7]/td[2]/select/option[1]").click()
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

#This is a method that sets up the cell from which will be coppied for rowX
def cellSelector(rowNumber, colNumber):
    return "/html/body/div[2]/p[5]/table[1]/tbody/tr[" + str(rowNumber) + "]/td[" + str(colNumber) + "]"

#There are a lot of entries. I set this originally to 500, that means 50000 runners. I nearly fell off my chair.
#There were more than 50000. I dont actually know, how many, but I set it to a million.
#YOu should probably add a few modifications to this code, add some exception handling

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

################### Some tuning ###################



