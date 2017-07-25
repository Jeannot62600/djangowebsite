from django.shortcuts import render, get_object_or_404
from project_review.models import *

def index(request):
    projs = Project.objects.all()
    return render(request, 'projets.html', {'projs': projs})

def proj(request, slug):
    proj = get_object_or_404(Project, slug=slug)
    return render(request, 'proj.html', {'proj': proj})
