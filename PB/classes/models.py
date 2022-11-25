from django.db import models
from accounts.models import User
from studios.models import Studio

# Create your models here.

class Classes(models.Model):
    studio = models.ManyToManyField(Studio, related_name='studios_studio')
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    coach = models.CharField(max_length=120)
    keywords = models.CharField(max_length=120)
    capacity = models.IntegerField()
    times = models.CharField(max_length=120)
    enrolled = models.ManyToManyField(User)