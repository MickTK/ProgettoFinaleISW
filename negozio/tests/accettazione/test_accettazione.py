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
from tests.accettazione.pagine.aggiungi_prodotto_page import AggiungiProdotto
from tests.accettazione.pagine.modifica_prodotto_page import ModificaProdotto
from tests.accettazione.pagine.resoconto_vendite_page import ResocontoVendite

# Tempo generale
global TIME_SLEEP
TIME_SLEEP = 4

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
    def test_00_successful_registrazione(self):
        registrazione_page = Registrazione(self.driver)
        time.sleep(TIME_SLEEP) 
        
        registrazione_page.registrazione("nuovoUtente", "nuovaPassword")
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il successo del registrazione
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP) 
        
        
    # test del registrazione con dati errati
    def test_01_failed_registrazione(self):
        registrazione_page = Registrazione(self.driver)
        time.sleep(TIME_SLEEP) 
        
        registrazione_page.registrazione("cliente", "cliente")
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il fallimento del registrazione
        expected_url = "http://127.0.0.1:8000/registrazione/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)    
        time.sleep(TIME_SLEEP)  


    # TEST SUL LOGIN
    
    # test del login con dati corretti
    def test_02_successful_login(self):
        login_page = Login(self.driver)
        time.sleep(TIME_SLEEP) 
        
        login_page.login("cliente", "cliente")
        time.sleep(TIME_SLEEP) 
        
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
        
        
    # test del login con username errato
    def test_03_failed_login_username(self):
        login_page = Login(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("clicli", "cluclu")
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il fallimento del login
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
    
    # test del login con password errata
    def test_04_failed_login_passw(self):
        login_page = Login(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("cliente", "cluclu")
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il fallimento del login
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
        
        
    # test del logout con url corretto
    def test_05_successful_logout(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        time.sleep(TIME_SLEEP) 
        
        login_page.login("cliente", "cliente")
        time.sleep(TIME_SLEEP)
        
        home_utente_page.logout()
        time.sleep(TIME_SLEEP) 
        
        # assert per verificare il successo del logout nella home utente
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)    
       
    
    # test: prova ad aggiungere un prodotto presente nel negozio (stock)
    def test_06_successful_prodotto_aggiunto_al_carrello(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        carrello_page = Carrello(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("cliente", "cliente")
        time.sleep(TIME_SLEEP)
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato_1 = "1"
        prodotto_id_desiderato_2 = "3"
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato_1)
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato_2)
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato_2)
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il il successo e l'aggiunta del prodotto al carrello
        # verifica se il prodotto è stato aggiunto al carrello
        home_utente_page.accedi_al_carrello()
        presente_nel_carrello_1 = carrello_page.verifica_prodotto_nel_carrello("1")
        presente_nel_carrello_2 = carrello_page.verifica_prodotto_nel_carrello("3")
        time.sleep(TIME_SLEEP)
        

        # assert per verificare che il prodotto sia presente nel carrello
        assert presente_nel_carrello_1  
        assert presente_nel_carrello_2
        time.sleep(TIME_SLEEP)
       
        
    # test rimuovi un prodotto dal carrello
    def test_07_rimuovi_prodotto_carrello(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        carrello_page = Carrello(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("cliente", "cliente")  
        time.sleep(TIME_SLEEP)
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato = "1"
        prodotto_id_desiderato_2 = "3"
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato)
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato_2)
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato_2)

        time.sleep(TIME_SLEEP)
                
        home_utente_page.accedi_al_carrello()
        numInizialeQuantitaProdotto = carrello_page.verifica_prodotto_nel_carrello_rimosso("1")
        numInizialeQuantitaProdotto_2 = carrello_page.verifica_prodotto_nel_carrello_rimosso("3")
        time.sleep(TIME_SLEEP)
    
        carrello_page.rimuovi_prodotto("1")
        carrello_page.rimuovi_prodotto("3")
        carrello_page.rimuovi_prodotto("3")
        numFinaleQuantitaProdotto = carrello_page.verifica_prodotto_nel_carrello_rimosso("1")
        numFinaleQuantitaProdotto_2 = carrello_page.verifica_prodotto_nel_carrello_rimosso("1")
        time.sleep(TIME_SLEEP)

        # assert per verificare che il prodotto sia presente nel carrello
        self.assertGreater(numInizialeQuantitaProdotto, numFinaleQuantitaProdotto)
        self.assertGreater(numInizialeQuantitaProdotto_2, numFinaleQuantitaProdotto_2)
        time.sleep(TIME_SLEEP)  
       
    # test per completare il checkout
    def test_08_completa_checkout(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        carrello_page = Carrello(self.driver)
        checkout_page = Checkout(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("cliente", "cliente") 
        time.sleep(TIME_SLEEP)
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato = "1"
        home_utente_page.aggiungi_prodotto(prodotto_id_desiderato)
        time.sleep(TIME_SLEEP)
        
        home_utente_page.accedi_al_carrello()
        time.sleep(TIME_SLEEP)
        
        carrello_page.accedi_al_checkout()
        time.sleep(TIME_SLEEP)
        
        checkout_page.inserimento_dati("", "")
        time.sleep(TIME_SLEEP)
        checkout_page.ordina()
        time.sleep(TIME_SLEEP)
        checkout_page.inserimento_dati("Via Roma 18", "")
        time.sleep(TIME_SLEEP)
        checkout_page.ordina()
        time.sleep(TIME_SLEEP)
        checkout_page.reset_form_checkout()
        time.sleep(TIME_SLEEP)
        checkout_page.inserimento_dati("", "5455988754516532")
        time.sleep(TIME_SLEEP)
        checkout_page.ordina()
        time.sleep(TIME_SLEEP)
        checkout_page.reset_form_checkout()
        time.sleep(TIME_SLEEP)
        checkout_page.inserimento_dati("Via", "54559887")
        time.sleep(TIME_SLEEP)
        checkout_page.ordina()
        time.sleep(TIME_SLEEP)
        checkout_page.reset_form_checkout()
        time.sleep(TIME_SLEEP)
        checkout_page.inserimento_dati("Via Roma 18", "54559887")
        time.sleep(TIME_SLEEP)
        checkout_page.ordina()
        time.sleep(TIME_SLEEP)
        checkout_page.reset_form_checkout()
        time.sleep(TIME_SLEEP)
        checkout_page.inserimento_dati("Via Roma 18", "5455988754516532")
        time.sleep(TIME_SLEEP)
        checkout_page.ordina()
        time.sleep(TIME_SLEEP)
        
        # verifica checkout
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url)  
        time.sleep(TIME_SLEEP)      
        
        
    # test del login (amministratore) con dati corretti
    def test_09_successful_login_amministratore(self):
        login_page = Login(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/Home_amministratore/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
          
        
    # test del login (amministratore) con dati corretti
    def test_10_failed_login_amministratore(self):
        login_page = Login(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("cliente", "cliente")
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il successo del login
        expected_url = "http://127.0.0.1:8000/home/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
             
        
    # test del logout con url corretto
    def test_11_successful_logout_amministratore(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)
        
        home_amministratore_page.logout()
        time.sleep(TIME_SLEEP)
        
        # assert per verificare il successo del logout nella home amministratore
        expected_url = "http://127.0.0.1:8000/login/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)  
    
        
    # test del filtro nella home utente
    def test_12_filtro_home_utente(self):
        login_page = Login(self.driver)
        home_utente_page = Home_utente(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("cliente", "cliente")
        time.sleep(TIME_SLEEP)
        
        home_utente_page.filtra_prodotti("Iphone", "", "200.00", "")
        time.sleep(TIME_SLEEP) 
        
        home_utente_page.filtra()
        time.sleep(TIME_SLEEP) 
        
        risultato_nome = home_utente_page.verifica_filtro_nome("Iphone 14")
        
        # home_utente_page.reset_filtro_home_utente()
        
        # home_utente_page.filtra_prodotti("", "", "600.00", "")
        risultato_minPrezzo = home_utente_page.verifica_filtro_minPrezzo("200.00")
        time.sleep(TIME_SLEEP) 
        
        assert risultato_nome
        assert risultato_minPrezzo
        
        time.sleep(TIME_SLEEP) 
    
    
    # test del filtro nella home amministratore
    def test_13_filtro_home_amministratore(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)
        
        home_amministratore_page.filtra_prodotti_amministratore("Iphone", "", "", "", "6", "")
        time.sleep(TIME_SLEEP) 
        
        home_amministratore_page.filtra()
        time.sleep(TIME_SLEEP) 
        
        risultato_nome = home_amministratore_page.verifica_filtro_nome("Iphone 14")
        risultato_minNumPezzi = home_amministratore_page.verifica_filtro_minNumPezzi("6")
        time.sleep(TIME_SLEEP) 
        
        assert risultato_nome
        assert risultato_minNumPezzi
        
        time.sleep(TIME_SLEEP) 
    
    
    # test inserimento nuovo prodotto (aggiungi prodotto - amministratore)
    def test_14_aggiungi_prodotto(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        aggiungi_prodotto_page = AggiungiProdotto(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)    
        
        home_amministratore_page.aggiungi_prodotto()
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.reset_campi_aggiungi_prodotto()
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.aggiungi_prodotto("Ventyl 15", "Ventilatore", "Un bel ventilatore", "7500", "10")
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.aggiungi_prodotto_button()
        time.sleep(TIME_SLEEP)
        
        risultato_nome = home_amministratore_page.verifica_presenza_in_negozio("Ventyl 15")
        time.sleep(TIME_SLEEP)
        
        assert risultato_nome
        
    # test inserimento nuovo prodotto senza inserire tutti i campi
    def test_15_aggiungi_prodotto_error(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        aggiungi_prodotto_page = AggiungiProdotto(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)    
        
        home_amministratore_page.aggiungi_prodotto()
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.reset_campi_aggiungi_prodotto()
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.aggiungi_prodotto("Ventyl 15", "Ventilatore", "", "", "")
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.aggiungi_prodotto_button()
        time.sleep(TIME_SLEEP)
        
        # assert per verificare che l'operazione sia andata a buon fine (deve restare nella pagina aggiungi prodotto)
        expected_url = "http://127.0.0.1:8000/Aggiungi_prodotto/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
        
        # test inserimento nuovo prodotto inserendo la quantità = 0
    def test_16_aggiungi_prodotto_error_quantita(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        aggiungi_prodotto_page = AggiungiProdotto(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)    
        
        home_amministratore_page.aggiungi_prodotto()
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.reset_campi_aggiungi_prodotto()
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.aggiungi_prodotto("Scrivany 845", "Scrivania moderna", "Una bella scrivania costosa", "7500", "0")
        time.sleep(TIME_SLEEP)
        
        aggiungi_prodotto_page.aggiungi_prodotto_button()
        time.sleep(TIME_SLEEP)
        
        # assert per verificare che l'operazione sia andata a buon fine (deve restare nella pagina aggiungi prodotto)
        expected_url = "http://127.0.0.1:8000/Aggiungi_prodotto/"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url) 
        time.sleep(TIME_SLEEP)
    
    
    # test modifica prodotto (modifica prodotto - amministratore)
    def test_17_modifica_prodotto(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        modifica_prodotto_page = ModificaProdotto(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP) 
        
        # bisogna prima aggiungere un prodotto lato amministratore, poi modificare la riga sotto ("1" --> prodotto appena aggiunto)
        
        home_amministratore_page.modifica_prodotto("1")
        time.sleep(TIME_SLEEP)
        
        modifica_prodotto_page.modifica_prodotto("Iphone 20", "", "", "", "30")
        time.sleep(TIME_SLEEP)
        
        modifica_prodotto_page.modifica_prodotto_button()
        time.sleep(TIME_SLEEP)
        
        risultato_nome = home_amministratore_page.verifica_presenza_in_negozio("Iphone 20")
        time.sleep(TIME_SLEEP)
    
        
        assert risultato_nome
        
    def test_18_modifica_prodotto_quantita_zero(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        modifica_prodotto_page = ModificaProdotto(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP) 
        
        # bisogna prima aggiungere un prodotto lato amministratore, poi modificare la riga sotto ("1" --> prodotto appena aggiunto)
        
        home_amministratore_page.modifica_prodotto("1")
        time.sleep(TIME_SLEEP)
        
        modifica_prodotto_page.modifica_prodotto("Iphone 20", "", "", "", "0")
        time.sleep(TIME_SLEEP)
        
        modifica_prodotto_page.modifica_prodotto_button()
        time.sleep(TIME_SLEEP)
        
        risultato_nome = home_amministratore_page.verifica_presenza_in_negozio("Iphone 20")
        time.sleep(TIME_SLEEP)
        
        
        
        assert not risultato_nome
        
    
    # test del filtro nella home amministratore
    def test_19_filtro_resoconto_vendite(self):
        login_page = Login(self.driver)
        home_amministratore_page = Home_amministratore(self.driver)
        resoconto_vendite_page = ResocontoVendite(self.driver)
        time.sleep(TIME_SLEEP)
        
        login_page.login("admin", "admin")
        time.sleep(TIME_SLEEP)
        
        home_amministratore_page.resoconto_vendite()
        time.sleep(TIME_SLEEP) 
        
        resoconto_vendite_page.filtra_prodotti("Playstation 5", "", "", "", "1", "")
        time.sleep(TIME_SLEEP) 
        
        resoconto_vendite_page.filtra()
        time.sleep(TIME_SLEEP)
        
        risultato_nome = resoconto_vendite_page.verifica_filtro_nome("Playstation 5")
        risultato_minNumPezzi = resoconto_vendite_page.verifica_filtro_minPezziVenduti("1")
        time.sleep(TIME_SLEEP) 
        
        assert risultato_nome
        assert risultato_minNumPezzi
        
        time.sleep(TIME_SLEEP) 
        
        
        
        
        
    def tearDown(self):
        pass 
