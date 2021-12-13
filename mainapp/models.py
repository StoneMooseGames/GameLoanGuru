from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

import uuid # Required for unique boardgame copies / instances.

# Create your models here.

class Genre(models.Model):
    """Model representing a boardgame genre."""
    name = models.CharField(max_length=200, help_text='Enter a boardgame genre (e.g. Strategy, Cardgame...)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class GameInstance(models.Model):
    """Model representing a specific copy of a boardgame (i.e. that can be borrowed)."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular copy of a boardgame.')

    game = models.ForeignKey('Game', on_delete=models.RESTRICT, null=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    free_date = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Available'),
        ('o', 'On loan'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Game availability',
    )

    class Meta:
        ordering = ['free_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.game.title})'


class Game(models.Model):
    """A Boardgame, including all information regarding that game."""
    title = models.CharField(max_length=200)
    
    # Owner of the boardgame
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Short information about the boardgame
    summary = models.TextField(max_length=200, help_text='Enter a brief description of the book')

    # Genre. A game can belong to several genre's, and many games to same genre's, so that's why we use ManyToManyField.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this boardgame')

    #Picture
    #RESEARCH HOW TO ADD PICTURE

    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        """Title of the Boradgame"""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this boardgame."""
        return reverse('bordgame-detail', args=[str(self.id)])

    
    



    
class Owner(models.Model):
    """Model representing an owner."""
    nickname = models.CharField(max_length=100)
        
    #### HOW TO LINK TO 'USER'?

    class Meta:
        ordering = ['nickname']

    def get_absolute_url(self):
        """Returns the url to access a particular owner instance."""
        return reverse('owner-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.nickname}'