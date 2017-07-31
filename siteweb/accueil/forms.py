from django import forms

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class InscriptionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    last_name = forms.CharField(label="Nom", max_length=30)
    first_name = forms.CharField(label="prénom", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
    email = forms.EmailField(label="Email")
