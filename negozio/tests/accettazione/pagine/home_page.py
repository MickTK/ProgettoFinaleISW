# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By

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
        logout_button.click()
        
class Home_utente(Home):
    # inizializza la classe
    def __init__(self, driver):
        url = "http://127.0.0.1:8000/home/"
        super().__init__(driver, url)
        
    # preme il bottone del logout
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        logout_button.click()    
    
    # aggiunge un prodotto al carrello
    def aggiungi_prodotto(self, prodotto_id):
        aggiungi_prodotto_button = self.driver.find_element(By.ID, f"aggiungi_prodotto_{prodotto_id}")
        aggiungi_prodotto_button.click()
        
    # accede al carrello
    def accedi_al_carrello(self):
        accedi_al_carrello_button = self.driver.find_element(By.ID, "accedi_carrello")
        accedi_al_carrello_button.click()    
    
    # filtra i prodotti
    def filtra_prodotti(self, nome, tipologia, minPrezzo, maxPrezzo):
        nome_input = self.driver.find_element(By.ID, "nome")
        tipologia_input = self.driver.find_element(By.ID, "tipologia")
        minPrezzo_input = self.driver.find_element(By.ID, "minPrezzo")
        maxPrezzo_input = self.driver.find_element(By.ID, "maxPrezzo")
        filtra_button = self.driver.find_element(By.ID, "filtra")
        
        nome_input.send_keys(nome)
        tipologia_input.send_keys(tipologia)
        minPrezzo_input.send_keys(minPrezzo)
        maxPrezzo_input.send_keys(maxPrezzo)
        filtra_button.click()
        
    # verifica se i prodotti sono tutti con lo stesso nome
    def verifica_filtro_nome(self, prodotto_nome):
        prodotti_presenti = self.driver.find_elements(By.CLASS_NAME, "prodotto")
        
        nomi = list()
        for element in prodotti_presenti:
            nome = (element.find_element(By.CLASS_NAME, "nome").text)
            nomi.append(nome)
            
        for nome in nomi:
            if nome.lower() != prodotto_nome.lower():
                return False
        return True          
      
        
        
        
        
        

class Home_amministratore(Home):
    # inizializza la classe
    def __init__(self, driver):
        url = "http://127.0.0.1:8000/Home_amministratore/"
        super().__init__(driver, url)
    
    # preme il bottone del logout
    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logout")
        logout_button.click()