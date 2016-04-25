from selenium import webdriver
from selenium.webdriver.common.proxy import *
import time
browser = webdriver.Firefox()

browser.get("http://www.xroxy.com/proxylist.htm")

source = browser.find_element_by_xpath("/html/body").text.encode('utf-8')
myFile = open("myFullproxydata2.txt", 'a')
myFile.write(source)
myFile.close
print 'done'
time.sleep(1)
for x in range (0, 200):
    browser.get("http://www.xroxy.com/proxylist.php?port=&type=&ssl=&country=&latency=&reliability=&sort=reliability&desc=true&pnum=" + str(x) + "#table")
    source = browser.find_element_by_xpath("/html/body").text.encode('utf-8')
    myFile = open("myFullproxydata2.txt", 'a')
    myFile.write(source)
    myFile.close
    time.sleep(5)
    print 'done'
