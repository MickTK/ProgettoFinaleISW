from django.test import TestCase 
from django.contrib.auth.models import User 
from django.urls import reverse 
from applicazione.views import * 
from applicazione.models import * 
 
class LoginViewTestCase(TestCase): 
    def setUp(self): 
        User.objects.create_user(username = "provacl", password = "passwcli") 
        Stock.objects.create(nome = "Negozio") 
 
    def test_login_view(self): 
 
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
 
        # Non esegue l'accesso perché le credenziali sono errate 
        data = { 
            "username": "pippo", 
            "password": "baudo", 
        } 
        response = self.client.post("/login/", data) 
        self.assertEqual(response.status_code, 200)