# classe di test
import unittest

# framework
from selenium import webdriver

from pagine.login_page import Login

    # inizializza il driver e l'istanza della classe login

    # test del login con dati corretti
    

    # test del login con dati errati
    def test_failed_login(self):
        self.login_page.login("clicli", "cluclu")
        # assert per verificare il fallimento del login
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  

    # chiusura del driver
    def tearDown(self):
        self.driver.quit()

# serve per eseguire il test quando il modulo è eseguito direttamente come script
if __name__ == '__main__':
    unittest.main()