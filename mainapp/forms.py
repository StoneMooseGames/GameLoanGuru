from django import forms
from django.forms import fields

from .models import Game

class Gameform(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['title', 'genre', 'summary']
        labels = {'name' : ''}