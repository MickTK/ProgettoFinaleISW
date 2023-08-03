from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.urls import reverse
from applicazione.views import *
from applicazione.models import Stock 
from unittest.mock import patch # mock permette di non basarsi sul database, ma ne simula il comportamento

class LoginViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory() # creare oggetti HttpRequest simulati,
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    # Sostituire temporaneamente un oggetto o un metodo con un oggetto mock.
    @patch('applicazione.views.Stock.objects.get')
    def test_login_successful(self, mock_get_stock):
        # Simula il comportamento di Stock
        mock_get_stock.return_value = Stock(nome='NomeStock')

        # Simula il login dell'utente
        self.client.force_login(self.user)

        # Crea una richiesta POST valida con credenziali corrette
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post(reverse('login_view'), data)

        # Verifica che la vista reindirizzi l'utente al percorso corretto
        if self.user.is_superuser:
            self.assertRedirects(response, '/Home_amministratore/')
        else:
            self.assertRedirects(response, '/home/')
