from django.test import TestCase 
from django.contrib.auth.models import User 
from django.urls import reverse 
from applicazione.views import * 
from applicazione.models import * 
from applicazione.forms import *

REDIRECT_STATUS_CODE = 302
 
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


class AggiungiProdottoViewTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username = "admin", password = "testpassword")
        user.is_superuser = True
        user.save()
        self.stock = Stock.objects.create(nome = NOME_STOCK)
        

    def test_aggiungi_prodotto_view_valid(self):

        # Effettuo il login
        data = {
            "username": "admin",
            "password": "testpassword",
        }
        self.client.post("/login/", data)

        # Cerca e trova la pagina del carrello
        response = self.client.get("/Aggiungi_prodotto/") 
        self.assertEqual(response.status_code, 200)

    
    def test_aggiungi_prodotto_view_invalid(self):

        # Cerca la pagina del checkout
        response = self.client.get("/Aggiungi_prodotto/") 
        # Non essendo autenticato torno al login
        self.assertEqual(response.status_code, REDIRECT_STATUS_CODE) #loginrequired 

                   