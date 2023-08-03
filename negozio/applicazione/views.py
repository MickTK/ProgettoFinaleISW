from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from applicazione.forms import *
from applicazione.models import *
from django.contrib.auth.decorators import login_required

NOME_STOCK = "Negozio"

def get_user(request):
  user_id = request.session.get("user_id")
  if user_id:
    return User.objects.get(id = user_id)
  else:
    return None

def set_user(request, user):
  login(request, user)
  request.session["user_id"] = request.user.id

#================================================
# Condivise
#================================================

def login_view(request):
  # Inizializzazione
  logout(request)
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
        set_user(request, user)
        if user.is_superuser:
          return redirect("../Home_amministratore/")
        else:
          return redirect("../home/")

  return HttpResponse(template.render(context, request))

#================================================
# Utente
#================================================

@login_required
def home_view(request):
  # Inizializzazione
  template = loader.get_template("utente/home.html")
  stock = Stock.objects.get(nome = NOME_STOCK)
  context = {
    "prodotti" : Prodotto.objects.filter(stock = stock).all(),
    "form": FiltroHomeUtenteForm()
  }
  
  # Gestione richieste
  if request.method =="POST":
    form = FiltroHomeUtenteForm(request.POST)
    if form.is_valid():
      nome = form.cleaned_data["nome"]
      tipologia = form.cleaned_data["tipologia"]
      minPrezzo = form.cleaned_data["minPrezzo"]
      maxPrezzo = form.cleaned_data["maxPrezzo"]

      nome_check = tipologia_check = prezzo_check = None

      prodotti = context["prodotti"]
      context["prodotti"] = list()
      for prodotto in prodotti:
        if nome is not None:
          nome_check = prodotto.nome.lower().find(nome.lower()) > -1
        if tipologia is not None:
          tipologia_check = prodotto.tipologia.lower().find(tipologia.lower()) > -1
        if minPrezzo is not None:
          prezzo_check = minPrezzo < prodotto.prezzo
        if maxPrezzo is not None:
          prezzo_check = prodotto.prezzo < maxPrezzo
        if minPrezzo is not None and maxPrezzo is not None:
          prezzo_check = minPrezzo < prodotto.prezzo and prodotto.prezzo < maxPrezzo
        if (nome_check or nome_check is None) and (tipologia_check or tipologia_check is None) and (prezzo_check or prezzo_check is None):
          context["prodotti"].append(prodotto)
      
      valori_iniziali_form = {
        "nome": nome,
        "tipologia": tipologia,
        "minPrezzo": minPrezzo,
        "maxPrezzo": maxPrezzo
      }
      context["form"] = FiltroHomeUtenteForm(initial = valori_iniziali_form)



  return HttpResponse(template.render(context, request))

def registrazione_view(request):
  # Inizializzazione
  template = loader.get_template("utente/registrazione.html")
  context = {"form": RegistrazioneForm()}

  # Gestione richieste
  if request.method =="POST":
    form = RegistrazioneForm(request.POST)
    if form.is_valid():
      username = form.cleaned_data["username"]
      password = form.cleaned_data["password"]
      user = User.objects.filter(username = username)
      if user.count() == 0:
        User.objects.create_user(username = username, password = password)
        user = authenticate(request,
          username = form.cleaned_data["username"],
          password = form.cleaned_data["password"]
        )
        set_user(request, user)
        return redirect("../home/")
      else:
        context["errore"] = "Nome utente già registrato."

  return HttpResponse(template.render(context, request))

@login_required
def carrello_view(request):
  template = loader.get_template("utente/carrello.html")
  user = get_user(request)
  context = {
    "prodottiCarrello": user.carrello.prodotti.all(),
    "carrello": user.carrello,
  }
  return HttpResponse(template.render(context, request))

@login_required
def checkout_view(request):
  template = loader.get_template("utente/checkout.html")
  context = {
    "form": CheckoutForm()
  }
  user = get_user(request)

  if request.method == "POST":
    form = CheckoutForm(request.POST)
    if form.is_valid():
      for prodotto in user.carrello.prodotti.all():
        prodotto.acquista()
      return redirect("../home")

  return HttpResponse(template.render(context, request))

#================================================
# Amministratore
#================================================

@login_required
def aggiungi_prodotto_view(request):
  template = loader.get_template("amministratore/Aggiungi_prodotto.html")
  context = {"form": AggiuntaNuovoProdottoForm()}

  if request.method =="POST":
    form = AggiuntaNuovoProdottoForm(request.POST)
    if form.is_valid():
      nome = form.cleaned_data["nome"]
      tipologia = form.cleaned_data["tipologia"]
      descrizione = form.cleaned_data["descrizione"]
      prezzo = form.cleaned_data["prezzo"]
      quantita = form.cleaned_data["quantita"]

      Prodotto.objects.create(
        nome = nome,
        tipologia = tipologia,
        descrizione = descrizione,
        prezzo = prezzo,
        quantita = quantita,
        stock = Stock.objects.get(nome = NOME_STOCK)
      )
      return redirect("../Home_amministratore")

  return HttpResponse(template.render(context, request))








######################################################
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
