# Generated by Django 2.1.5 on 2019-04-23 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edashboard', '0015_auto_20190423_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensortype',
            name='alias',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
