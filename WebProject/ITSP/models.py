from django.db import models
from django_mysql.models import ListCharField


# Create your models here.

class Team(models.Model):
    teamID = models.CharField(max_length=15)
    teamName = models.CharField(max_length= 25)
    members = ListCharField(base_field = models.CharField(max_length = 25) , size = 6, max_length=(6*26))

    def __str__(self):
        return self.teamName
