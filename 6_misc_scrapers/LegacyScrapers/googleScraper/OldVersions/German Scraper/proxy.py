# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.proxy import *

myProxy = "213.136.79.124:80"

proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy': '' # set this value as desired
    })

driver = webdriver.Firefox(proxy=proxy)

driver.get("http://www.myipaddress.com/show-my-ip-address/")

"""
217.51.14.76

# for remote
caps = webdriver.DesiredCapabilities.FIREFOX.copy()
proxy.add_to_capabilities(caps)

driver = webdriver.Remote(desired_capabilities=caps)


92.222.237.89:8888
92.222.237.119:8888
213.136.79.124:80
148.251.234.73:80
62.153.96.164:80
92.222.237.79:8888
188.195.104.119:80
212.227.251.53:8118
92.222.237.76:8888
213.239.214.73:1000
92.222.237.85:8888
88.198.233.141:7808
37.200.99.210:8118
213.136.89.121:80
193.37.152.186:3128
31.214.240.212:3128
195.71.127.224:80
213.144.23.149:8080
212.211.197.94:80
"""
