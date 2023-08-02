from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os

#test prova

driver = webdriver.Chrome() 
driver.get("login/") 
time.sleep(15) 
