from datetime import date

from django.core.validators import RegexValidator
from django.db import models
from accounts.models import User
from django.contrib.gis.geos import Point
from django.utils import timezone

from datetime import date
# Create your models here.


class Studio(models.Model):
    name = models.CharField(max_length=120, primary_key=True)
    address = models.CharField(max_length=120)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    postal_code_regex = RegexValidator(regex=r"^[A-Z]\d[A-Z]\s?\d[A-Z]\d$",
                                       message="Postal codes must be entered in the following format: A1A 1A1 or "
                                               "A1A1A1")
    postal_code = models.CharField(validators=[postal_code_regex], max_length=7)
    phone_regex = RegexValidator(regex=r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$",
                                 message="Phone number must be entered in the format: "
                                         "'+111111111 or 111-111-1111 (+ optional)'. Up to 10 digits allowed.")
    phone_num = models.CharField(validators=[phone_regex], max_length=15)
    images = models.ImageField(upload_to='studios', null=True)

    @property
    def studio_loc(self):
        studio_loc = Point(self.lon, self.lat, srid=4326)
        return studio_loc


class Amenity(models.Model):
    studio = models.ManyToManyField(Studio, related_name='studios_amenity')
    type = models.CharField(max_length=120)

    quantity = models.PositiveIntegerField()


class Classes(models.Model):
    FREQUENCY = {(0, "Once"),
                 (1, "Daily"),
                 (2, "Weekly"),
                 (3, "Monthly"),
                 }

    studio = models.ManyToManyField(Studio, related_name='studios_classes')
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    coach = models.CharField(max_length=120)
    keywords = models.CharField(max_length=120)
    capacity = models.PositiveIntegerField()
    frequency = models.IntegerField(choices=FREQUENCY, null=True)
    start_date = models.DateTimeField(auto_now_add=False, null=True)
    start_time = models.CharField(max_length=120, null=True)
    end_time = models.CharField(max_length=120, null=True)
    cancelled_date = models.DateTimeField(auto_now_add=False, null=True)
    enrolled = models.ManyToManyField(User)

    @property
    def is_cancelled(self):
        return self.cancelled_date is not None

