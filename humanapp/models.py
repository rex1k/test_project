from django.db import models

# Create your models here.



class HumanModel(models.Model):
    avatar = models.ImageField(verbose_name='avatar', upload_to='static/humans_avatars', blank=True)
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)