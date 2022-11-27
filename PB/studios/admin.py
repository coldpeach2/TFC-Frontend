from django.contrib import admin
from .models import Studio, Classes, Amenity
# Register your models here.

admin.site.register(Studio)
admin.site.register(Amenity)
admin.site.register(Classes)
