# Generated by Django 2.1.5 on 2019-05-02 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edashboard', '0018_auto_20190429_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensor',
            name='s_sub_type',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
