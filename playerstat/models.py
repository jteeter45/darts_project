from django.db import models

from teams.models import Team
from weeks.models import Week
from players.models import Player
from model_utils import Choices

class Playerstat(models.Model):
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    player_name = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True)
    WON_LOSS_CHOICES = Choices(
        'W',
        'L',
        'DNP'
    )
    five_singles_wldnp = models.CharField(choices=WON_LOSS_CHOICES, default=WON_LOSS_CHOICES.DNP, max_length=3)
    five_singles_win = models.IntegerField(default=0)
    five_singles_loss = models.IntegerField(default=0)
    cricket_singles_wldnp = models.CharField(choices=WON_LOSS_CHOICES, default=WON_LOSS_CHOICES.DNP, max_length=3)
    cricket_singles_win = models.IntegerField(default=0)
    cricket_singles_loss = models.IntegerField(default=0)
    five_doubles_wldnp = models.CharField(choices=WON_LOSS_CHOICES, default=WON_LOSS_CHOICES.DNP, max_length=3)
    five_doubles_win = models.IntegerField(default=0)
    five_doubles_loss = models.IntegerField(default=0)
    cricket_doubles_wldnp = models.CharField(choices=WON_LOSS_CHOICES, default=WON_LOSS_CHOICES.DNP, max_length=3)
    cricket_doubles_win = models.IntegerField(default=0)
    cricket_doubles_loss = models.IntegerField(default=0)


    def __int__(self):
        return self.player_name
