from django.db import models
from django.utils import timezone

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    team_abbr = models.CharField(max_length=3, default='XXX')
    elo_rank = models.IntegerField(default=1500)
    ranked_games_played = models.IntegerField(default=0)
    k_factor = models.IntegerField(default=32)
    add_date = models.DateTimeField('date added', default=timezone.now)

    def __str__(self):
        return self.team_name

class Game(models.Model):
    team_winner = models.ManyToManyField(Team, related_name='team_winner')
    winner_score = models.IntegerField(default = 0)
    team_loser = models.ManyToManyField(Team, related_name='team_loser')
    loser_score = models.IntegerField(default = 0)
    game_date = models.DateTimeField('game date', default=timezone.now)
