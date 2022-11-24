from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from rest_framework.permissions import IsAdminUser

from .models import Studio
# Register your models here.

admin.site.register(Studio)
