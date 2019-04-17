from django.db import models

from teams.models import Team
from weeks.models import Week
from model_utils import Choices

class Playerstat(models.Model):
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    PLAYER_CHOICES = Choices(
        'Adkins, Trey',
        'Baldwin, Craig',
        'Bradley, John',
        'Corbitt, Jeff',
        'Frank, Wayne',
        'Glascoe, Matt',
        'Harris, Chuck',
        'Jablon, Joe',
        'Johnson, Jennifer',
        'JOhnson, John',
        'Masten, Matt',
        'Masten, Pat',
        'Masten, Thomas',
        'Miller, Brooke',
        'Murray, Jess',
        'Nolan, Kevin',
        'Patterson, Eric',
        'Petty, Robert',
        'Pilkenton, Justin',
        'Swing, Ken',
        'Teeter, Jake',
        'Thompson, Frank',
        'Wagner, Terry',
        'Williams, April',
        'Wortman, Darryl',
        'Unknown'
    )
    player_name = models.CharField(choices=PLAYER_CHOICES, default=PLAYER_CHOICES.Unknown, max_length=30) 
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


    def __str__(self):
        return self.player_name
