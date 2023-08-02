from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from applicazione.forms import *
from applicazione.models import *

NOME_STOCK = "Negozio"

def login_view(request):
  # Inizializzazione
  request.session["user_id"] = None
  template = loader.get_template("login.html")
  context = {"form" : LoginForm()}

  # Gestione richieste
  if request.method =="POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      user = authenticate(request,
        username = form.cleaned_data["username"],
        password = form.cleaned_data["password"]
      )
      if user is not None : 
        login(request, user)
        request.session["user_id"] = request.user.id
        return redirect("../home/")

  return HttpResponse(template.render(context, request))

def home_view(request):
  # Inizializzazione
  user_id = request.session.get("user_id")
  if user_id:
    user = User.objects.get(id=user_id)
  else:
   return redirect("../login/")
  
  template = loader.get_template("utente/home.html")
  stock = Stock.objects.get(nome = NOME_STOCK)
  context = {"prodotti" : Prodotto.objects.filter(stock = stock).all()}
  return HttpResponse(template.render(context, request))


















def registrazione_view(request):
  template = loader.get_template("utente/registrazione.html")
  context = {}
  return HttpResponse(template.render(context, request))



#get restituisce un solo oggetto, filter tutti quelli che soddisfano la condizione

#def checkout_view(request):
 # template = loader.get_template("utente/checkout.html")
 # context = {}
 # return HttpResponse(template.render(context, request))

#Vista del checkout impostata la logica
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


#Vista del carrello impostata la logica
def carrello_view(request):
    template = loader.get_template("utente/carrello.html")

    # Utente Autenticato e con carrello
    if request.user.is_authenticated:
        carrello = request.user.carrello
        prodottiCarrello = carrello.prodotti.all()

        context = {
            "prodottiCarrello": prodottiCarrello,
            "carrello": carrello,
        }
    else:
        # Se non è autenticato torna al login
        return HttpResponseRedirect("/login/")

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
