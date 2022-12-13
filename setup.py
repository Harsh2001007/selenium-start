import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service("C:/Users/TUL/Desktop/cd/cd2.exe")

driver = webdriver.Chrome(service=s)
driver.get('https://www.universityliving.com/')
