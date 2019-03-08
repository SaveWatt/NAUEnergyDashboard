import datetime
import csv
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import UserManager

time = models.DateTimeField(timezone.now())

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Demo(models.Model):
    date = models.DateTimeField('Event Date')
    value = models.IntegerField()
    objects = UserManager()
    def getvalue(self):
        return self.value
    def getdate(self):
        return self.date
    class Meta:
       managed = False
       db_table = 'Demo'

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

class LoginForm(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)



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
