# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
from django.test import TestCase
import time

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 4

class Checkout:
    # inizializza la classe
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:8000/checkout/"

    # apre il browser e la pagina web
    def open(self):
        self.driver.get(self.url)
        
    # torna al carrello
    def torna_al_carrello(self):
        torna_al_carrello_button = self.driver.find_element(By.ID, "carrelloCheckout")
        time.sleep(TIME_SLEEP)
        
        torna_al_carrello_button.click()  
    
    # completa l'ordine
    def ordina(self):
        ordina_button = self.driver.find_element(By.ID, "ordina")
        ordina_button.click() 
        
    # inserisce i dati per il checkout
    def inserimento_dati(self, indirizzo, codice_paypal):
        indirizzo_input = self.driver.find_element(By.ID, "indirizzo")
        codice_paypal_input = self.driver.find_element(By.ID, "codice_paypal")
        time.sleep(TIME_SLEEP)

        indirizzo_input.send_keys(indirizzo)
        time.sleep(TIME_SLEEP)
        
        codice_paypal_input.send_keys(codice_paypal)
        time.sleep(TIME_SLEEP)
    
    # pulire i campi del form checkout
    def reset_form_checkout(self):
        indirizzo_input = self.driver.find_element(By.ID, "indirizzo")
        codice_paypal_input = self.driver.find_element(By.ID, "codice_paypal")
        time.sleep(TIME_SLEEP)
        
        indirizzo_input.clear()
        codice_paypal_input.clear()
