from django.db import models
from phone_field import PhoneField
from teams.models import Team

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True) 
    name = models.CharField(max_length=30)
    phone = PhoneField(blank=True)
    email = models.EmailField(max_length=50,blank=True)

    def __str__(self):
        return self.name
