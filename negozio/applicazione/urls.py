from django.urls import path

from . import views

urlpatterns = [
  path("", views.login_view, name="login_view"),
  path("login/", views.login_view, name="login_view"),
  path("registrazione/", views.registrazione, name="registrazione"),
  path("home/", views.home, name="home"),
  path("checkout/", views.checkout, name="checkout"),
  path("carrello/", views.carrello_view, name="carrello_view"),
  path("aggiungi_prodotto/", views.aggiungi_prodotto, name="aggiungi_prodotto"),
  path("home_amministratore/", views.home_amministratore, name="home_amministrazione"),
  path("resoconto_vendite/", views.resoconto_vendite, name="resoconto_vendite"),
  
]
