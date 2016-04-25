from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("file:///home/myanime/Desktop/googleScraper/webforum/web.html")



for x in range (1, 100):
    name = '//*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/h4'
    position = '//*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/span[1]/strong'
    company = '//*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/span[2]/strong'
    country = '//*[@id="featured-attendees"]/li[' + str(x) + ']/figcaption/span[4]/strong'
    try:
        textName = driver.find_element_by_xpath(name).text
    except:
        textName = "None"
    try:
        textPosition = driver.find_element_by_xpath(position).text
    except:
        textPosition = "None"
    try:
        textCompany = driver.find_element_by_xpath(company).text
    except:
        textCompany = "None"
    try:
        textCountry = driver.find_element_by_xpath(country).text
    except:
        textCountry = "None"
    print x
    
    with open("webForum.csv", "a") as file:
        file.write(textName)
        file.write(",")
        file.write(textPosition)
        file.write(",")
        file.write(textCompany)
        file.write(",")
        file.write(textCountry)
        file.write("\n")
