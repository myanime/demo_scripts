from selenium import webdriver
import time
import lxml.html
import traceback
import itertools
import csv
import codecs
import time
inputURL = "/home/myanime/Desktop/webScrapers/emailFarm/redaction/0-500/0-500fw.csv"
def getURL(myStart):
    driver = webdriver.Firefox()
    with open (inputURL, 'rb') as searchList:
        myCSV = csv.reader(searchList, delimiter='|', quotechar='"')
        start = myStart
        stop = 1000
        for company in itertools.islice(myCSV, start, stop):
            try:
                time.sleep(1)
                text = company[14].decode('utf-8')
                driver.implicitly_wait(6)
                time.sleep(.3)
                driver.get(text)
                time.sleep(.3)
                try:
                    searchbox = driver.find_element_by_xpath('//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]/a')
                    searchbox.click()
                    email = driver.find_element_by_xpath('//*[@id="firmenwissen"]/div[2]/div[4]/div[2]/div[2]/div[4]/div[1]/p[2]/a').text
                    print email
                except:
                    print "No email"
                    email = "None"
                time.sleep(2)
                start = start + 1
                
                with open ("fullListWithEmails.csv", "a") as file:
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
                    file.write(company[14])
                    file.write("|")
                    file.write(email.encode('utf-8'))
                    file.write("\n")
                
            except:
                traceback.print_exc()
                time.sleep(5)
                driver.quit()
                time.sleep(5)
                getURL(start)
getURL(0)


