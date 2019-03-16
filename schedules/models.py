from django.db import models
from datetime import datetime
from weeks.models import Week

class Schedule(models.Model):
    week = models.ForeignKey(Week, on_delete=models.SET_NULL, null=True) 
    team_one = models.CharField(max_length=2)
    score_one = models.IntegerField(default=0)
    team_two = models.CharField(max_length=2)
    score_two = models.IntegerField(default=0)
    team_three = models.CharField(max_length=2)
    score_three = models.IntegerField(default=0)
    team_four = models.CharField(max_length=2)
    score_four = models.IntegerField(default=0)
    team_five = models.CharField(max_length=2)
    score_five = models.IntegerField(default=0)
    team_six = models.CharField(max_length=2)
    score_six = models.IntegerField(default=0)
    team_seven = models.CharField(max_length=3)
    score_seven = models.IntegerField(default=0)
    team_eight = models.CharField(max_length=3)
    score_eight = models.IntegerField(default=0)
    def __str__(self):
        return self.team_one
