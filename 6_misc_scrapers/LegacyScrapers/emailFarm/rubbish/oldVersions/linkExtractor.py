#!/usr/bin/env python
import re
import requests
from BeautifulSoup import BeautifulSoup
import urllib2
import requests
import requests.exceptions

import mechanize
from selenium import webdriver
'''
br = mechanize.Browser()

response = br.open('http://maier-gefluegelhof.de/')
#print response.read()      # the text of the page
#response1 = br.response()  # get the response again
#print response1.read() 

for link in br.links():
    print link.text, link.url


req = br.click_link(text='Kontakt')
br.open(req)

print response.read()   
print response.geturl()

'''



   

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
    def collectEmail(self, htmlSource):
        "collects all emails that starts with mailto: in the html source string"
        #example: <a href="mailto:t.s@d.com">
        
        email_pattern = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", re.IGNORECASE)
        myEmail = self.emails = re.findall(email_pattern, htmlSource)
        #print myEmail[0]

def getEmail(html):
    myEmail = EmailScraper()
    myEmail.collectAllEmail(html)
    
def searchLink(link2follow):
    response = urllib2.urlopen(link2follow)
    html = response.read()
    getEmail(html)

driver = webdriver.Firefox()
driver.get("http://maier-gefluegelhof.de/")
linkToFollow = driver.find_element_by_link_text("Impressum")
linkToFollow.click()
driver.implicitly_wait(20)
text2search = driver.page_source
getEmail(text2search)

'''
#url = "http://www.agrar-grossengottern.de/"
url = "http://maier-gefluegelhof.de/"
response = requests.get(url)
# parse html
page = str(BeautifulSoup(response.content))
#getEmail(page)
page2 = BeautifulSoup(response.content)

for link in page2.findAll('a', href=True, text='Kontakt'):
    #response = requests.get(link)
    #print BeautifulSoup(response.content)
    searchLink(link)


for link in page2.findAll('Kontakt', href=True):
    # skip useless links
    print link
    print "@@@@@@@@@@@@@@@@@@@"


    br.links(text_regex='...')
    
def getURL(page):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    start_link = page.find("a href")
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1: end_quote]
    return url, end_quote

while True:
    url2, n = getURL(page)
    page = page[n:]
    if url2:
        link2follow = url + url2[2:]
        print link2follow
        searchLink(link2follow)
    else:
        break

'''
