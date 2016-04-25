#!/usr/bin/env python
import re
import requests
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import time

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
        
    def collectEmail(self, htmlSource):
        "collects all emails that starts with mailto: in the html source string"
        #example: <a href="mailto:t.s@d.com">
        email_pattern = re.compile("<a\s+href=\"mailto:([a-zA-Z0-9._@]*)\">", re.IGNORECASE)
        self.emails = re.findall(email_pattern, htmlSource)

def getEmail(html):
    myEmail = EmailScraper()
    printEmail = myEmail.collectAllEmail(html)
    print printEmail
    
#url = "http://www.agrar-grossengottern.de/"
url = "http://maier-gefluegelhof.de/maier/index.php?module=content&web=impressum"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
texts = soup.findAll(text=True)
print texts

getEmail(texts[0])
'''
def visible(element):
    if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element)):
        return False
    return True
visible_texts = filter(visible, texts)


saveFile = open("completeFile.txt", 'a')
saveFile.write(str(visible_texts))
saveFile.close()
'''
"""

response = urllib2.urlopen(url)
html = response.read()
#print html
htmlSource = "ryan@sibmail.com"

    

"""
