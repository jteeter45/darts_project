from django.db import models
from decimal import Decimal
from weeks.models import Week
from teams.models import Team

class Standing(models.Model):
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True)
    wins = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    losses = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
       

    def __int__(self):
        return self.team
