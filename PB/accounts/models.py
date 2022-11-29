from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.gis.geos import Point
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        extra_fields = {"is_staff": False, "is_superuser": False, **extra_fields}
        if not email:
            raise ValueError("Users must have an email address")
        user = User(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields = {**extra_fields, "is_staff": True, "is_superuser": True}
        user = self.create_user(email=email, password=password, **extra_fields)
        user.save()
        return user

class User(AbstractUser):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    email = models.EmailField(max_length=120, unique=True)
    avatar = models.ImageField(null=True)
    phone_num = models.IntegerField(null=True)
    username = None
    password = models.CharField(max_length=120)
    lon = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def user_loc(self):
        user_loc = Point(self.lon, self.lat, srid=4326)
        return user_loc


class SubscriptionPlan(models.Model):
    
    PLANS = {('Free', 'Free'), 
    ('14.99/month', '14.99/month'), 
    ('149.99/year', '149.99/year')
    }

    subscription_choices = models.CharField(max_length=120, choices=PLANS, default='Free')
    start_date = models.DateTimeField(auto_now_add=False, null=True)

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_subscription')
    card_info = models.IntegerField(null=True)
    subscription_plan = models.ForeignKey('SubscriptionPlan', on_delete=models.CASCADE, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    #active = models.BooleanField(default=False)
    #start_date = models.DateTimeField(auto_now_add=False)
    #amount_paid = models.IntegerField(default=0)

    @property
    def is_active(self):
        return self.active

    # def activate_subscription(self):
    #     self.active = True
    #     self.start_date = timezone.now()

class Subscription(models.Model):
    user_subscription = models.ForeignKey(UserSubscription, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    
