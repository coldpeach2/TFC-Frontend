from django.db import models
from accounts.models import User
from studios.models import Studio
import datetime


class Class(models.Model):
    FREQ_CHOICES = (
        (0, 'None'),
        (1, 'Daily'),
        (2, 'Weekly'),
        (3, 'Biweekly'),
        (4, 'Monthly')
    )
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    coach = models.CharField(max_length=120)
    key_words = models.CharField(max_length=120)
    capacity = models.IntegerField()
    start_date = models.DateField('Start Date', default=datetime.date.today())
    end_date = models.DateField('End Date', default=None)
    start_time = models.TimeField('CLass Start Time', default=datetime.datetime.now())
    end_time = models.TimeField('Class End Time', default=None)
    frequency = models.IntegerField(choices=FREQ_CHOICES)
    studio = models.ManyToManyField(Studio, related_name='studios_classes')
    enrolled = models.ManyToManyField(User)
    cancelled_date = models.DateField('Cancelled Date', blank=True, null=True)

    @property
    def is_cancelled(self):
        return self.cancelled_date is not None

    def cancel_date(self, date: datetime.date, time: datetime.time):
        if self.start_time == time:
            self.cancelled_date = date
            self.save()
        print(f"Date {date} at {time} has been cancelled")

    def cancel_all(self):
        self.delete()


class CancelClassManager(models.Manager):
    def get_query_set(self):
        return Class.objects.filter(cancelled_date__isnull=False)


class CancelledClass(Class):
    class Meta:
        proxy = True

    objects = CancelClassManager()

