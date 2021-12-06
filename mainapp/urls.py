from django.urls import path
from django.urls import path

from . import views

app_name = 'mainapp'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]