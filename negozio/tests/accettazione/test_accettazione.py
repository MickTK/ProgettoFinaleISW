# classe di test
import unittest

from django.test import TestCase
import time

# framework
from selenium import webdriver


from tests.accettazione.pagine.registrazione_page import Registrazione
from tests.accettazione.pagine.login_page import Login
from tests.accettazione.pagine.home_page import Home
from tests.accettazione.pagine.home_page import Home_utente
from tests.accettazione.pagine.home_page import Home_amministratore
from tests.accettazione.pagine.carrello_page import Carrello
from tests.accettazione.pagine.checkout_page import Checkout

# ---------------------------------------------------
# BISOGNA METTERE time.sleep() E ORDINARE I TEST!!!!!
# ---------------------------------------------------

# Tempo generale
TIME_SLEEP = 5

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
    
    # TEST SULLA REGISTRAZIONE
    
    # test del registrazione con dati corretti
    def test_0_successful_registrazione(self):
        registrazione_page = Registrazione(self.driver)
        registrazione_page.registrazione("nuovoUssdddarfffname", "nuovaPassword")
        time.sleep(TIME_SLEEP)
        # assert per verificare il successo del registrazione
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP) 
        
    # test del registrazione con dati errati
    def test_a_failed_registrazione(self):
        registrazione_page = Registrazione(self.driver)
        registrazione_page.registrazione("cliente", "cliente")
        time.sleep(TIME_SLEEP)
        # assert per verificare il fallimento del registrazione
        expected_url = "http://127.0.0.1:8000/registrazione/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)    
        time.sleep(TIME_SLEEP)  

    # TEST SUL LOGIN
    
    # test del login con dati corretti
    def test_successful_login(self):
        login_page = Login(self.driver)
        login_page.login("cliente", "cliente")
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
        
    # test del logout con url corretto
    def test_successful_logout(self):
        home_utente_page = Home_utente(self.driver)
        home_utente_page.logout()
        # assert per verificare il successo del logout nella home utente
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)    
    
    # test del login con dati errati
    def test_failed_login(self):
        login_page = Login(self.driver)
        login_page.login("clicli", "cluclu")
        # assert per verificare il fallimento del login
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
        
    
    # test: prova ad aggiungere un prodotto presente nel negozio (stock)
    def test_successful_prodotto_aggiunto_al_carrello(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        carrello_page = Carrello(self.driver)
        login_page.login("cliente", "cliente")
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato = "1"
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato)
        
        # assert per verificare il il successo e l'aggiunta del prodotto al carrello
        # verifica se il prodotto è stato aggiunto al carrello
        home_utente_page.accedi_al_carrello()
        presente_nel_carrello = carrello_page.verifica_prodotto_nel_carrello("1")

        # assert per verificare che il prodotto sia presente nel carrello
        assert presente_nel_carrello  
        time.sleep(TIME_SLEEP)
        
    # test del login (amministratore) con dati corretti
    def test_successful_login_amministratore(self):
        login_page = Login(self.driver)
        login_page.login("admin", "admin")
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/Home_amministratore/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
          
        
    # test del login (amministratore) con dati corretti
    def test_failed_login_amministratore(self):
        login_page = Login(self.driver)
        login_page.login("cliente", "cliente")
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
             
        
    # test del logout con url corretto
    def test_successful_logout_amministratore(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        login_page.login("admin", "admin")
        home_amministratore_page.logout()
        # assert per verificare il successo del logout nella home amministratore
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)  
        
    
    # test rimuovi un prodotto dal carrello
    def test_rimuovi_prodotto_carrello(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        carrello_page = Carrello(self.driver)
        login_page.login("cliente", "cliente")  
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato = "1"
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato)
                
        home_utente_page.accedi_al_carrello()
        numInizialeQuantitaProdotto = carrello_page.verifica_prodotto_nel_carrello_rimosso("1")
    
        carrello_page.rimuovi_prodotto("1")
        numFinaleQuantitaProdotto = carrello_page.verifica_prodotto_nel_carrello_rimosso("1")

        # assert per verificare che il prodotto sia presente nel carrello
        self.assertGreater(numInizialeQuantitaProdotto, numFinaleQuantitaProdotto)
        time.sleep(TIME_SLEEP)
    
    
        
    # test per completare il checkout
    def test_completa_checkout(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        carrello_page = Carrello(self.driver)
        checkout_page = Checkout(self.driver)
        
        login_page.login("cliente", "cliente") 
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato = "1"
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato)
        
        home_utente_page.accedi_al_carrello()
        carrello_page.accedi_al_checkout()
        
        checkout_page.inserimento_dati("", "")
        checkout_page.ordina()
        checkout_page.inserimento_dati("Via Roma 18", "")
        checkout_page.ordina()
        checkout_page.reset_form_checkout()
        checkout_page.inserimento_dati("", "5455988754516532")
        checkout_page.ordina()
        checkout_page.reset_form_checkout()
        checkout_page.inserimento_dati("Via", "54559887")
        checkout_page.ordina()
        checkout_page.reset_form_checkout()
        checkout_page.inserimento_dati("Via Roma 18", "54559887")
        checkout_page.ordina()
        checkout_page.reset_form_checkout()
        checkout_page.inserimento_dati("Via Roma 18", "5455988754516532")
        checkout_page.ordina()
        
        # verifica checkout
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  
        time.sleep(TIME_SLEEP)
        
        
        
        
         
        
        
        
        
        
        

    def tearDown(self):
        pass 
