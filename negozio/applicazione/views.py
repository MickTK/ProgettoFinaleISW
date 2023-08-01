from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from applicazione.forms import *
from applicazione.models import *

def login_view(request):
  form = LoginForm()
  template = loader.get_template("login.html")
  context = {"form" : form}

  if request.method =='POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(request, username=username, password=password)

      if user is None : 
        return HttpResponse(template.render(context, request))
      else:
        login(request, user)
        return home_view(request)
  return HttpResponse(template.render(context, request))


#Devo fare una funzione per ogni pagina request è il PAYLOAD, context passo i valori alla pagina


def registrazione_view(request):
  template = loader.get_template("utente/registrazione.html")
  context = {}
  return HttpResponse(template.render(context, request))

#Bisogna popolare la lista degli oggetti, stock prendo negozio nel contesto cerco i prodotti che si trovano lì
def home_view(request):
  template = loader.get_template("utente/home.html")
  stock = Stock.objects.get(nome="Negozio")
  context = {"prodotti" : Prodotto.objects.filter(stock = stock).all()}
  return HttpResponse(template.render(context, request))

#get restituisce un solo oggetto, filter tutti quelli che soddisfano la condizione

#def checkout_view(request):
 # template = loader.get_template("utente/checkout.html")
 # context = {}
 # return HttpResponse(template.render(context, request))

#Vista del checkout NON TESTATA, DA PROVARE, impostata la logica
def checkout_view(request):
    template = loader.get_template("utente/checkout.html")

    # Utente Autenticato
    if request.user.is_authenticated:
        carrello = request.user.carrello
        prodottiCarrello = carrello.prodotti.all()

        # Calcolo del totale del carrello
        total_price = sum(prodotto.prezzo for prodotto in prodottiCarrello)

        context = {
            "prodottiCarrello": prodottiCarrello,
            "carrello": carrello,
            "total_price": total_price,
        }
    else:
        # Se non è autenticato torna al login
        return HttpResponseRedirect("/login/")

    return HttpResponse(template.render(context, request))


#Come visualizzo il carrello dell'utente? "prodottiCarrello" Request.user
def carrello_view(request):
  login(request, User.objects.get(username = "cliente"))
  template = loader.get_template("utente/carrello.html")
  carrello = request.user.carrello
  context = {"prodottiCarrello" : request.user.carrello.prodotti.all(), "carrello" : carrello}
  return HttpResponse(template.render(context, request))

def aggiungi_prodotto_view(request):
  template = loader.get_template("amministratore/Aggiungi_prodotto.html")
  context = {}
  return HttpResponse(template.render(context, request))

#"prodottiNegozio"
def home_amministratore_view(request):
  template = loader.get_template("amministratore/Home_amministratore.html")
  context = {}
  return HttpResponse(template.render(context, request))

#"resocontoVendite"
def resoconto_vendite_view(request):
  template = loader.get_template("amministratore/Resoconto_vendite.html")
  context = {}
  return HttpResponse(template.render(context, request))
