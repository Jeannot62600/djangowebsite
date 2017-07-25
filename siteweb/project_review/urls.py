from django.conf.urls import url
from project_review import views
app_name = 'project_review'

urlpatterns = [
    url(r'^project/$', views.index, name='index'),
    url(r'^project/(?P<slug>[\w-]+)/$', views.proj, name='proj'),
]
