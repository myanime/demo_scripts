#!/usr/bin/env python
import re
import requests
from BeautifulSoup import BeautifulSoup
import urllib2
import requests
import requests.exceptions

from selenium import webdriver


class EmailScraper():
    def __init__(self):        
        self.emails = []

    def reset(self):
        self.emails = []

    def collectAllEmail(self, htmlSource):
        "collects all possible email addresses from a string, but still it can miss some addresses"
        #example: t.s@d.com
        email_pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
        self.emails = re.findall(email_pattern, htmlSource)
        myEmail = re.findall(email_pattern, htmlSource)
        try:
            print myEmail[0]
        except:
            print "None"

def getEmail(html):
    myEmail = EmailScraper()
    myEmail.collectAllEmail(html)
    
def followLink(name):
    linkToFollow = driver.find_element_by_link_text(name)
    linkToFollow.click()
    driver.implicitly_wait(20)
    text2search = driver.page_source
    getEmail(text2search)
def checkLink():
    pass
driver = webdriver.Firefox()
x = True
while x == True:
    checkLink()
    driver.get("http://maier-gefluegelhof.de/")
    followLink("Impressum")
