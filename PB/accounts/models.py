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
    unsubscribed = (
        ('0', 'None')
    )
    subscription_choices = (
    ('1', '14.99/month'),
    ('2', '149.99/year')   
    )
    subscription = models.CharField(max_length=15, choices=subscription_choices, blank=True, default=unsubscribed)

class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_subscription')
    card_info = models.IntegerField(blank=True)
    subscription_plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=False)
    amount_paid = models.IntegerField(default=0)

    def activate_subscription(self):
        self.active = True
        self.start_date = timezone.now()

