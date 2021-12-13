from django.shortcuts import render

from .models import Game

# Create your views here.
def index(request):
    allgames = Game.objects.order_by('date_added')
    context = {'allgames' : allgames}
    return render(request, 'mainapp/index.html', context)


def mygames(request):
    allgames = Game.objects.filter(owner=request.user).order_by('date_added')
    context = {'allgames' : allgames}
    return render(request, 'mainapp/mygames.html', context)

def addgame(request):
    return render(request, 'mainapp/addgame.html')


def editgame(request):
    return render(request, 'mainapp/editgame.html')


def game(request, game_id):
    """Show a single boardgame and all it's features and properties"""
    #game = Game.objects.get(id=game_id)    
    #picture RESEARCH how to set a game image for a game. Great if user can upload it.
    owner = Game.add_to_class
    return render(request, 'mainapp/game.html') #add ', context)' to end of line when game.html is ready