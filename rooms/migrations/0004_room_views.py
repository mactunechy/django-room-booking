# Generated by Django 2.1.4 on 2018-12-20 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20181220_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]