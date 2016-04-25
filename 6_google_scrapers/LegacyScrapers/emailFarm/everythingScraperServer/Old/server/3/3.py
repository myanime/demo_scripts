from selenium import webdriver
import time
import traceback
import itertools
import csv
import codecs
import time
import random
import threading

searchEngine = "DUCK"
fileOutputName = searchEngine + "fullListFW.csv"

if searchEngine == "BING":
    engineURL = "http://www.bing.de"
    inputBox = '//*[@id="sb_form_q"]'
    searchButon = '//*[@id="sb_form_go"]'
    firstElement = '//*[@id="b_results"]/li[1]/div[1]/h2/a'
elif searchEngine == "GOOGLE":
    engineURL = "file:///home/myanime/Desktop/webScrapers/webForum/google/Google.html"
    inputBox = '//*[@id="lst-ib"]'
    searchButon = '//*[@id="tsf"]/div[2]/div[3]/center/input[1]'
    firstElement = '//*[@id="rso"]/div/div[1]/div/h3/a'
elif searchEngine == "DUCK":
    engineURL = 'https://duckduckgo.com/'
    inputBox = '//*[@id="search_form_input_homepage"]'
    searchButon = '//*[@id="search_button_homepage"]'
    firstElement = '//*[@id="r1-0"]/div/h2/a[1]'

listLoad = "myList.csv"
listSave = ["Thread1_" + fileOutputName, "Thread2_" + fileOutputName]
listNumber = ["Thread 1", "Thread 2"]
startArray = [3500, 4000]
stopArray = [4000, 4500]
google = True

def main():
    multiThreading()
  
def multiThreading():
    for number in range (0, 2):
        
        try:
            print "multiThreading Started"
            myFileNameSave = listSave[number]
            myFileNameLoad = listLoad
            myThreadNumber = listNumber[number]
            myStart = startArray[number]
            myStop = stopArray[number]

            t = threading.Thread(target=getURL, args = (myFileNameSave, myFileNameLoad, myThreadNumber, myStart, myStop))
            t.start()
            time.sleep(60)
        except Exception, detail:
                print "ERROR:", detail

def errorLog():
    try:
        with open ("error.log", "a") as erfile:
            erfile.write(str(start))
            file.write("|")
            file.write("\n")
    except:
        time.sleep(5)
        
def getURL(myFileNameSave, myFileNameLoad, myThreadNumber, myStart, myStop):
    driver = webdriver.Firefox()
    with open (myFileNameLoad, 'rb') as searchList:
        myCSV = csv.reader(searchList, delimiter='|', quotechar='"')
        start = myStart
        stop = myStop
        for company in itertools.islice(myCSV, start, stop):
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
                driver.implicitly_wait(20)
                try:
                    driver.find_element_by_xpath(firstElement).click()
                except:
                    errorLog()
                    start = start + 1
                time.sleep(2)
                urlText = driver.current_url
                #print str(start) + ": " + urlText

                try:
                    searchbox = driver.find_element_by_xpath('//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]/a')
                    searchbox.click()
                    email = driver.find_element_by_xpath('//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]/a').text
                    myWait = random.randrange(3, 10, 1)
                    time.sleep(myWait)
                    print str(start) +": " + email + " wait: " + str(myWait)
                except:
                    myWait = random.randrange(1, 5, 1)
                    time.sleep(myWait)
                    print str(start) +": " + "No email" + " wait: " + str(myWait)
                    email = "None"
                
                start = start + 1
                with open (myFileNameSave, "a") as file:
                    file.write(company[0])
                    file.write("|")
                    file.write(company[1])
                    file.write("|")
                    file.write(company[2])
                    file.write("|")
                    file.write(company[3])
                    file.write("|")
                    file.write(company[4])
                    file.write("|")
                    file.write(company[5])
                    file.write("|")
                    file.write(company[6])
                    file.write("|")
                    file.write(company[7])
                    file.write("|")
                    file.write(company[8])
                    file.write("|")
                    file.write(company[9])
                    file.write("|")
                    file.write(company[10])
                    file.write("|")
                    file.write(company[11])
                    file.write("|")
                    file.write(company[12])
                    file.write("|")
                    file.write(company[13])
                    file.write("|")
                    file.write(urlText.encode('utf-8'))
                    file.write("|")
                    file.write(email.encode('utf-8'))
                    file.write("\n")
            
            except:
                traceback.print_exc()
                time.sleep(5)
                driver.quit()
                start = start + 1
                errorLog()
                getURL(myFileNameSave, myFileNameLoad, myThreadNumber, start, myStop)
                
if __name__ == '__main__':
    main()

                
