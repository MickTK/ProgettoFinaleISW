from django.urls import path

from . import views

urlpatterns = [
  path("", views.login, name="login"),
  path("login/", views.login, name="login"),
  path("registrazione/", views.registrazione, name="registrazione"),
  path("home/", views.home, name="home"),
  path("checkout/", views.checkout, name="checkout"),
  path("carrello/", views.carrello, name="carrello"),
  path("aggiungi_prodotto/", views.aggiungi_prodotto, name="aggiungi_prodotto"),
  path("home_amministratore/", views.home_amministratore, name="home_amministrazione"),
  path("resoconto_vendite/", views.resoconto_vendite, name="resoconto_vendite"),
  
]
