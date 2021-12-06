from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Game(models.Model):
    """A Boardgame, including all information regarding that game."""
    name = models.CharField(max_length=200)
    #Picture
    #free tells if game is free for loaning
    free = models.BooleanField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        """Title of the Boradgame"""
        return self.name