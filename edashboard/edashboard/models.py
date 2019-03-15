import datetime
from django.db import models
from django.db.models.base import ModelBase
from django.utils import timezone


class Building(models.Model):
    b_name = models.CharField(max_length=200)
    b_num = models.CharField(max_length=10, primary_key=True)
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

'''
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text'''
