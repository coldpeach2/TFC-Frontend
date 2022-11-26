from django.db import models
from accounts.models import User
from studios.models import Studio
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.

class Classes(models.Model):
    #studio = GenericRelation(Studio)
    studio = models.ManyToManyField(Studio, related_name='studios_classes')
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    coach = models.CharField(max_length=120)
    keywords = models.CharField(max_length=120)
    capacity = models.IntegerField()
    times = models.CharField(max_length=120)
    enrolled = models.ManyToManyField(User)