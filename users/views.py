from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def userindex(request):
    return render(request, 'registration/usersindex.html')
    
def register(request):
    return render(request, 'registration/register.html')



