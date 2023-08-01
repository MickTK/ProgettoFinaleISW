from django.test import TestCase
from applicazione.forms import *

class LoginFormTestCase(TestCase):

  def test_login_form_valid(self):
    form = LoginForm(data={
      "username": "marietto",
      "password": "12345678"
    })
    self.assertTrue(form.is_valid())

  def test_login_form_invalid(self):
    form = LoginForm(data={
      "username": "mario",
      "password": "12345"
    })
    self.assertFalse(form.is_valid())

class RegistrazioneFormTestCase(TestCase):

  def test_registrazione_form_valid(self):
    form = RegistrazioneForm(data={
      "username": "marietto",
      "password": "12345678"
    })
    self.assertTrue(form.is_valid())

  def test_registrazione_form_invalid(self):
    form = RegistrazioneForm(data={
      "username": "mario",
      "password": "12345"
    })
    self.assertFalse(form.is_valid())

class CheckoutFormTestCase(TestCase):

  def test_checkout_form_valid(self):
    form = CheckoutForm(data={
      "indirizzo": "Via delle Rose, 14",
      "codice_paypal": "2364985234762348"
    })
    self.assertTrue(form.is_valid())

  def test_checkout_form_invalid(self):
    form = CheckoutForm(data={
      "indirizzo": "Via delle Rose, 14",
      "codice_paypal": "53297464"
    })
    self.assertFalse(form.is_valid())

class ModificaProdottoFormTestCase(TestCase):

  def test_modifica_prodotto_form_valid(self):
    form = ModificaProdottoForm(data={
      "nome": "LG Plasma A02",
      "tipologia": "Televisore",
      "descrizione": "Un bellissimo televisore.",
      "prezzo": "1099.99",
      "quantita": "200"
    })
    self.assertTrue(form.is_valid())

  def test_modifica_prodotto_form_invalid(self):
    form = ModificaProdottoForm(data={
      "nome": "LG Plasma A02",
      "tipologia": "Televisore",
      "descrizione": "Un bellissimo televisore.",
      "prezzo": "-10",
      "quantita": "200.1"
    })
    self.assertFalse(form.is_valid())

class AggiuntaNuovoProdottoFormTestCase(TestCase):

  def test_aggiunta_nuovo_prodotto_form_valid(self):
    form = AggiuntaNuovoProdottoForm(data={
      "nome": "LG Plasma A02",
      "tipologia": "Televisore",
      "descrizione": "Un bellissimo televisore.",
      "prezzo": "1099.99",
      "quantita": "200"
    })
    self.assertTrue(form.is_valid())

  def test_aggiunta_nuovo_prodotto_form_invalid(self):
    form = AggiuntaNuovoProdottoForm(data={
      "nome": "LG Plasma A02",
      "tipologia": "Televisore",
      "descrizione": "Un bellissimo televisore.",
      "prezzo": "-10",
      "quantita": "200.1"
    })
    self.assertFalse(form.is_valid())
