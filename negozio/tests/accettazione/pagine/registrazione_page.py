# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
import time

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 2

class Registrazione:
    # inizializza la classe
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:8000/registrazione/"

    # apre il browser e la pagina web
    def open(self):
        self.driver.get(self.url)

    # inserisce le credenziali
    def inserimento_credenziali(self, username, password):
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")
        time.sleep(TIME_SLEEP)

        username_input.send_keys(username)
        time.sleep(TIME_SLEEP)
        
        password_input.send_keys(password)
        time.sleep(TIME_SLEEP)

    # preme il tasto per registrarsi
    def click_registrati(self):
        registrati = self.driver.find_element(By.ID, "registrati")
        time.sleep(TIME_SLEEP)
        
        registrati.click()
    
    def click_login(self):
        login = self.driver.find_element(By.ID, "login")
        time.sleep(TIME_SLEEP)
        
        login.click()
        
    # corpo della funzione principale
    def registrazione(self, username, password):
        self.open()
        self.inserimento_credenziali(username, password)
        self.click_registrati()
        
    # pulire i campi del filtro nella home amminsitratore
    def reset_campi_registrazione(self):
        username_input = self.driver.find_element(By.ID, "username")
        password_input = self.driver.find_element(By.ID, "password")

        username_input.clear()
        password_input.clear()
        
        