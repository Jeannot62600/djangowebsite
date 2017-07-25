from django.shortcuts import render, get_object_or_404
from infopage.models import *

def index(request):
    infos = Info.objects.all()
    return render(request, 'infos.html', {'infos': infos})

def info(request, slug):
    info = get_object_or_404(Info, slug=slug)
    return render(request, 'info.html', {'info': info})
