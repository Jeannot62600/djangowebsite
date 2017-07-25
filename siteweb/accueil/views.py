from django.shortcuts import render, get_object_or_404
from accueil.models import *

def index(request):
    parts = Part.objects.all()
    return render(request, 'index.html', {'parts': parts})
