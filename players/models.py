from django.db import models

from teams.models import Team

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
