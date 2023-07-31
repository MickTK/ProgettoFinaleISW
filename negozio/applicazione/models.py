from django.db import models
from django.contrib.auth.models import User

#==============================================================================
# Negozio
#==============================================================================

class Stock(models.Model):
  nome = models.CharField(max_length=100, default="", unique=True)

  # Aggiunge un nuovo prodotto al negozio
  def aggiungi_nuovo_prodotto(self,nome,tipologia,descrizione,prezzo,quantita=1):
    prodotto = Prodotto(
      nome = nome,
      tipologia = tipologia,
      descrizione = descrizione,
      prezzo = prezzo,
      quantita = quantita,
      stock = self
    )
    prodotto.save()
    return prodotto

  # Rimuove completamente un prodotto dal negozio
  def rimuovi_prodotto(self,prodotto):
    if prodotto.stock.id == self.id:
      prodotto.delete()

class Carrello(models.Model):
  user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='carrello')

  # Aggiunge un'unità di prodotto al carrello
  def aggiungi_prodotto(self, prodotto, quantita=1):
    prodotto_carrello = ProdottoCarrello.objects.filter(carrello=self,prodotto=prodotto)
    if quantita < 1:
      quantita = 1
    # Incrementa la quantità
    if prodotto_carrello.count() > 0:
      prodotto_carrello.quantita += quantita
      prodotto_carrello.save()
    # Aggiunge il prodotto al carrello
    else:
      prodotto_carrello = ProdottoCarrello.objects.create(
        quantita=quantita,
        carrello=self,
        prodotto=prodotto
      )
    return prodotto_carrello

  # Rimuove un'unità di prodotto al carrello
  def rimuovi_prodotto(self, prodotto, quantita=1):
    prod = ProdottoCarrello.objects.get(carrello=self,prodotto=prodotto)
    if quantita < 1:
      quantita = 1
    # Decrementa la quantità
    if prod != None:
      prod.quantita -= quantita
      # Se viene rimosso l'ultima unità di prodotto del carrello
      prod.delete() if prod.quantita < 1 else prod.save()

  # Il prezzo totale dei prodotti nel carrello
  def totale(self):
    prodotti = ProdottoCarrello.objects.filter(carrello=self)
    totale = 0
    for prodotto in prodotti:
      totale += prodotto.prodotto.prezzo * prodotto.quantita
    return totale

#================================================
# Prodotto
#================================================

# Prodotto presente nel negozio e disponibile per l'acquisto
class Prodotto(models.Model):
  nome = models.CharField(max_length=100)
  tipologia = models.CharField(max_length=100)
  descrizione = models.CharField(max_length=500)
  prezzo = models.FloatField()
  quantita = models.IntegerField()
  stock = models.ForeignKey(Stock,on_delete=models.CASCADE,related_name='prodotti')

  # Modifica le informazioni del Prodotto
  # @params (string)nome, (string)tipologia, (string)descrizione, (float)prezzo, (integer)quantita
  def modifica(self, **kwargs):
    if "nome" in kwargs:
      self.nome = kwargs["nome"]
    if "tipologia" in kwargs:
      self.tipologia = kwargs["tipologia"]
    if "descrizione" in kwargs:
      self.descrizione = kwargs["descrizione"]
    if "prezzo" in kwargs:
      self.prezzo = kwargs["prezzo"]
    if "quantita" in kwargs:
      self.quantita = kwargs["quantita"]
    self.save()

# Prodotto presente nel Carrello del Cliente (indica in che quantità è presente)
class ProdottoCarrello(models.Model):
  quantita = models.IntegerField()
  carrello = models.ForeignKey(Carrello,on_delete=models.CASCADE,related_name='prodotti')
  prodotto = models.ForeignKey(Prodotto,on_delete=models.CASCADE)

  # Modifica la quantità di un Prodotto all'interno del Carrello
  # @param quantita: un valore intero che verrà sommato alla quantita attuale di prodotto
  def modifica_quantita(self, quantita):
    self.quantita += quantita
    self.delete() if self.quantita < 1 else self.save()

  # Rimuove il ProdottoCarrello corrente e ne crea una copia come ProdottoVenduto
  def acquista(self):
    ProdottoVenduto.objects.create(
      nome = self.prodotto.nome,
      tipologia = self.prodotto.tipologia,
      descrizione = self.prodotto.descrizione,
      prezzo = self.prodotto.prezzo,
      quantita = self.quantita,
      stock = self.prodotto.stock
    )
    self.prodotto.quantita -= self.quantita
    if self.prodotto.quantita < 1:
      self.prodotto.stock.rimuovi_prodotto(self.prodotto)
    self.delete()

# Informazioni relative ad un prodotto venduto (serve per il resoconto)
class ProdottoVenduto(models.Model):
  nome = models.CharField(max_length=100)
  tipologia = models.CharField(max_length=100)
  descrizione = models.CharField(max_length=500)
  prezzo = models.FloatField()
  quantita = models.IntegerField()
  stock = models.ForeignKey(Stock,on_delete=models.CASCADE,related_name='prodotti_venduti')

  # Calcola il ricavo dato dalla vendita dei prodotti dello stesso tipo
  def ricavo(self):
    return self.quantita * self.prezzo
