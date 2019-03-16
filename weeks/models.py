from django.db import models
from datetime import date

class Week(models.Model):
    week_char = models.CharField(max_length=1, blank=True, null=True)
    week_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.week_char
