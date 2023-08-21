# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
import time

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 2

class Home:
    # inizializza la classe
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # apre il browser e la pagina web
    def open(self):
        self.driver.get(self.url)

    # preme il bottone del logout
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        time.sleep(TIME_SLEEP)
        
        logout_button.click()
        
        
        
        
class Home_utente(Home):
    # inizializza la classe
    def __init__(self, driver):
        url = "http://127.0.0.1:8000/home/"
        super().__init__(driver, url)
        
    # preme il bottone del logout
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        time.sleep(TIME_SLEEP)
        
        logout_button.click()    
    
    # aggiunge un prodotto al carrello
    def aggiungi_prodotto(self, prodotto_id):
        aggiungi_prodotto_button = self.driver.find_element(By.ID, f"aggiungi_prodotto_{prodotto_id}")
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_button.click()
        
    # accede al carrello
    def accedi_al_carrello(self):
        accedi_al_carrello_button = self.driver.find_element(By.ID, "accedi_carrello")
        time.sleep(TIME_SLEEP)
        
        accedi_al_carrello_button.click()   
    
    # preme il bottone del filtro home utente
    def filtra(self):
        filtra_button = self.driver.find_element(By.ID, "filtra")
        time.sleep(TIME_SLEEP)
        
        filtra_button.click() 
    
    # filtra i prodotti nella home utente
    def filtra_prodotti(self, nome, tipologia, minPrezzo, maxPrezzo):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        time.sleep(TIME_SLEEP)
        
        nome_input.send_keys(nome)
        time.sleep(TIME_SLEEP)
        
        tipologia_input.send_keys(tipologia)
        time.sleep(TIME_SLEEP)
        
        minPrezzo_input.send_keys(minPrezzo)
        time.sleep(TIME_SLEEP)
        
        maxPrezzo_input.send_keys(maxPrezzo)
        time.sleep(TIME_SLEEP)
        
    # verifica se i prodotti sono tutti con lo stesso nome
    def verifica_filtro_nome(self, prodotto_nome):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodotto")
        
        nomi = list()
        for element in prodotti_presenti:
            nome = (element.find_element(By.CLASS_NAME, "nome").text)
            nomi.append(nome)
            
        for nome in nomi:
            if not (prodotto_nome.lower() in nome.lower()):
                return False
        return True   
    
    
    # verifica che il prezzo dei prodotti sia >= minPrezzo inserito nel filtro
    def verifica_filtro_minPrezzo(self, prodotto_minPrezzo):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodotto")
        
        prezzi = list()
        for element in prodotti_presenti:
            prezzo = float(element.find_element(By.CLASS_NAME, "prezzo").text)
            prezzi.append(prezzo)
            
        for prezzo in prezzi:
            if prezzo < float(prodotto_minPrezzo):
                return False
        return True  
    

    # pulire i campi del filtro nella home utente
    def reset_filtro_home_utente(self):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        time.sleep(TIME_SLEEP)
       
        nome_input.clear()
        tipologia_input.clear() 
        minPrezzo_input.clear()
        maxPrezzo_input.clear()      
      
      
      
class Home_amministratore(Home):
    # inizializza la classe
    def __init__(self, driver):
        url = "http://127.0.0.1:8000/Home_amministratore/"
        super().__init__(driver, url)
    
    # preme il bottone del logout
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        time.sleep(TIME_SLEEP)
        
        logout_button.click()
        
    def aggiungi_prodotto(self):
        aggiungi_prodotto_button = self.driver.find_element(By.ID, "aggiungiProdotto")
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_button.click() 
        
    # aggiunge un prodotto al carrello
    def modifica_prodotto(self, prodotto_id):
        modifica_prodotto_button = self.driver.find_element(By.ID, f"modifica_prodotto_{prodotto_id}")
        time.sleep(TIME_SLEEP)
        
        modifica_prodotto_button.click()
        
    def resoconto_vendite(self):
        resoconto_vendite_button = self.driver.find_element(By.ID, "resocontoVendite")
        time.sleep(TIME_SLEEP)
        
        resoconto_vendite_button.click() 
    
    # preme il bottone del filtro home amministratore
    def filtra(self):
        filtra_button = self.driver.find_element(By.ID, "filtra")
        time.sleep(TIME_SLEEP)
        
        filtra_button.click() 
        
    # filtra i prodotti nella home amministratore
    def filtra_prodotti_amministratore(self, nome, tipologia, minPrezzo, maxPrezzo, minNumPezzi, maxNumPezzi):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        minNumPezzi_input = self.driver.find_element(By.ID, "minNumPezzi")
        maxNumPezzi_input = self.driver.find_element(By.ID, "maxNumPezzi")
        time.sleep(TIME_SLEEP)
        
        nome_input.send_keys(nome)
        time.sleep(TIME_SLEEP)
        
        tipologia_input.send_keys(tipologia)
        time.sleep(TIME_SLEEP)
        
        minPrezzo_input.send_keys(minPrezzo)
        time.sleep(TIME_SLEEP)
        
        maxPrezzo_input.send_keys(maxPrezzo)
        time.sleep(TIME_SLEEP)
        
        minNumPezzi_input.send_keys(minNumPezzi)
        time.sleep(TIME_SLEEP)
        
        minNumPezzi_input.send_keys(maxNumPezzi)
        time.sleep(TIME_SLEEP)
        
    # verifica se i prodotti sono tutti con lo stesso nome
    def verifica_filtro_nome(self, prodotto_nome):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodotto")
        
        nomi = list()
        for element in prodotti_presenti:
            nome = (element.find_element(By.CLASS_NAME, "nome").text)
            nomi.append(nome)
            
        for nome in nomi:
            if not (prodotto_nome.lower() in nome.lower()):
                return False
        return True  
    
    # Controlla se un dato nome appare nel negozio come prodotto
    def verifica_presenza_in_negozio(self, nome_cercato):
        prodotti = self.driver.find_elements(By.CLASS_NAME, "prodotto")
        for prodotto in prodotti:
            nome_prodotto = (prodotto.find_element(By.CLASS_NAME, "nome").text)
            if nome_prodotto.lower() == nome_cercato.lower():
                return True
        return False
    

    # verifica che il numero di pezzi disponibili dei prodotti sia >= minNumPezzi inserito nel filtro
    def verifica_filtro_minNumPezzi(self, prodotto_minNumPezzi):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodotto")
        
        lista_quantita = list()
        for element in prodotti_presenti:
            quantita = int(element.find_element(By.CLASS_NAME, "quantita").text)
            lista_quantita.append(quantita)
            
        for quantita in lista_quantita:
            if quantita < int(prodotto_minNumPezzi):
                return False
        return True    
    
    # pulire i campi del filtro nella home amminsitratore
    def reset_filtro_home_amministratore(self):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        minNumPezzi_input = self.driver.find_element(By.ID, "minNumPezzi")
        maxNumPezzi_input = self.driver.find_element(By.ID, "maxNumPezzi")
        time.sleep(TIME_SLEEP)
       
        nome_input.clear()
        tipologia_input.clear() 
        minPrezzo_input.clear()
        maxPrezzo_input.clear()
        minNumPezzi_input.clear()
        maxNumPezzi_input.clear()      
    
    
        
      