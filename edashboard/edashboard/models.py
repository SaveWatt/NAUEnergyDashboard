import datetime
from django.db import models
from django.utils import timezone


class Building(models.Model):
    b_id = models.PrimaryKey()
    b_name = models.CharField(max_length=200)
    b_num = models.CharField(max_length=10)
    b_alias = models.CharField(max_length=200)

    def __str__(self):
        return self.bname

class Sensor(models.Model):
    s_id = models.PrimaryKey()
    s_name = models.CharField(max_length=200)
    s_type = models.CharField(max_lenght=200)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    s_log = models.CharField(max_length=200)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
