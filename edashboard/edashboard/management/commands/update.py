from django.core.management.base import BaseCommand
from edashboard.backend import BackendRetriever, StaticDataRetriever
import datetime

class Command(BaseCommand):
   help = "This runs an update of sensor information in the backend database.\
   Sensors information will be gathered from the EnergyCap database according\
   to functions in the StaticDataRetriever. Sensors will be aligned with\
   with buildings, assigned types and sub_types, and will be associated with\
   their respective trendlog according to aliases that can be assigned in the\
   administrative portal."

   def handle(self, **options):
       sdr = StaticDataRetriever()
       sdr.update_sensors()
