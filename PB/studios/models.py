from django.db import models
from django.contrib.gis.db.models import PointField
# Create your models here.


class Studio(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    geolocation = PointField(default=None)
    postal_code = models.CharField(max_length=7)
    phone_num = models.CharField(max_length=12)
    images = models.ImageField(upload_to='studios')


class Amenity(models.Model):
    type = models.CharField(max_length=120)
    quantity = models.IntegerField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
