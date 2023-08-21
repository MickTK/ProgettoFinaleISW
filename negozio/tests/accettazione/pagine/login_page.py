# Utile per individuare elementi html in una pagina
from selenium.webdriver.common.by import By
import time

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 0

class Login:
    # inizializza la classe
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://127.0.0.1:8000/login/"

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

    # preme il tasto per fare il Login
    def click_login(self):
        login = self.driver.find_element(By.ID, "login")
        time.sleep(TIME_SLEEP)
        
        login.click()
        
    # preme il link per andare nella pagina della registrazione    
    def click_link_registrazione(self):
        link_registrazione = self.driver.find_element(By.ID, "registrazione")
        time.sleep(TIME_SLEEP)
        
        link_registrazione.click()
        
    # corpo della funzione principale
    def login(self, username, password):
        self.open()
        self.inserimento_credenziali(username, password)
        self.click_login()