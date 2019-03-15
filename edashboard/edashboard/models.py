import datetime
import csv
from django.db import models
from django.db.models.base import ModelBase
from django.utils import timezone
from django.contrib.auth.models import UserManager

time = models.DateTimeField(timezone.now())

class Building(models.Model):
    b_name = models.CharField(max_length=200)
    b_num = models.CharField(max_length=10)
    b_alias = models.CharField(max_length=200)

    def __str__(self):
        return self.b_num

class Sensor(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    s_name = models.CharField(max_length=200)
    s_type = models.CharField(max_length=200, default='None')
    s_log = models.CharField(max_length=200)

    def __str__(self):
        return str((self.s_log, self.s_type))

def create_model(db_table):
    class LogMeta(ModelBase):
        def __new__(cls, name, bases, attrs):
            model = super(LogMeta, cls).__new__(cls, name, bases, attrs)
            model.meta.db_table = db_table
            return model

    class Log(models.Model):
        __metaclass__ = LogMeta
        srno = models.IntegerField(db_column='SRNO', primary_key=True)
        sam_val = models.IntegerField(max_length=256)
        sam_date = models.DateTimeField('Date Collected')
        sam_seq = models.IntegerField(max_length=256)

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
