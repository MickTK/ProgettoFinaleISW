from django.urls import path

from . import views

urlpatterns = [
    
  # Cliente
  path("", views.login_view, name="login_view"),
  path("login/", views.login_view, name="login_view"),
  path("registrazione/", views.registrazione_view, name="registrazione_view"),
  path("home/", views.home_view, name="home_view"),
  path("checkout/", views.checkout_view, name="checkout_view"),
  path("carrello/", views.carrello_view, name="carrello_view"),
  
  # Amministratore
  path("Aggiungi_prodotto/", views.aggiungi_prodotto_view, name="aggiungi_prodotto_view"),
  path("Home_amministratore/", views.home_amministratore_view, name="home_amministratore_view"),
  path("Resoconto_vendite/", views.resoconto_vendite_view, name="resoconto_vendite_view"),
]
