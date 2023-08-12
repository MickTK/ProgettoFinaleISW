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
        prodottiCarrello = self.driver.find_elements(By.ID, prodotto_id_cercato)

        # restituisce true se la lunghezza della lista è maggiore di zero
        return len(prodottiCarrello) > 0

# verifica se un determinato prodotto è stato rimosso dal carrello    
    def verifica_prodotto_nel_carrello_rimosso(self, prodotto_id_cercato):
        prodottiCarrello = self.driver.find_elements(By.ID, prodotto_id_cercato)
        if len(prodottiCarrello) > 0:
            prodottiCarrello = int(prodottiCarrello[0].text)
        else:
            return 0
            


        
        
            
        # restituisce la lunghezza della lista
        return prodottiCarrello 
    
# torna alla home
    def accedi_alla_home(self):
        accedi_alla_home_button = self.driver.find_element(By.ID, "homeCarr")
        accedi_alla_home_button.click()    
        
# logout dal carrello
    def logout_dal_carrello(self):
        logout_dal_carrello_button = self.driver.find_element(By.ID, "logoutCarr")
        logout_dal_carrello_button.click()      
        
# accedi al checkout
    def accedi_al_checkout(self):
        accedi_al_checkout_button = self.driver.find_element(By.ID, "checkout")
        accedi_al_checkout_button.click()
        
# rimuove un singolo prodotto dal carrello
    def rimuovi_prodotto(self, prodotto_id):
        rimuovi_prodotto_button = self.driver.find_element(By.ID, f"rimuovi_prodotto_{prodotto_id}")
        rimuovi_prodotto_button.click()
                         

            