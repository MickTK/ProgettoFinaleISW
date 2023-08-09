# classe di test
import unittest

# framework
from selenium import webdriver

from pagine.login_page import Login

class TestLogin(unittest.TestCase):
    # inizializza il driver e l'istanza della classe login
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = Login(self.driver)

    # test del login con dati corretti
    def test_successful_login(self):
        self.login_page.login("cliente", "cliente")
        # Aggiungi gli assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  

    # test del login con dati errati
    def test_failed_login(self):
        self.login_page.login("clicli", "cluclu")
        # Aggiungi gli assert per verificare il fallimento del login
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  

    # chiusura del driver
    def tearDown(self):
        self.driver.quit()

# serve per eseguire il test quando il modulo è eseguito direttamente come script
if __name__ == '__main__':
    unittest.main()