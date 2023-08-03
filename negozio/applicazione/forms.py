from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", min_length=5, max_length=100)
  password = forms.CharField(label="Password", min_length=5, widget=forms.PasswordInput)

class RegistrazioneForm(forms.Form):
  username = forms.CharField(label="Username", min_length=5, max_length=100)
  password = forms.CharField(label="Password", min_length=5, widget=forms.PasswordInput)

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





# filtro per cercare all'interno della home utente
class FiltroHomeUtenteForm(forms.Form):
  nome = forms.CharField(label="Nome", max_length=100, required=False)
  tipologia = forms.CharField(label="Tipologia", max_length=100, required=False)
  minPrezzo = forms.FloatField(label="minPrezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01}), required=False)
  maxPrezzo = forms.FloatField(label="maxPrezzo", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000}), required=False)
  
  def clean(self):
        cleaned_data = super().clean()
        min_prezzo = cleaned_data.get("minPrezzo")
        max_prezzo = cleaned_data.get("maxPrezzo")

        if min_prezzo is not None and max_prezzo is not None:
            if min_prezzo >= max_prezzo:
                raise forms.ValidationError("Il prezzo minimo deve essere strettamente minore del prezzo massimo.")
        
        return cleaned_data
  
# filtro per cercare all'interno della home amministratore
class FiltroHomeAmministratoreForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100, required=False)
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100, required=False)
  minPrezzo = forms.FloatField(label="minPrezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01}), required=False)
  maxPrezzo = forms.FloatField(label="maxPrezzo", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000}), required=False)
  minNumPezziDisponibili = forms.IntegerField(label="minNumPezziDisponibili", min_value=1, widget=forms.NumberInput(attrs={'min': 1}), required=False)
  maxNumPezziDisponibili = forms.IntegerField(label="maxNumPezziDisponibili", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000}), required=False)
  
  def clean(self):
        cleaned_data = super().clean()
        min_prezzo = cleaned_data.get("minPrezzo")
        max_prezzo = cleaned_data.get("maxPrezzo")
        min_prodotti = cleaned_data.get("minNumPezziDisponibili")
        max_prodotti = cleaned_data.get("maxNumPezziDisponibili")

        if min_prezzo is not None and max_prezzo is not None:
            if min_prezzo >= max_prezzo:
                raise forms.ValidationError("Il prezzo minimo deve essere strettamente minore del prezzo massimo.")
        
        if min_prodotti is not None and max_prodotti is not None:
            if min_prodotti > max_prodotti:
                raise forms.ValidationError("Il numero minimo di prodotti disponibili non può essere maggiore del numero massimo.")

        return cleaned_data
      
      
     # filtro per cercare all'interno del resoconto vendite
class FiltroResocontoVenditeForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100, required=False)
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100, required=False)
  minPrezzo = forms.FloatField(label="minPrezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01}), required=False)
  maxPrezzo = forms.FloatField(label="maxPrezzo", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000}))
  minNumPezziVenduti = forms.IntegerField(label="minNumPezziVenduti", min_value=0, widget=forms.NumberInput(attrs={'min': 0}), required=False)
  maxNumPezziVenduti = forms.IntegerField(label="maxNumPezziVenduti", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000}), required=False)
  
  def clean(self):
    cleaned_data = super().clean()
    min_prezzo = cleaned_data.get("minPrezzo")
    max_prezzo = cleaned_data.get("maxPrezzo")
    min_prodotti = cleaned_data.get("minNumPezziVenduti")
    max_prodotti = cleaned_data.get("maxNumPezziVenduti")

    if min_prezzo is not None and max_prezzo is not None:
      if min_prezzo >= max_prezzo:
        raise forms.ValidationError("Il prezzo minimo deve essere strettamente minore del prezzo massimo.")
        
      if min_prodotti is not None and max_prodotti is not None:
        if min_prodotti > max_prodotti:
          raise forms.ValidationError("Il numero minimo di prodotti venduti non può essere maggiore del numero massimo.")

        return cleaned_data