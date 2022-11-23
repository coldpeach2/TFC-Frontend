#from django.contrib.gis.db import models
from django.db import models
# Create your models here.
class Studio(models.Model):
    name =  models.CharField(max_length=120)
    address =  models.CharField(max_length=120)
    #geolocation = models.PointField()
    #postal_code = 
    #phone_num = 
    #images = 