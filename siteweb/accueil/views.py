from django.shortcuts import render, get_object_or_404, redirect
from accueil.models import *
from django.contrib.auth import authenticate, login, logout
from accueil.forms import ConnexionForm, InscriptionForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def index(request):
    parts = Part.objects.all()
    return render(request, 'index.html', {'parts': parts})

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect('/')

def inscription(request):
    error = False

    if request.method == "POST":
        form = InscriptionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            last_name = form.cleaned_data["last_name"]
            last_name = form.cleaned_data["first_name"]
            user = User.objects.create_user(username, email, password)
    else:
        form = InscriptionForm()

    return render(request, 'inscription.html', locals())

@login_required()
def site(request):
    parts = Part.objects.all()
    return render(request, 'site.html', {'parts': parts})
