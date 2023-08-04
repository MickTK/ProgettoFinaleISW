from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os

#test prova

driver = webdriver.Chrome() 
driver.get("http://127.0.0.1:8000/login/") 
time.sleep(15) 
