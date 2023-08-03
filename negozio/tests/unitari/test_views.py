from django.test import TestCase 
from django.contrib.auth.models import User 
from django.urls import reverse 
from applicazione.views import * 
from applicazione.models import * 
from applicazione.forms import *
 
class LoginViewTestCase(TestCase): 
    def setUp(self): 
        User.objects.create_user(username = "provacl", password = "passwcli") 
        Stock.objects.create(nome = "Negozio") 
 
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

    def test_login_view_valid(self): 
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
        Stock.objects.create(nome = "Negozio") 

    def test_registrazione_view_valid(self):

        # Cerca e trova la pagina di registrazione
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200) 

        # Esegue l'accesso tramite le credenziali di un cliente 
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        response = self.client.post("/login/", data) 
        self.assertRedirects(response, "/home/")

    def test_registrazione_view_invalid(self):
        
        # Cerca e trova la pagina di registrazione
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200) 

        # Non esegue l'accesso perché le credenziali sono errate 
        data = { 
            "username": "pippo", 
            "password": "baudo", 
        }
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, stesso username ma password diversa
        data = { 
            "username": "testuser", 
            "password": "altra_password", 
        }
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono vuote 
        data = {}
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, manca password
        data = { 
            "username": "testuser", 
            "password": "", 
        }
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200)

        # Non esegue l'accesso perché le credenziali sono errate, manca username
        data = { 
            "username": "", 
            "password": "testpassword", 
        }
        response = self.client.get("/registrazione/") 
        self.assertEqual(response.status_code, 200)
        