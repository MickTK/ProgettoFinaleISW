from django.db import models

class Autenticatore:
  def registra_cliente(self,username,password):
    if login_cliente(username,password) == None and login_amministratore(username,password) == None:
      Cliente(username=username,password = password).save()
      return True
    else:
      return False
    
  def login_cliente(self,username,password):
    return Cliente.objects.get(username=username,password=password)
  
  def login_amministratore(self,username,password):
    return Amministratore.objects.get(username=username,password=password)
  
  def logout(self):
    pass

#==============================================================================
# Negozio
#==============================================================================

class Stock(models.Model):
  nome = models.CharField(max_length=100, default="")

  # Aggiunge un nuovo prodotto al negozio
  def aggiungi_nuovo_prodotto(self,nome,tipologia,descrizione,prezzo,quantita=1):
    Prodotto(
      nome = nome,
      tipologia = tipologia,
      descrizione = descrizione,
      prezzo = prezzo,
      quantita = quantita,
      stock = self
    ).save()

  # Rimuove completamente un prodotto dal negozio
  def rimuovi_prodotto(self,prodotto):
    prod = Prodotto.objects.get(
      nome = prodotto.nome,
      tipologia = prodotto.tipologia,
      descrizione = prodotto.descrizione,
      prezzo = prodotto.prezzo,
      quantita = prodotto.quantita,
      stock = self
    )
    if prod == prodotto:
      prodotto.delete()

class Carrello(models.Model):

  # Il prezzo totale dei prodotti nel carrello
  def totale(self):
    prodotti = ProdottoCarrello.objects.get(carrello=self)
    totale = 0
    for prodotto in prodotti:
      totale += prodotto.prodotto.prezzo * prodotto.quantita
    return totale
  
  # Aggiunge un'unità di prodotto al carrello
  def aggiungi_prodotto(self,prodotto):
    prod = ProdottoCarrello.objects.get(carrello=self,prodotto=prodotto)
    # Incrementa la quantità
    if prod != None:
      prod.quantita += 1
      prod.save()
    # Aggiunge il prodotto al carrello
    else:
      ProdottoCarrello(
        quantita=1,
        carrello=self,
        prodotto=prodotto
      ).save()

  # Rimuove un'unità di prodotto al carrello
  def rimuovi_prodotto(self,prodotto):
    prod = ProdottoCarrello.objects.get(carrello=self,prodotto=prodotto)
    # Decrementa la quantità
    if prod != None:
      prod.quantita -= 1
      # Se viene rimosso l'ultima unità di prodotto del carrello
      prod.delete() if prod.quantita < 1 else prod.save()

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
  stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

  # Modifica le informazioni del Prodotto
  # @params (string)nome, (string)tipologia, (string)descrizione, (float)prezzo, (integer)quantita
  def modifica(self, **kwargs):
    if kwargs["nome"] != None:
      self.nome = kwargs["nome"]
    if kwargs["tipologia"] != None:
      self.tipologia = kwargs["tipologia"]
    if kwargs["descrizione"] != None:
      self.descrizione = kwargs["descrizione"]
    if kwargs["prezzo"] != None:
      self.prezzo = kwargs["prezzo"]
    if kwargs["quantita"] != None:
      self.quantita = kwargs["quantita"]
    self.save()

  def __eq__(self, other):
    return (self.nome, self.tipologia, self.descrizione, self.prezzo, self.quantita, self.stock) == (other.nome, other.tipologia, other.descrizione, other.prezzo, other.quantita, other.stock)

# Prodotto presente nel Carrello del Cliente (indica in che quantità è presente)
class ProdottoCarrello(models.Model):
  quantita = models.IntegerField()
  carrello = models.ForeignKey(Carrello,on_delete=models.CASCADE)
  prodotto = models.ForeignKey(Prodotto,on_delete=models.CASCADE)

  # Modifica la quantità di un Prodotto all'interno del Carrello
  def modifica_quantita(self, quantita):
    self.quantita = quantita
    self.delete() if quantita < 1 else self.save()

  # Rimuove il ProdottoCarrello corrente e ne crea una copia come ProdottoVenduto
  def acquista(self):
    ProdottoVenduto(
      nome = self.prodotto.nome,
      tipologia = self.prodotto.tipologia,
      descrizione = self.prodotto.descrizione,
      prezzo = self.prodotto.prezzo,
      quantita = self.quantita
    ).save()
    Stock.objects.get(pk=1).rimuovi_prodotto(self.prodotto, self.quantita)
    self.delete()

# Informazioni relative ad un prodotto venduto (serve per il resoconto)
class ProdottoVenduto(Prodotto):
  
  # Calcola il ricavo dato dalla vendita dei prodotti dello stesso tipo
  def ricavo(self):
    return self.quantita * self.prezzo

#==============================================================================
# Attori
#==============================================================================

# Utente (generico)
class Utente(models.Model):
  username = models.CharField(max_length=100, primary_key=True)
  password = models.CharField(max_length=100)

  def tipo(self):
    return self.__class__.__name__

# Cliente (utilizza il Carrello e acquista i prodotti)
class Cliente(Utente):
  carrello = models.ForeignKey(Carrello, null=True, on_delete=models.SET_NULL)

  def __str__(self):
    return f"Cliente: {self.username}"

# Amministratore (gestisce il negozio)
class Amministratore(Utente):

  def __str__(self):
    return f"Amministratore: {self.username}"
