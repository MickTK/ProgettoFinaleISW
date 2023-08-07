from selenium import webdriver
from django.test import TestCase

from selenium.webdriver.common.keys import Keys 
import time 
import os

# Inizializza il driver singleton
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get("http://127.0.0.1:8000/")