from django.core.management.base import BaseCommand
import subprocess
class Command(BaseCommand):
     help = 'Startup'
     def handle(self, *args, **kwargs):
        subprocess.call(['sh', '/Users/areej/CSC309-Fall2022/group_9543/PB/startup.sh'])
        #subprocess.call(['sh', '/Users/areej/CSC309-Fall2022/group_9543/PB/run.sh'])

