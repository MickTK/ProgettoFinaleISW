from django import forms

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", min_length=8, max_length=100)
  password = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)

class RegistrazioneForm(forms.Form):
  username = forms.CharField(label="Username", min_length=8, max_length=100)
  password = forms.CharField(label="Password", min_length=8, widget=forms.PasswordInput)

class CheckoutForm(forms.Form):
  indirizzo = forms.CharField(label="Indirizzo", min_length=5, max_length=100)
  codice_paypal = forms.CharField(label="Codice", min_length=16, max_length=16)

class ModificaProdottoForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100)
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100)
  descrizione = forms.CharField(label="Descrizione", min_length=1, max_length=500)
  prezzo = forms.FloatField(label="Prezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01}))
  quantita = forms.IntegerField(label="Quantita", min_value=1, widget=forms.NumberInput(attrs={'min': 1}))

class AggiuntaNuovoProdottoForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100)
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100)
  descrizione = forms.CharField(label="Descrizione", min_length=1, max_length=500)
  prezzo = forms.FloatField(label="Prezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01}))
  quantita = forms.IntegerField(label="Quantita", min_value=1, widget=forms.NumberInput(attrs={'min': 1}))
