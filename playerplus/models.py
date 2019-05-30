from django.db import models
from players.models import Player
from teams.models import Team
from weeks.models import Week
from model_utils import Choices

class Playerplus(models.Model):
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player_name = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    WON_LOSS_CHOICES = Choices(
        'W',
        'L',
        'DNP'
    )
    plus_one = models.IntegerField(default=0)
    ton_eighty = models.IntegerField(default=0)
    nine_hitter = models.IntegerField(default=0)
    mvp = models.IntegerField(default=0)
    high_out = models.IntegerField(default=0)
    six_bull = models.IntegerField(default=0)
    
    def __int__(self):
        return self.player_name
