from django.test import TestCase
from applicazione.models import *
from datetime import datetime, timezone

class MasterTestCase(TestCase):
  def setUp(self):
    self.stock = Stock.objects.create(nome = "Negozio")
    self.stock.aggiungi_nuovo_prodotto(
      "Motorino",
      "Veicolo",
      "Motorino elettrico ecologico.",
      499.99,
      25
    )
    self.cliente = User.objects.create(
      username = "user",
      password = "pass",
      last_login = datetime.now(timezone.utc)
    )
    self.carrello = Carrello.objects.create(user = self.cliente)

#==============================================================================
# Negozio
#==============================================================================

class StockTestCase(MasterTestCase):

  def setUp(self):
    super().setUp()

  def test_aggiungi_nuovo_prodotto(self):
    count = self.stock.prodotti.count()
    self.stock.aggiungi_nuovo_prodotto(
      "Lavatrice",
      "Elettrodomestici",
      "Una bellissima lavatrice",
      200,
      100
    )
    self.assertEqual(self.stock.prodotti.count(), count + 1)
    self.assertEqual(self.stock.prodotti.get(id = count + 1).nome, "Lavatrice")

  def test_rimuovi_prodotto(self):
    count = self.stock.prodotti.count()
    self.assertGreater(count, 0)
    self.stock.rimuovi_prodotto(self.stock.prodotti.get(nome = "Motorino"))
    with self.assertRaises(Prodotto.DoesNotExist):
      self.stock.prodotti.get(nome = "Motorino")
    self.assertEqual(self.stock.prodotti.count(), count - 1)

class CarrelloTestCase(MasterTestCase):

  def setUp(self):
    super().setUp()

  def test_aggiungi_prodotto(self):
    count = self.carrello.prodotti.count()
    prodotto = Stock.objects.get(nome = "Negozio").prodotti.get(nome = "Motorino")
    self.carrello.aggiungi_prodotto(prodotto)
    self.assertEqual(self.carrello.prodotti.count(), count + 1)
    self.assertIsNotNone(self.carrello.prodotti.get(carrello = self.carrello, prodotto = prodotto))

  def test_rimuovi_prodotto(self):
    prodotto = Stock.objects.get(nome = "Negozio").prodotti.get(nome = "Motorino")
    quantita = 10
    self.carrello.aggiungi_prodotto(prodotto, quantita)
    self.carrello.rimuovi_prodotto(prodotto)
    self.assertEqual(self.carrello.prodotti.get(prodotto = prodotto).quantita, quantita - 1)

  def test_totale(self):
    prodotto = Stock.objects.get(nome = "Negozio").prodotti.get(nome = "Motorino")
    quantita = 2
    self.carrello.aggiungi_prodotto(prodotto, quantita)
    totale_atteso = quantita * prodotto.prezzo
    prodotto = self.stock.aggiungi_nuovo_prodotto(
      "Lavatrice",
      "Elettrodomestici",
      "Una bellissima lavatrice",
      200,
      100
    )
    quantita = 5
    self.carrello.aggiungi_prodotto(prodotto, quantita)
    totale_atteso += quantita * prodotto.prezzo
    self.assertEqual(self.carrello.totale(), totale_atteso)

#================================================
# Prodotto
#================================================

class ProdottoTestCase(MasterTestCase):

  def setUp(self):
    super().setUp()

  def test_modifica(self):
    prodotto = self.stock.prodotti.get(nome = "Motorino")
    nome = "Monopattino elettrico"
    descrizione = "Un monopattino ecologico con impatto zero sull'ambiente."
    prodotto.modifica(descrizione = descrizione, nome = nome)
    self.assertEqual(prodotto.nome, nome)
    self.assertEqual(prodotto.descrizione, descrizione)

class ProdottoCarrelloTestCase(MasterTestCase):

  def setUp(self):
    super().setUp()

  def test_modifica_quantita(self):
    prodotto = self.stock.prodotti.get(nome = "Motorino")
    self.carrello.aggiungi_prodotto(prodotto, 5)
    count = self.carrello.prodotti.count()
    prodotto_carrello = self.carrello.prodotti.get(prodotto = prodotto)
    prodotto_carrello.modifica_quantita(+3)
    self.assertEqual(prodotto_carrello.quantita, 8)
    prodotto_carrello.modifica_quantita(-5)
    self.assertEqual(prodotto_carrello.quantita, 3)
    prodotto_carrello.modifica_quantita(-100)
    self.assertEqual(self.carrello.prodotti.count(), count - 1)

  def test_acquista(self):
    prodotto = self.stock.prodotti.get(nome = "Motorino")
    quantita_magazzino = prodotto.quantita
    quantita_carrello = quantita_magazzino - 5 # 20
    prodotto_carrello = self.carrello.aggiungi_prodotto(prodotto, quantita_carrello)
    prodotto_carrello.acquista()
    prodotto_venduto = ProdottoVenduto.objects.get(stock = self.stock, nome = "Motorino")
    self.assertEqual(prodotto_venduto.quantita, quantita_carrello)
    self.assertEqual(prodotto.quantita, quantita_magazzino - quantita_carrello)

class ProdottoVendutoTestCase(MasterTestCase):
  
  def setUp(self):
    super().setUp()
    self.prodotto = self.stock.prodotti.get(nome = "Motorino")
    self.carrello.aggiungi_prodotto(self.prodotto, 2).acquista()
    self.prodotto_venduto = self.stock.prodotti_venduti.get(nome = "Motorino")

  def test_ricavo(self):
    ricavo_atteso = self.prodotto.prezzo * 2
    self.assertEqual(self.prodotto_venduto.ricavo(), ricavo_atteso)
