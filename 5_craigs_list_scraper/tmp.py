#!/usr/bin/env python
import requests
proxies = {
    'http': 'http://switchproxy.proxify.net:7498',
    'https': 'http://switchproxy.proxify.net:7498',
}
headers = {'SwitchProxy': 'identifier', 'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
print(requests.get('http://www.example.com/', proxies = proxies, headers = headers).text)
