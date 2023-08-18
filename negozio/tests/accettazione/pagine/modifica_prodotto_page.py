# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By

class ModificaProdotto:
    # inizializza la classe
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:8000/Aggiungi_prodotto/"

    # apre il browser e la pagina web
    def open(self):
        self.driver.get(self.url)

# preme il bottone del home
    def home(self):
        home_button = self.driver.find_element(By.ID, "home")
        home_button.click()
        
# preme il bottone per modificare un prodotto
    def modifica_prodotto_button(self):
        modifica_prodotto_button = self.driver.find_element(By.ID, "aggiungiProdotto")
        modifica_prodotto_button.click()

# metodo per compilare il form con i dati del prodotto da modificare
    def modifica_prodotto(self, nome, tipologia, descrizione, prezzo, quantita):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        descrizione_input = self.driver.find_element(By.ID, "descrizione")
        prezzo_input = self.driver.find_element(By.ID, "prezzo")
        quantita_input = self.driver.find_element(By.ID, "quantita")
    
        if nome:
            nome_input.clear()  
            nome_input.send_keys(nome)
        
        if tipologia:
            tipologia_input.clear()
            tipologia_input.send_keys(tipologia)
        
        if descrizione:
            descrizione_input.clear()
            descrizione_input.send_keys(descrizione)
        
        if prezzo:
            prezzo_input.clear()
            prezzo_input.send_keys(prezzo)
        
        if quantita:
            quantita_input.clear()
            quantita_input.send_keys(quantita)
            
        