from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
  username = forms.CharField(label="Username", min_length=5, max_length=100, widget=forms.TextInput(attrs={'id': 'username'}))
  password = forms.CharField(label="Password", min_length=5, widget=forms.PasswordInput(attrs={'id': 'password'}))

class RegistrazioneForm(forms.Form):
  username = forms.CharField(label="Username", min_length=5, max_length=100, widget=forms.TextInput(attrs={'id': 'username'}))
  password = forms.CharField(label="Password", min_length=5, widget=forms.PasswordInput(attrs={'id': 'password'}))

class CheckoutForm(forms.Form):
  indirizzo = forms.CharField(label="Indirizzo", min_length=5, max_length=100, widget=forms.TextInput(attrs={'id': 'indirizzo'}))
  codice_paypal = forms.CharField(label="Codice paypal", min_length=16, max_length=16, widget=forms.NumberInput(attrs={'id': 'codice_paypal'}))

class ModificaProdottoForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100, widget=forms.TextInput(attrs={'id': 'nome'}))
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100, widget=forms.TextInput(attrs={'id': 'tipologia'}))
  descrizione = forms.CharField(label="Descrizione", min_length=1, max_length=500, widget=forms.TextInput(attrs={'id': 'descrizione'}))
  prezzo = forms.FloatField(label="Prezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01, 'id': 'prezzo'}))
  quantita = forms.IntegerField(label="Quantita", min_value=0, widget=forms.NumberInput(attrs={'min': 0, 'id': 'quantita'}))

class AggiuntaNuovoProdottoForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100, widget=forms.TextInput(attrs={'id': 'nome'}))
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100, widget=forms.TextInput(attrs={'id': 'tipologia'}))
  descrizione = forms.CharField(label="Descrizione", min_length=1, max_length=500, widget=forms.TextInput(attrs={'id': 'descrizione'}))
  prezzo = forms.FloatField(label="Prezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01, 'id': 'prezzo'}))
  quantita = forms.IntegerField(label="Quantita", min_value=0, widget=forms.NumberInput(attrs={'min': 0, 'id': 'quantita'}))





# filtro per cercare all'interno della home utente
class FiltroHomeUtenteForm(forms.Form):
  nome = forms.CharField(label="Nome", max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'nome'}))
  tipologia = forms.CharField(label="Tipologia", max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'tipologia'}))
  minPrezzo = forms.FloatField(label="minPrezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01, 'id': 'minPrezzo'}), required=False)
  maxPrezzo = forms.FloatField(label="maxPrezzo", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000, 'id': 'maxPrezzo'}), required=False)
  
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
  nome = forms.CharField(label="Nome", min_length=3, max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'nome'}))
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'tipologia'}))
  minPrezzo = forms.FloatField(label="minPrezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01, 'id': 'minPrezzo'}), required=False)
  maxPrezzo = forms.FloatField(label="maxPrezzo", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000, 'id': 'maxPrezzo'}), required=False)
  minNumPezzi = forms.IntegerField(label="minNumPezzi", min_value=1, widget=forms.NumberInput(attrs={'min': 1, 'id': 'minNumPezzi'}), required=False)
  maxNumPezzi = forms.IntegerField(label="maxNumPezzi", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000, 'id': 'maxNumPezzi'}), required=False)
  
  def clean(self):
        cleaned_data = super().clean()
        min_prezzo = cleaned_data.get("minPrezzo")
        max_prezzo = cleaned_data.get("maxPrezzo")
        minNumPezzi = cleaned_data.get("minNumPezzi")
        maxNumPezzi = cleaned_data.get("maxNumPezzi")

        if min_prezzo is not None and max_prezzo is not None:
            if min_prezzo >= max_prezzo:
                raise forms.ValidationError("Il prezzo minimo deve essere strettamente minore del prezzo massimo.")
        
        if minNumPezzi is not None and maxNumPezzi is not None:
            if minNumPezzi > maxNumPezzi:
                raise forms.ValidationError("Il numero minimo di prodotti disponibili non può essere maggiore del numero massimo.")

        return cleaned_data
      
      
     # filtro per cercare all'interno del resoconto vendite
class FiltroResocontoVenditeForm(forms.Form):
  nome = forms.CharField(label="Nome", min_length=3, max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'nome'}))
  tipologia = forms.CharField(label="Tipologia", min_length=2, max_length=100, required=False, widget=forms.TextInput(attrs={'id': 'tipologia'}))
  minPrezzo = forms.FloatField(label="minPrezzo", min_value=0.01, widget=forms.NumberInput(attrs={'min': 0.01, 'id': 'minPrezzo'}), required=False)
  maxPrezzo = forms.FloatField(label="maxPrezzo", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000, 'id': 'maxPrezzo'}), required=False)
  minPezziVenduti = forms.IntegerField(label="minPezziVenduti", min_value=0, widget=forms.NumberInput(attrs={'min': 0, 'id': 'minPezziVenduti'}), required=False)
  maxPezziVenduti = forms.IntegerField(label="maxPezziVenduti", max_value=10000, widget=forms.NumberInput(attrs={'max': 10000, 'id': 'maxPezziVenduti'}), required=False)
  
  def clean(self):
    cleaned_data = super().clean()
    min_prezzo = cleaned_data.get("minPrezzo")
    max_prezzo = cleaned_data.get("maxPrezzo")
    minPezziVenduti = cleaned_data.get("minPezziVenduti")
    maxPezziVenduti = cleaned_data.get("maxPezziVenduti")

    if min_prezzo is not None and max_prezzo is not None:
      if min_prezzo >= max_prezzo:
        raise forms.ValidationError("Il prezzo minimo deve essere strettamente minore del prezzo massimo.")
        
      if minPezziVenduti is not None and maxPezziVenduti is not None:
        if minPezziVenduti > maxPezziVenduti:
          raise forms.ValidationError("Il numero minimo di prodotti venduti non può essere maggiore del numero massimo.")

        return cleaned_data