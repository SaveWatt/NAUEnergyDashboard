# Generated by Django 2.1.5 on 2019-02-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edashboard', '0002_auto_20190205_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Event Date')),
                ('value', models.IntegerField()),
            ],
        ),
    ]
