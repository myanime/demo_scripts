from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
browser = webdriver.Firefox()

browser.get('http://gatherproxy.com/proxylist/country/?c=United%20States#3')
browser.find_element_by_xpath('//*[@id="body"]/form/p/input').click()
source = browser.find_element_by_xpath("/html/body").text.encode('utf-8')
myFile = open("gatherProxy.txt", 'a')
myFile.write(source)
myFile.close
print 'done'
time.sleep(1)
for x in range (1, 20):
    time.sleep(1)
    link = '//*[@id="psbform"]/div/a[' + str(x) + ']'
    browser.find_element_by_xpath(link).click()
    source = browser.find_element_by_xpath("/html/body").text.encode('utf-8')
    myFile = open("gatherProxy.txt", 'a')
    myFile.write(source)
    myFile.close
    print 'done'
