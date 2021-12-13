from django.contrib import admin

from .models import Genre, Game, GameInstance, Owner

admin.site.register(Genre)
admin.site.register(Game)
admin.site.register(GameInstance)
admin.site.register(Owner)
# Register your models here.
