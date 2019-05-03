from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Building(models.Model):
    b_name = models.CharField(max_length=200)
    b_num = models.CharField(max_length=10)
    b_alias = models.CharField(max_length=200)

    def __str__(self):
        return self.b_name + ' (' + self.b_num + ')'

class Sensor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=200)
    s_type = models.CharField(max_length=200, default='None')
    s_log = models.CharField(max_length=200, unique=True)
    s_sub_type = models.CharField(max_length=200, default='None')

    def __str__(self):
        return str(self.s_name)

class SensorType(models.Model):
    utility = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=200, default='?')
    alias = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


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
   description = models.CharField(max_length=100, default='Low Level User')
   permission = models.IntegerField(default=1)

   def __str__(self):
       return self.user.username

def create_profile(sender, **kwargs):
   if kwargs['created']:
       user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
