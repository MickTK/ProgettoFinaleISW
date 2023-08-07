from django.test import TestCase

from selenium import webdriver

from selenium.webdriver.common.keys import Keys 
import time 
import os

# Apre la pagina del login su Chrome
driver = webdriver.Chrome() 
driver.implicitly_wait(15)  # Impostare un tempo di attesa di tot secondi per ogni operazione
driver.get("http://127.0.0.1:8000/") 

# Individua i campi username, password e il bottone mediante l'id
username = driver.find_element(by='id', value='username')
password = driver.find_element(by='id', value='password')
login = driver.find_element(by='id', value='login')

# Compila i campi dei form
time.sleep(3)
username.send_keys("cliente")
time.sleep(3)
password.send_keys("cliente")

# preme il bottone e accede alla home
time.sleep(6)
login.click()



time.sleep(15)  # tot secondi prima della chiusura del browser
