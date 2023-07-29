from django.test import TestCase
from applicazione.models import *

class StockTestCase(TestCase):
  def setUp(self):
    self.stock = Stock.objects.create(nome = "negozio")
  def test_aggiungi_nuovo_prodotto(self):
    self.stock.aggiungi_nuovo_prodotto(
      "Lavatrice",
      "Elettrodomestici",
      "Una bellissima lavatrice",
      200,
      100
    )
    prodotto = Prodotto.objects.get(nome = "Lavatrice", prezzo = 200)
    self.assertEqual(self.stock.id,prodotto.stock.id)
  def test_rimuovi_prodotto(self):
    self.stock.aggiungi_nuovo_prodotto(
      "Lavatrice",
      "Elettrodomestici",
      "Una bellissima lavatrice",
      200,
      100
    )
    prodotto = Prodotto.objects.get(nome = "Lavatrice", prezzo = 200)
    #self.stock.rimuovi_prodotto(prodotto)
    prodotto = Prodotto.objects.get(stock = self.stock)
    #self.assertEqual(prodotto, None)

class ProdottoTestCase(TestCase):
  def setUp(self):
    Stock.objects.create(nome = "negozio")
    self.prodotto = Prodotto.objects.create(
      nome = "Smart TV",
      tipologia = "Televisore",
      descrizione = "Televisore con riconoscimento vocale.",
      prezzo = 1499.99,
      quantita = 10,
      stock = Stock.objects.get(nome = "negozio")
    )
  def test_modifica(self):
    nuovo_nome = "Smart TV+"
    nuovo_prezzo = 1749.99
    self.prodotto.modifica(prezzo = nuovo_prezzo, nome = nuovo_nome)
    self.assertEqual(self.prodotto.nome, nuovo_nome)
    self.assertEqual(self.prodotto.prezzo, nuovo_prezzo)
