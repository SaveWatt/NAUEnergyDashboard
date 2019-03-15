import datetime
import csv
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save
from django.contrib.auth.models import User

time = models.DateTimeField(timezone.now())

class BuildingSearch(models.Model):
    choice_text = models.CharField(max_length=200)
    def getBuildingString():
        buildings = []
        with open('edashboard/buildings.csv','r') as f:
            lines= f.readlines()
            i=0
            for line in lines:
                if "number" not in line:
                    data = (line.strip()).split(",")
                    buildings.append(data[1] + " (" + data[0] + ")")
                    i+=1
        f.close()
        return buildings

class ExportBuilding(models.Model):
    date = models.DateTimeField()
    usage = models.IntegerField()
    sensor = models.IntegerField()
    build_num = models.IntegerField()
    util = models.CharField(max_length=200)
    def __str__(self):
        return self.usage
    class Meta:
       managed = False
       db_table = 'export_demo'

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.PROTECT)
   description = models.CharField(max_length=100, default='')
   permission = models.IntegerField(default=1)

   def __str__(self):
       return self.user.username

def create_profile(sender, **kwargs):
   if kwargs['created']:
       user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
