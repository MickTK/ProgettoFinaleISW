# classe di test
import unittest

# framework
from selenium import webdriver

from pagine.home_page import Home
from pagine.home_page import Home_utente
from pagine.home_page import Home_amministratore

from pagine.login_page import Login

class TestLogout(unittest.TestCase):
    # inizializza il driver e l'istanza della classe home utente
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = Login(self.driver)
        self.home_utente_page = Home_utente(self.driver)

    # test del logout con url corretto
    def test_successful_logout(self):
        self.login_page.login("cliente", "cliente")
        self.home_utente_page.logout()
        # Aggiungi gli assert per verificare il successo del logout
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  

    # chiusura del driver
    def tearDown(self):
        self.driver.quit()


# inizializza il driver e l'istanza della classe home amministratore
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = Login(self.driver)
        self.home_amministratore_page = Home_amministratore(self.driver)

    # test del logout con url corretto
    def test_successful_logout(self):
        self.login_page.login("admin", "admin")
        self.home_amministratore_page.logout()
        # Aggiungi gli assert per verificare il successo del logout
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)   

    # chiusura del driver
    def tearDown(self):
        self.driver.quit()
        



# serve per eseguire il test quando il modulo è eseguito direttamente come script
if __name__ == '__main__':
    unittest.main()