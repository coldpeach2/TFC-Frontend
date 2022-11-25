from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from PB.studios.models import Studio


class Class(models.Model):
    FREQ_CHOICES = (
        (0, 'None'),
        (1, 'Daily'),
        (2, 'Weekly'),
        (3, 'Biweekly'),
    )
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    coach = models.CharField(max_Length=120)
    key_words = models.CharField(max_length=120)
    capacity = models.IntegerField()
    times = models.DateTimeField()
    frequency = models.IntegerField(choices=FREQ_CHOICES)
    studio = GenericRelation(Studio, on_delete=models.CASCADE)
