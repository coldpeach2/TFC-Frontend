from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from datetime import datetime, timedelta
from accounts.models import UserSubscription
import pytz

utc=pytz.UTC

class Command(BaseCommand):
     help = 'Make payments on all UserSubscription models if todays date is equal to next_payment property'
     def handle(self, *args, **kwargs):
        now = datetime.now().replace(tzinfo=utc) 
        user_subscriptions = UserSubscription.objects.all()
        for user in user_subscriptions:
            if user.next_payment != None:
                if user.next_payment <= now:
                    user.make_payment
                    self.stdout.write("Made Payment for User")

         
