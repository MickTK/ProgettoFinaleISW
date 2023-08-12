# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
from django.test import TestCase

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
        torna_al_carrello_button.click()  
    
    # completa l'ordine
    def ordina(self):
        ordina_button = self.driver.find_element(By.ID, "ordina")
        ordina_button.click() 
        
    # inserisce i dati per il checkout
    def inserimento_credenziali(self, indirizzo, codice_paypal):
        indirizzo_input = self.driver.find_element(By.ID, "indirizzo")
        codice_paypal_input = self.driver.find_element(By.ID, "codice_paypal")

        indirizzo_input.send_keys(indirizzo)
        codice_paypal_input.send_keys(codice_paypal)
