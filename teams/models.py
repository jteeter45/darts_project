from django.db import models

class Team(models.Model):
    abbrev = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    site = models.CharField(max_length=30)

    def __str__(self):
        return self.name
