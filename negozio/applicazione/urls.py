from django.urls import path

from . import views

urlpatterns = [
  path("", views.login_view, name="login_view"),
  path("login/", views.login_view, name="login_view"),
  path("login_result/", views.login_form_result, name="login_form_result"),
  path("registrazione/", views.registrazione_view, name="registrazione_view"),
  path("home/", views.home_view, name="home_view"),
  path("checkout/", views.checkout_view, name="checkout_view"),
  path("carrello/", views.carrello_view, name="carrello_view"),
  path("aggiungi_prodotto/", views.aggiungi_prodotto_view, name="aggiungi_prodotto_view"),
  path("home_amministratore/", views.home_amministratore_view, name="home_amministratore_view"),
  path("resoconto_vendite/", views.resoconto_vendite_view, name="resoconto_vendite_view"),
  
]
