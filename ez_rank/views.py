from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Team, Game

def home(request):
    return HttpResponse("This is the home page.")

def teamlist(request):
    latest_team_list = Team.objects.order_by('-add_date')
    context = {'latest_team_list': latest_team_list}
    return render(request, 'ez_rank/teamlist.html', context)

def gamelist(request):
    games_list = Game.objects.order_by('-game_date')
    context = {'games_list': games_list}
    return render(request, 'ez_rank/gamelist.html', context)

def teamdetail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    return render(request, 'ez_rank/teamdetail.html', {'team': team})

def gamedetail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'ez_rank/gamedetail.html', {'game': game})

