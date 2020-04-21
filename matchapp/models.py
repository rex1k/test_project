from django.db import models


# Create your models here.


class MatchModel(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
