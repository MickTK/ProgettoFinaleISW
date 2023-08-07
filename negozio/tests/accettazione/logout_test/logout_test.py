from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os

# Apre la pagina del login su Chrome
driver = webdriver.Chrome() 
driver.implicitly_wait(15)  # Impostare un tempo di attesa di tot secondi per ogni operazione 

# Individua il bottone al logout
logout = driver.find_element(by='id', value='logout')

# preme il link del logout
time.sleep(6)
logout.click()

time.sleep(6)