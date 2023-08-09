# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
from django.test import TestCase

class Carrello:
    # inizializza la classe
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:8000/carrello/"

    # apre il browser e la pagina web
    def open(self):
        self.driver.get(self.url)
        

# verifica la presenza di un determinato prodotto nel carrello    
    def verifica_prodotto_nel_carrello(self, prodotto_id_cercato):
        prodottiCarrello = self.driver.find_elements(By.ID, "prodotti_carrello")
        
        
        for prodottoCarrello in prodottiCarrello:
            id_prodotto_attuale = prodottoCarrello.find_element(By.ID, "id_prodotto_carrello").text
            if id_prodotto_attuale == prodotto_id_cercato:
                return True
        return False
            