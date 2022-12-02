from django.contrib import admin
from .models import User, SubscriptionPlan

admin.site.register(User)
# Register your models here.

admin.site.register(SubscriptionPlan)
