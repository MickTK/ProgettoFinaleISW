# classe di test
import unittest

from django.test import TestCase
import time

# framework
from selenium import webdriver

'''
from test.test_login import TestLogin
from test.test_registrazione import TestRegistrazione
from test.test_logout import TestLogout
from test.test_aggiungi_prodotto_al_carrello import TestAggiungiProdottoAlCarrello '''

from tests.accettazione.pagine.login_page import Login


class AccettazioneTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        # Inizializza il browser   
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        # Chiudi il browser
        cls.driver.quit()
    

    def setUp(self):
        pass

    def test_successful_login(self):
        login_page = Login(self.driver)
        login_page.login("cliente", "cliente")
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  
        time.sleep(10)

    def tearDown(self):
        pass 

'''if __name__ == '__main__':
    # Inizializza il browser
    #driver = webdriver.Chrome()

    # Inizializza il runner dei test
    test_runner = unittest.TextTestRunner()

    # Esegue i test
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(TestAggiungiProdottoAlCarrello))
    #suite.addTest(unittest.makeSuite(TestLogout))
    #suite.addTest(unittest.makeSuite(TestRegistrazione))
    suite.addTest(unittest.makeSuite(TestLogin))
    

    result = test_runner.run(suite)

    # Chiudi il browser
    driver.quit() '''