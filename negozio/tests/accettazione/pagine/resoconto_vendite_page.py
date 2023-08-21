# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
import time

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 4

class ResocontoVendite:
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

# preme il bottone del filtro home amministratore
    def filtra(self):
        filtra_button = self.driver.find_element(By.ID, "filtra")
        time.sleep(TIME_SLEEP)
        
        filtra_button.click() 
        
# filtra i prodotti venduti nel resoconto vendite
    def filtra_prodotti(self, nome, tipologia, minPrezzo, maxPrezzo, minPezziVenduti, maxPezziVenduti):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        minPezziVenduti_input = self.driver.find_element(By.ID, "minPezziVenduti")
        maxPezziVenduti_input = self.driver.find_element(By.ID, "maxPezziVenduti")
        time.sleep(TIME_SLEEP)
        
        nome_input.send_keys(nome)
        time.sleep(TIME_SLEEP)
        tipologia_input.send_keys(tipologia)
        time.sleep(TIME_SLEEP)
        minPrezzo_input.send_keys(minPrezzo)
        time.sleep(TIME_SLEEP)
        maxPrezzo_input.send_keys(maxPrezzo)
        time.sleep(TIME_SLEEP)
        minPezziVenduti_input.send_keys(minPezziVenduti)
        time.sleep(TIME_SLEEP)
        maxPezziVenduti_input.send_keys(maxPezziVenduti)
        time.sleep(TIME_SLEEP)
        
    # pulire i campi del filtro nel resoconto vendite
    def reset_filtro_resoconto_vendite(self):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        minPezziVenduti_input = self.driver.find_element(By.ID, "minPezziVenduti")
        maxPezziVenduti_input = self.driver.find_element(By.ID, "maxPezziVenduti")
        time.sleep(TIME_SLEEP)
       
        nome_input.clear()
        tipologia_input.clear() 
        minPrezzo_input.clear()
        maxPrezzo_input.clear()
        minPezziVenduti_input.clear()
        maxPezziVenduti_input.clear()  
        
    # verifica se i prodotti sono tutti con lo stesso nome
    def verifica_filtro_nome(self, prodotto_nome):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodottoVenduto")
        
        nomi = list()
        for element in prodotti_presenti:
            nome = (element.find_element(By.CLASS_NAME, "nome").text)
            nomi.append(nome)
            
        for nome in nomi:
            if not (prodotto_nome.lower() in nome.lower()):
                return False
        return True  
    
    # verifica che il numero di pezzi venduti dei prodotti sia >= minPezziVenduti inserito nel filtro
    def verifica_filtro_minPezziVenduti(self, prodotto_minPezziVenduti):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodottoVenduto")
        
        lista_quantita = list()
        for element in prodotti_presenti:
            quantita = int(element.find_element(By.CLASS_NAME, "quantita").text)
            lista_quantita.append(quantita)
            
        for quantita in lista_quantita:
            if quantita < int(prodotto_minPezziVenduti):
                return False
        return True  