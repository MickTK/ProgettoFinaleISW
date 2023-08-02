from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os

#test prova

driver = webdriver.Chrome("C:\chromedriver.exe") 
driver.get("https://www.google.com") 
time.sleep(2) 
ricerca=driver.find_element("id","APjFqb") 
ricerca.send_keys("Ciao") 
ricerca.send_keys(Keys.ENTER)
time.sleep(10)
