# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import string
from selenium.webdriver.common.keys import Keys


############################## THINGS TO CHANGE ##############################


#password and login details
myUsername = "maria.ivanova-msk@mail.ru"
myPassword = "test1234" 


#sort of a gui, if you want to package it
#print "Login to hh.ru"
#myUsername = raw_input("Vodi email (ot hh.ru chet): ")
#myPassword = raw_input("Vodi parol: ")


#change to your desired job type
catalogName = "http://hh.ru/catalog/Sportivnye-kluby-fitnes-salony-krasoty"


##############################################################################


#The program works quite well, will iterate through and apply for about 400 jobs in the selected category (20 jobs, twenty pages)
#Also some of the companies will ask for a Cover letter, that sort of also throws an exception (actually hh doesnt let you press the button)
#Apart from that it works well enough




#This loads Selenium webdriver
browser = webdriver.Firefox()


#Logs into the program using Login function


def hhLogin():
browser.get("https://www.hh.ru/account/login")
browser.page_source.encode('utf-8')
# fill username 
loginFieldElement = browser.find_element_by_name("username")
loginFieldElement.clear()
loginFieldElement.send_keys(myUsername)


# fill password
passwordFieldElement = browser.find_element_by_name("password")
passwordFieldElement.clear()
passwordFieldElement.send_keys(myPassword)


# click "submit"
submit_button = browser.find_element_by_xpath("//input[@type='submit']")
submit_button.click()


def jobSelector(x, catName):
#popup window handler
parent_h = browser.current_window_handle


#this selects which type of job you want to apply for, and also the page number.
#Change catalogName to your desired job catalog category, the page numbers are set up automatically in the pageCreator() method
browser.get(catName)


#this loops through the table of jobs on page number n
workLink = browser.find_element_by_xpath(jobTableNumberCreator(x))
workLink.click()

#after clicking on the link that opens a new window the following 3 lines have to be run to switch the focus to the pop-up window
handles = browser.window_handles
handles.remove(parent_h)
browser.switch_to_window(handles.pop())

try:
#do stuff in the popup, specifically click the Откликнуться button. Then some sort of java popup will open and we have to select Отправить отклик
greenButton = browser.find_element_by_partial_link_text("Откликнуться")
greenButton.click()
#waits a little for the browser, otherwise an exception could arise
time.sleep(2)
browser.find_element_by_xpath(u"//input[@value='Отправить отклик']").click()
browser.close()
#popup window closes and you are returned to the table of jobs
browser.switch_to_window(parent_h)
except:
#if a job has already been applied for an exception will be thrown, and the program moves on to the next job.
#this can happen quite often as hh.ru puts "premium" job adds on the top of the first couple of pages
execptionFound = 1
print "There was an error applying for job number "
print x
browser.close()
browser.switch_to_window(parent_h)


#sets up the xPath for jobs number x in the list of jobs.
def jobTableNumberCreator(x):
xPathJob = "//*[@id='js-disabled']/body/div[3]/div[2]/div/div[7]/div/table/tbody/tr/td[2]/div/table/tbody/tr/td[1]/div[1]/div[" + str(x) + "]/div[2]/div[1]/a"
return xPathJob


#sets up the url for the next pages 
def pageCreator(a):
catalogNameExtended = catalogName + "/page-" + str(a)
return catalogNameExtended


##### MAIN LOOP #####


#loops through page 1 to 21
#there is the option of starting the first page and subsequent page job serches (startFirsPageJobA) at different job numbers. This was simply for testing purposes.
#(I had already applied to most of the jobs on the fist page, and couldnt be a$$ed waiting for all the iterations to see it the page change function worked.)
def looper(startFirstPageJobAt, startnPageJobAt):
firstLoop(startFirstPageJobAt)


for pageNumber in range (1, 20):
nLoop(startnPageJobAt, pageNumber)


print "20 pages of jobs have been applied for. Exiting program"


def main():
print 'Welcome to HeadHunter AutoWorker Version 1'
time.sleep(2)
hhLogin()
looper(1, 1)


#Here you can trigger the helper loops if you want to
#firstLoop(15)
#nLoop(1, 2)




### HELPER LOOPS ###


#loops through the first page
def firstLoop(startJobAt):
print "pg 1 loop has started at job number: "
print startJobAt

for currentJobApplicationNumber in range (startJobAt, 20):
execptionFound = 0
jobSelector(currentJobApplicationNumber, catalogName)
if execptionFound == 1:
startJobAt = currentJobApplicationNumber + 1
firstLoop(startJobAt)


print "firstLoop has finished. All jobs on page number 1 have been applied for. Commencing nLoop..."

#loops through page 2 to 21
def nLoop(startJobAt, pageNumber):

print "page number (n) Loop has started at job number: "
print startJobAt
print "On page number (+1): "
print pageNumber



for currentJobApplicationNumber in range (startJobAt, 20):
execptionFound = 0
jobSelector(currentJobApplicationNumber, pageCreator(pageNumber)) 


if execptionFound == 1:
startJobAt = currentJobApplicationNumber + 1
nLoop(startJobAt, pageNumber)


print "page number (n) loop has finished. Commencing next page... "


#Python Boilerplate code
if __name__ == '__main__':
main()
