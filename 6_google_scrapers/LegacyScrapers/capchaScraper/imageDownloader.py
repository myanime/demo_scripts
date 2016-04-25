import urllib
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://m.simon.com/store.aspx?tid=90389&id=1353')

# get the image source
img = driver.find_element_by_xpath('//*[@id="ctl00_cpBody_fvTenant"]/tbody/tr/td/div[1]/img')
src = img.get_attribute('src')

# download the image
urllib.urlretrieve(src, "captcha.png")

