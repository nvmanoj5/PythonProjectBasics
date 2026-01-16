import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#chrome driver service intermediater between webdriver and chrome driver
#service_obj = Service("F:/TESTING/AUTOMATION/PYTHON/Browser/chromedriver.exe")
#driver = webdriver.Chrome(service = service_obj)
#driver.get("https://www.google.com/")


#This will also work - It will download driver directly if you have download restriction please use above steps and download driver manually according to bro

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(3)