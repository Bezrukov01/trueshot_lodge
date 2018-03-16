from . import views
from django.urls import path, include, re_path

app_name = 'main'
urlpatterns = [
    path(r'', views.home, name='home'),
    re_path(r'^(?P<name>[\w.@+-]+)/$', views.character, name='character'),
]
