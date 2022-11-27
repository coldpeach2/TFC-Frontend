from django.db import models
#from classes.models import Classes
# Create your models here.
from accounts.models import User
from django.contrib.gis.geos import Point


class Studio(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    address = models.CharField(max_length=120)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    postal_code = models.CharField(max_length=7)
    phone_num = models.CharField(max_length=12)
    images = models.ImageField(upload_to='studios')
    #location = Point((lon, lat), srid=4326)

    @property
    def studio_loc(self):
        #studio_location = Point(self.lon, self.lat)
        #return studio_location 
        studio_loc = Point(self.lon, self.lat, srid=4326)
        return studio_loc

class Amenity(models.Model):
    studio = models.ManyToManyField(Studio, related_name='studios_amenity')
    type = models.CharField(max_length=120)
    quantity = models.IntegerField()

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