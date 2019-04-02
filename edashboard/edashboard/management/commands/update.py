from django.core.management.base import BaseCommand
from edashboard.backend import BackendRetriever, StaticDataRetriever
import datetime

class Command(BaseCommand):
   help = "This runs the loop of glory, that does as it is told."

   def handle(self, **options):
       sdr = StaticDataRetriever()
       #sdr.update_buildings()
       #sdr.update_sensors()
       BackendRetriever.getData("B60", "Current Demand KW", datetime.datetime(2018, 8, 1, 0, 0), datetime.datetime(2018, 8, 31, 23, 59))
