from django.urls import path
from django.urls import path

from . import views

app_name = 'mainapp'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('game/<int:game_id>/', views.game, name='game'),
    path('mygames/', views.mygames, name='mygames'),
    path('addgame/', views.addgame, name='addgame'),
    path('editgame/<int:game_id>/', views.editgame, name='editgame'),
    
]