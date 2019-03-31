from django.db import models

from teams.models import Team
from weeks.models import Week
from model_utils import Choices

class Playerplus(models.Model):
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
        'Johnson, John',
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
    plus_one = models.IntegerField(default=0)
    ton_eighty = models.IntegerField(default=0)
    nine_hitter = models.IntegerField(default=0)
    mvp = models.IntegerField(default=0)
    high_out = models.IntegerField(default=0)
    six_bull = models.IntegerField(default=0)
    
    def __str__(self):
        return self.player_name
