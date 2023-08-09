# classe di test
import unittest

# framework
from selenium import webdriver

from pagine.home_page import Home
from pagine.home_page import Home_utente
from pagine.home_page import Home_amministratore

from pagine.login_page import Login
from pagine.carrello_page import Carrello

class TestAggiungiProdottoAlCarrello(unittest.TestCase):
    # inizializza il driver e l'istanza della classe home utente
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.login_page = Login(self.driver)
        self.home_utente_page = Home_utente(self.driver)
        self.carrello_page = Carrello(self.driver)



    # test: prova ad aggiungere un prodotto presente nel negozio (stock)
    def test_successful_prodotto_aggiunto_al_carrello(self):
        self.login_page.login("cliente", "cliente")
        
        # aggiunta di un prodotto al carrello
        prodotto_id_desiderato = "1"
        self.home_utente_page.aggiungi_prodotto(prodotto_id_desiderato)
        
        # assert per verificare il il successo e l'aggiunta del prodotto al carrello
        # verifica se il prodotto è stato aggiunto al carrello
        self.home_utente_page.accedi_al_carrello()
        presente_nel_carrello = self.carrello_page.verifica_prodotto_nel_carrello("1")

        # assert per verificare che il prodotto sia presente nel carrello
        assert presente_nel_carrello
        
        
        
        

    # chiusura del driver
    def tearDown(self):
        self.driver.quit()



# serve per eseguire il test quando il modulo è eseguito direttamente come script
if __name__ == '__main__':
    unittest.main()