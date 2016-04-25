from selenium import webdriver
import time
import lxml.html
import traceback
import itertools
import csv
def getURL():
    driver = webdriver.Firefox()
    with open ("myList.csv", 'rb') as searchList:
        myCSV = csv.reader(searchList, delimiter='|', quotechar='"')
        start = 0
        for company in itertools.islice(myCSV, start, 5):
            try:
                time.sleep(1)
                text = company[2].decode('utf-8')
                driver.implicitly_wait(20)
                driver.get("file:///home/myanime/Desktop/googleScraper/webforum/google/Google.html")
                searchbox = driver.find_element_by_xpath('//*[@id="lst-ib"]')
                searchbox.send_keys(text)
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="gbqfbb"]').click()
                driver.implicitly_wait(20)
                urlText = driver.current_url
                start = start + 1
                with open ("fullList.csv", "a") as file:
                    file.write(company[0].encode('utf-8'))
                    file.write("|")
                    file.write(company[1].encode('utf-8'))
                    file.write("|")
                    file.write(company[2].encode('utf-8'))
                    file.write("|")
                    file.write(company[3].encode('utf-8'))
                    file.write("|")
                    file.write(urlText.encode('utf-8'))
                    file.write("\n")
            except:
                traceback.print_exc()
'''
driver = webdriver.Firefox()

driver.get("file:///home/myanime/Desktop/googleScraper/webforum/webSummit/web2.html")

html = lxml.html.fromstring(driver.page_source)
for x in range (0, 1000):
    name = './/*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/h4/text()'
    position = './/*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/span[1]/strong/text()'
    company = './/*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/span[2]/strong/text()'
    country = './/*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/span[4]/strong/text()'
    
    try:
        textNameL = html.xpath(name)
        textName = textNameL[0].encode('utf-8')
    except:
        textName = "None".encode('utf-8')
        traceback.print_exc()
    try:
        textPositionL = html.xpath(position)
        textPosition = textPositionL[0].encode('utf-8')
    except:
        textPosition = "None".encode('utf-8')
    try:
        textCompanyL = html.xpath(company)
        textCompany = textCompanyL[0].encode('utf-8')
    except:
        textCompany = "None".encode('utf-8')
    try:
        textCountryL = html.xpath(country)
        textCountry = textCountryL[0].encode('utf-8')
    except:
        textCountry = "None".encode('utf-8')
    print x
    
    with open("webForum2.csv", "a") as file:
        file.write(textName)
        file.write("|")
        file.write(textPosition)
        file.write("|")
        file.write(textCompany)
        file.write("|")
        file.write(textCountry)
        file.write("\n")

'''
