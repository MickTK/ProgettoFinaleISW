from django.test import TestCase 
from django.contrib.auth.models import User 
from django.urls import reverse 
from applicazione.views import * 
from applicazione.models import * 
from applicazione.forms import *

REDIRECT_STATUS_CODE = 302

#================================================
# Condivise
#================================================

class LoginViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username = "provacl", password = "passwcli")
        Stock.objects.create(nome = NOME_STOCK)

    def test_login_view_valid(self):
        # Cerca e trova la pagina di login 
        response = self.client.get("/login/") 
        self.assertEqual(response.status_code, 200) 
 
        # Esegue l'accesso tramite le credenziali di un cliente 
        data = { 
            "username": "provacl", 
            "password": "passwcli", 
        } 
        response = self.client.post("/login/", data) 
        self.assertRedirects(response, "/home/") 

    def test_login_view_invalid(self): 
        # Cerca e trova la pagina di login 
        response = self.client.get("/login/") 
        self.assertEqual(response.status_code, 200) 

        # Non esegue l'accesso perché le credenziali sono errate 
        data = { 
            "username": "pippo", 
            "password": "baudo", 
        } 
        response = self.client.post("/login/", data) 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono vuote 
        data = { } 
        response = self.client.post("/login/", data) 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, manca password
        data = { 
            "username": "provacl", 
            "password": "", 
        } 
        response = self.client.post("/login/", data) 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, manca username
        data = { 
            "username": "", 
            "password": "passwcli", 
        } 
        response = self.client.post("/login/", data) 
        self.assertEqual(response.status_code, 200)

#================================================
# Utente
#================================================

class HomeViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username = "testuser", password = "testpassword") 
        self.stock = Stock.objects.create(nome = NOME_STOCK)
        self.stock.aggiungi_nuovo_prodotto(
          "Motorino",
          "Veicolo",
          "Motorino elettrico ecologico.",
          499.99,
          25
        )

        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        self.client.post("/login/", data)

    def test_home_view_valid(self):

        # Cerca e trova la pagina di registrazione
        response = self.client.get("/home/") 
        self.assertEqual(response.status_code, 200)
        num_prodotti = len(response.context["prodotti"]) # Salvo 

        data = { 
            "nome": "", 
            "tipologia": "", 
            "minPrezzo": "", 
            "maxPrezzo": "", 
        }
        
        response = self.client.post("/home/", data)
        contatore = len(response.context["prodotti"])        
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(contatore, num_prodotti)

        # Filtro per tipologia

        data = { 
            "nome": "", 
            "tipologia": "Telefono", 
            "minPrezzo": "", 
            "maxPrezzo": "", 
        }
        
        response = self.client.post("/home/", data)
        contatore = len(response.context["prodotti"])        
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(contatore, 0)

        # Aggiungo due prodotti

        self.stock.aggiungi_nuovo_prodotto(
          "Iphone 10",
          "Telefono",
          "Un telefono bello",
          599.99,
          5
        )

        self.stock.aggiungi_nuovo_prodotto(
          "Iphone 14",
          "Telefono",
          "Un telefono molto più bello",
          899.99,
          4
        )

        data = { 
            "nome": "IphOne", 
            "tipologia": "TElefono", 
            "minPrezzo": "", 
            "maxPrezzo": "", 
        }

        response = self.client.post("/home/", data)
        contatore = len(response.context["prodotti"])        
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(contatore, 2)

class RegistrazioneViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username = "testuser", password = "testpassword") 
        Stock.objects.create(nome = NOME_STOCK) 

    def test_registrazione_view_valid(self):

        # Cerca e trova la pagina di registrazione
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200) 

        # Esegue l'accesso tramite le credenziali di un cliente 
        data = {
            "username": "pippo",
            "password": "testpassword",
        }
        response = self.client.post("/registrazione/", data) 
        self.assertRedirects(response, "/home/")

    def test_registrazione_view_invalid(self):
        
        # Cerca e trova la pagina di registrazione
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200) 

        # Non esegue l'accesso perché le credenziali sono errate, stesso username ma password diversa
        data = { 
            "username": "testuser", 
            "password": "altra_password", 
        }
        response = self.client.post("/registrazione/", data) 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono vuote 
        data = {}
        response = self.client.post("/registrazione/", data) 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, manca password
        data = { 
            "username": "testuser", 
            "password": "", 
        }
        response = self.client.post("/registrazione/", data) 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, manca username
        data = { 
            "username": "", 
            "password": "testpassword", 
        }
        response = self.client.post("/registrazione/", data) 
        self.assertEqual(response.status_code, 200)

class CarrelloViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username = "testuser", password = "testpassword") 
        self.carrello = Carrello.objects.create(user = user)
        self.stock = Stock.objects.create(nome = NOME_STOCK)
        self.prodotto = self.stock.aggiungi_nuovo_prodotto(
          "Motorino",
          "Veicolo",
          "Motorino elettrico ecologico.",
          499.99,
          25
        )  

    def test_carrello_view_valid(self):

        # Effettuo il login
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        self.client.post("/login/", data)

        # Cerca e trova la pagina del carrello
        response = self.client.get("/carrello/") 
        self.assertEqual(response.status_code, 200)

        # Visualizzo il carrello
        self.assertEqual(len(response.context["prodottiCarrello"]), 0)

        # Aggiungo un prodotto al carrello
        self.carrello.aggiungi_prodotto(self.prodotto, 1)

        # Ricarico la pagina e verifico che il prodotto è aumentato
        response = self.client.get("/carrello/")
        self.assertEqual(len(response.context["prodottiCarrello"]), 1)

        # Vendo il prodotto
        for prodotto_carrello in self.carrello.prodotti.all() :
            prodotto_carrello.acquista()
        
        # Ricarico la pagina e verifico che il prodotto è aumentato
        response = self.client.get("/carrello/")
        self.assertEqual(len(response.context["prodottiCarrello"]), 0)

    def test_carrello_view_invalid(self):

        # Cerca la pagina del carrello
        response = self.client.get("/carrello/") 
        # Non essendo autenticato torno al login
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE) #loginrequired

class CheckoutViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username = "testuser", password = "testpassword") 
        self.carrello = Carrello.objects.create(user = user)
        self.stock = Stock.objects.create(nome = NOME_STOCK)
        self.prodotto = self.stock.aggiungi_nuovo_prodotto(
          "Motorino",
          "Veicolo",
          "Motorino elettrico ecologico.",
          499.99,
          25
        )

    def test_checkout_view_valid(self):

        # Effettuo il login
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        self.client.post("/login/", data)

        self.carrello.aggiungi_prodotto(self.prodotto, 1)

        # Cerca e trova la pagina del checkout
        response = self.client.get("/checkout/") 
        self.assertEqual(response.status_code, 200)

        # Dati form
        data = {
            "indirizzo": "Via Roma",
            "codice_paypal": "1243142409121414"
        }
        response = self.client.post("/checkout/", data, follow = True)
        self.assertRedirects(response, "/home/")

    def test_checkout_view_invalid(self):

        # Cerca la pagina del checkout
        response = self.client.get("/checkout/") 
        # Non essendo autenticato torno al login
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE) #loginrequired

        # Effettuo il login
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        self.client.post("/login/", data)

        # Cerca e trova la pagina del checkout
        response = self.client.get("/checkout/") 
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE) 

        # Dati form
        data = {
            "indirizzo": "Via Roma",
            "codice_paypal": "7632"
        }

        # I dati del form sono sbagliati
        response = self.client.post("/checkout/", data)
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE) 

#================================================
# Amministratore
#================================================

class AggiungiProdottoViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="cliente", password="cliente")
        user = User.objects.create_user(username = "admin", password = "admin")
        user.is_superuser = True
        user.save()
        self.stock = Stock.objects.create(nome = NOME_STOCK)

    def test_aggiungi_prodotto_view_valid(self):

        # Effettuo il login
        data = {
            "username": "admin",
            "password": "admin",
        }
        self.client.post("/login/", data)

        # Cerca e trova la pagina del carrello
        response = self.client.get("/Aggiungi_prodotto/") 
        self.assertEqual(response.status_code, 200)

        # Aggiunta nuovo prodotto
        self.assertEqual(len(Prodotto.objects.filter(nome = "Telecomando televisore")), 0)
        quantita_prodotto = 10
        data = {
            "nome": "Telecomando televisore",
            "tipologia": "Telecomando",
            "descrizione": "Un telecomando universale per il televisore.",
            "prezzo": 59.99,
            "quantita": quantita_prodotto,

            "prodotto_id": "-1"
        }
        response = self.client.post("/Aggiungi_prodotto/", data, follow=True)
        self.assertRedirects(response, "/Home_amministratore/")
        self.assertIsNotNone(Prodotto.objects.get(nome = "Telecomando televisore"))

        # Accede alla pagina di modifica prodotto
        prodotto = Prodotto.objects.get(nome = "Telecomando televisore")
        data = { "prodotto_id": str(prodotto.id) }
        response = self.client.post("/Modifica_prodotto/", data)
        self.assertEqual(response.status_code, 200)

        # Modifica prodotto già esistente
        self.assertEqual(prodotto.quantita, quantita_prodotto)
        nuova_quantita_prodotto = 5
        data = {
            "prodotto_id": str(prodotto.id),
            "nome": prodotto.nome,
            "tipologia": prodotto.tipologia,
            "descrizione": prodotto.descrizione,
            "prezzo": prodotto.prezzo,
            "quantita": nuova_quantita_prodotto
        }
        response = self.client.post("/Modifica_prodotto/", data, follow=True)
        self.assertRedirects(response, "/Home_amministratore/")
        self.assertEqual(Prodotto.objects.get(id = prodotto.id).quantita, nuova_quantita_prodotto)

    def test_aggiungi_prodotto_view_invalid(self):

        # Non è stato effettuato il login
        response = self.client.get("/Aggiungi_prodotto/")
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE)

        # Il login è stato effettuato come cliente
        data = {
            "username": "cliente",
            "password": "cliente",
        }
        self.client.post("/login/", data)
        response = self.client.get("/Aggiungi_prodotto/", follow=True)
        self.assertRedirects(response, "/home/")

class HomeAmministratoreViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="cliente", password="cliente")
        user = User.objects.create_user(username = "admin", password = "admin")
        user.is_superuser = True
        user.save()
        self.stock = Stock.objects.create(nome = NOME_STOCK)

    def test_home_amministratore_view_valid(self):
        data = {
            "username": "admin",
            "password": "admin",
        }
        self.client.post("/login/", data)

        response = self.client.get("/Home_amministratore/") 
        self.assertEqual(response.status_code, 200)

        prodotto = Prodotto.objects.create(
            nome = "Telecomando televisore",
            tipologia = "Telecomando",
            descrizione = "Un telecomando universale per il televisore.",
            prezzo = 59.99,
            quantita = 10,
            stock = self.stock
        )
        data = {
            "nome": prodotto.nome
        }
        response = self.client.post("/Home_amministratore/", data)
        self.assertEqual(response.status_code, 200)

    def test_home_amministratore_view_invalid(self):

        # Non è stato effettuato il login
        response = self.client.get("/Home_amministratore/")
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE)

        # Il login è stato effettuato come cliente
        data = {
            "username": "cliente",
            "password": "cliente",
        }
        self.client.post("/login/", data)
        response = self.client.get("/Home_amministratore/", follow=True)
        self.assertRedirects(response, "/home/")

class ResocontoVenditeViewTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username="cliente", password="cliente")
        user = User.objects.create_user(username = "admin", password = "admin")
        user.is_superuser = True
        user.save()
        self.stock = Stock.objects.create(nome = NOME_STOCK)

    def test_resoconto_vendite_view_valid(self):
        data = {
            "username": "admin",
            "password": "admin",
        }
        self.client.post("/login/", data)

        response = self.client.get("/Resoconto_vendite/") 
        self.assertEqual(response.status_code, 200)

        prodotto = Prodotto.objects.create(
            nome = "Telecomando televisore",
            tipologia = "Telecomando",
            descrizione = "Un telecomando universale per il televisore.",
            prezzo = 59.99,
            quantita = 10,
            stock = self.stock
        )
        data = {
            "nome": prodotto.nome
        }
        response = self.client.post("/Resoconto_vendite/", data)
        self.assertEqual(response.status_code, 200)

    def test_resoconto_vendite_view_invalid(self):

        # Non è stato effettuato il login
        response = self.client.get("/Resoconto_vendite/")
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE)

        # Il login è stato effettuato come cliente
        data = {
            "username": "cliente",
            "password": "cliente",
        }
        self.client.post("/login/", data)
        response = self.client.get("/Resoconto_vendite/", follow=True)
        self.assertRedirects(response, "/home/")
