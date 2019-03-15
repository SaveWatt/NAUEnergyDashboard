from django.core.management.base import BaseCommand
from edashboard.StaticDataRetriever import StaticDataRetriever

class Command(BaseCommand):
   help = "This runs the loop of glory, that does as it is told."

   def handle(self, **options):
       sdr = StaticDataRetriever()
       sdr.update_buildings()
       sdr.update_sensors()
