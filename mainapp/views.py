from django.http.response import Http404
from django.shortcuts import render, redirect

from mainapp.forms import Gameform

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
    if request.method != 'POST':
        #No data submitted; create a blank form.
        newGameForm = Gameform()
    else:
        # POST data submitted; process data.
        form = Gameform(data=request.POST)
        if form.is_valid():
            newGame = form.save(commit=False)
            newGame.owner = request.user
            newGame.save()
            return redirect('mainapp:mygames')
    #Display a blank or invalid form
    context = {'form' : newGameForm}
    return render(request, 'mainapp/addgame.html', context)

def editgame(request, game_id):
    #Edit an existing game.
    game = Game.objects.get(id=game_id)
    if game.owner != request.user:
        raise Http404
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = Gameform(instance=game)
    else:
        # POST data submitted; process data.
        form = Gameform(instance=game, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainapp:mygames')
    #Display a blank or invalid form
    context = {'game' : game, 'form' : form}
    return render(request, 'mainapp/editgame.html', context)
    


def game(request, game_id):
    """Show a single boardgame and all it's features and properties"""
    game = Game.objects.get(id=game_id) 
       
    #picture RESEARCH how to set a game image for a game. Great if user can upload it.
    context = {'game': game }
    return render(request, 'mainapp/game.html', context)