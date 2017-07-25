from django.conf.urls import url
from infopage import views

app_name = 'infopage'

urlpatterns = [
    url(r'^info/$', views.index, name='index'),
    url(r'^info/(?P<slug>[\w-]+)/$', views.info, name='info'),
]
