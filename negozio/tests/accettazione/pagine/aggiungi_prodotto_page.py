# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
import time

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 0

class AggiungiProdotto:
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
        time.sleep(TIME_SLEEP)
        
        home_button.click()
    
    # preme il bottone per aggiungere un prodotto
    def aggiungi_prodotto_button(self):
        aggiungi_prodotto_button = self.driver.find_element(By.ID, "aggiungiProdotto")
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_button.click()
    
    # metodo per compilare il form con i dati del prodotto da aggiungere
    def aggiungi_prodotto(self, nome, tipologia, descrizione, prezzo, quantita):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        descrizione_input = self.driver.find_element(By.ID, "descrizione")
        prezzo_input = self.driver.find_element(By.ID, "prezzo")
        quantita_input = self.driver.find_element(By.ID, "quantita")
        time.sleep(TIME_SLEEP)
        
        nome_input.send_keys(nome)
        time.sleep(TIME_SLEEP)
        
        tipologia_input.send_keys(tipologia)
        time.sleep(TIME_SLEEP)
        
        descrizione_input.send_keys(descrizione)
        time.sleep(TIME_SLEEP)
        
        prezzo_input.send_keys(prezzo)
        time.sleep(TIME_SLEEP)
        
        quantita_input.send_keys(quantita)
        time.sleep(TIME_SLEEP)

    # metodo completo per aggiungere un prodotto nel negozio
    def aggiungi_un_prodotto_nel_negozio(self, nome, tipologia, descrizione, prezzo, quantita):
        self.aggiungi_prodotto(nome, tipologia, descrizione, prezzo, quantita)
        self.aggiungi_prodotto_button()
        self.home()
    
    # metodo per resettare i campi del form utilizzato per aggiungere un oggetto
    def reset_campi_aggiungi_prodotto(self):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        descrizione_input = self.driver.find_element(By.ID, "descrizione")
        prezzo_input = self.driver.find_element(By.ID, "prezzo")
        quantita_input = self.driver.find_element(By.ID, "quantita")
        time.sleep(TIME_SLEEP)
        
        
        nome_input.clear()
        tipologia_input.clear()
        descrizione_input.clear()
        prezzo_input.clear()
        quantita_input.clear()
        