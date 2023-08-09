# classe di test
import unittest

# framework
from selenium import webdriver

from pagine.registrazione_page import Registrazione

class TestRegistrazione(unittest.TestCase):
    # inizializza il driver e l'istanza della classe registrazione
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.registrazione_page = Registrazione(self.driver)

    # test del registrazione con dati corretti
    def test_successful_registrazione(self):
        self.registrazione_page.registrazione("Cberererererererererere", "lolop")
        # Aggiungi gli assert per verificare il successo del registrazione
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  

    # test del registrazione con dati errati
    def test_failed_registrazione(self):
        self.registrazione_page.registrazione("cliente", "cliente")
        # Aggiungi gli assert per verificare il fallimento del registrazione
        expected_url = "http://127.0.0.1:8000/registrazione/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  

    # chiusura del driver
    def tearDown(self):
        self.driver.quit()

# serve per eseguire il test quando il modulo è eseguito direttamente come script
if __name__ == '__main__':
    unittest.main()