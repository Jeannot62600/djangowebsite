from django.conf.urls import url
from accueil import views

app_name = 'accueil'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^connexion/$', views.connexion, name='connexion'),
    url(r'^deconnexion/$', views.deconnexion, name='deconnexion'),
    url(r'^site/$', views.site, name='site'),
    url(r'^inscription/$', views.inscription, name='inscription'),
]
