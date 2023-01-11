import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('D:\\webdriver\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.google.com/")
time.sleep(2)
driver.close()
