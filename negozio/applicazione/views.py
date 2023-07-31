from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from applicazione.models import *

def login_view(request):
  login(request, User.objects.get(username = "cliente"))
  template = loader.get_template("login.html")
  context = {}
  return HttpResponse(template.render(context, request))

#Devo fare una funzione per ogni pagina request è il PAYLOAD, context passo i valori alla pagina

#Form con Python(?)
def registrazione(request):
  template = loader.get_template("utente/registrazione.html")
  context = {}
  return HttpResponse(template.render(context, request))

#Bisogna popolare la lista degli oggetti, stock prendo negozio nel contesto cerco i prodotti che si trovano lì
def home(request):
  template = loader.get_template("utente/home.html")
  stock = Stock.objects.get(nome="Negozio")
  context = {"prodotti" : Prodotto.objects.filter(stock = stock).all()}
  return HttpResponse(template.render(context, request))

#get restituisce un solo oggetto, filter tutti quelli che soddisfano la condizione

def checkout(request):
  template = loader.get_template("utente/checkout.html")
  context = {}
  return HttpResponse(template.render(context, request))

#Come visualizzo il carrello dell'utente? "prodottiCarrello" Request.user
def carrello_view(request):
  login(request, User.objects.get(username = "cliente"))
  template = loader.get_template("utente/carrello.html")
  carrello = request.user.carrello
  context = {"prodottiCarrello" : request.user.carrello.prodotti.all(), "carrello" : carrello}
  return HttpResponse(template.render(context, request))

def aggiungi_prodotto(request):
  template = loader.get_template("amministratore/Aggiungi_prodotto.html")
  context = {}
  return HttpResponse(template.render(context, request))

#"prodottiNegozio"
def home_amministratore(request):
  template = loader.get_template("amministratore/Home_amministratore.html")
  context = {}
  return HttpResponse(template.render(context, request))

#"resocontoVendite"
def resoconto_vendite(request):
  template = loader.get_template("amministratore/Resoconto_vendite.html")
  context = {}
  return HttpResponse(template.render(context, request))
