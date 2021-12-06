from django.urls import path,include

from . import views

app_name = 'users'
urlpatterns = [
    #users page
    path('', views.userindex, name="usersindex"),
    path('register/', views.register, name='register'),
]