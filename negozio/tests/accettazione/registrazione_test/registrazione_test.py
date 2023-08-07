from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os


# Apre la pagina del login su Chrome
driver = webdriver.Chrome() 
driver.implicitly_wait(15)  # Impostare un tempo di attesa di tot secondi per ogni operazione
driver.get("http://127.0.0.1:8000/") 


# preme il link alla registrazione

registrazione = driver.find_element(by='id', value='registrazione')
time.sleep(6)
registrazione.click()

# Individua i campi username, password

username = driver.find_element(by='id', value='username')
password = driver.find_element(by='id', value='password')

# Compila i campi dei form
time.sleep(3)
username.send_keys("frefrufri")
time.sleep(3)
password.send_keys("cocacola")

# Individua il bottone della registrazione e si registra
time.sleep(6)
registrati = driver.find_element(by='id', value='registrati')
registrati.click()

time.sleep(6)