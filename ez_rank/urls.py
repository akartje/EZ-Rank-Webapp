from django.urls import path

from . import views

app_name = 'ez_rank'
urlpatterns = [
    # home page
    path('', views.home, name = 'home'),
    # team list
    path('teams/', views.teamlist, name='teamlist'),
    #game list
    path('games/', views.gamelist, name = 'gamelist'),
    #team detail
    path('teams/<int:team_id>/', views.teamdetail, name='teamdetail'),
    #game detail
    path('games/<int:game_id>/', views.gamedetail, name='gamedetail'),
]