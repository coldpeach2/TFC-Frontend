from datetime import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.gis.geos import Point
import datetime
from datetime import timedelta
import decimal
from django.utils.dateparse import parse_datetime
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
    
    PLANS = { 
    ('Free', 'Free'),
    ('14.99/month', '14.99/month'), 
    ('149.99/year', '149.99/year')
    }

    subscription_choices = models.CharField(max_length=120, choices=PLANS, default='Free')
    
class UserSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users_subscription')
    card_info = models.IntegerField(null=True)
    subscription_plan = models.ForeignKey('SubscriptionPlan', on_delete=models.CASCADE, null=True)
    _amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    active = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=False, null=True)
    _next_payment = models.DateTimeField(auto_now_add=False, null=True)
    end_date = models.DateTimeField(auto_now_add=False, null=True)

    @property
    def activate(self):
        self.active = True
        self.start_date = datetime.datetime.now()
        self.save(update_fields=['active', 'start_date'])
        return self.start_date 

    @property
    def deactivate(self):
        self.active = False
        self.end_date = datetime.datetime.now()
        self.save(update_fields=['active', 'end_date'])
        return self.active

    def make_payment(self):
        #field_value = getattr(self, 'subscription_plan')
        #sub = getattr(field_value, 'subscription_choices')
        #sub_plan = sub['subscription_choices']
        sub_plan = self.subscription_plan.subscription_choices
        date_str = getattr(self, 'start_date')
        date_started = parse_datetime(str(date_str))
        if sub_plan == '14.99/month':
            price = decimal.Decimal(14.99)
            frequency = 30
            self._amount_paid = decimal.Decimal(self.amount_paid) + price
        else: 
            price = decimal.Decimal(149.99)
            frequency = 365
            self._amount_paid = decimal.Decimal(self.amount_paid) + price
        self._next_payment = date_started + timedelta(days=frequency)
        paid = getattr(self, '_amount_paid')
        next_pay = getattr(self, '_next_payment')
        PaymentHistory.objects.create(user=self, amount=paid, next_payment=next_pay)
        return self.next_payment
            
    @property
    def amount_paid(self):
        self.save(update_fields=['_amount_paid'])
        return self._amount_paid

    @property
    def next_payment(self):
        self.save(update_fields=['_next_payment'])
        return self._next_payment

class PaymentHistory(models.Model):
    user = models.ForeignKey(UserSubscription, on_delete=models.CASCADE, related_name='usersubscriptions_paymenthistory')
    payment_date = models.DateTimeField(auto_now_add=True, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    next_payment = models.CharField(max_length=120, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['payment_date', 'amount'],
                name = 'together'
                )
            ]
    
