# Generated by Django 3.0.8 on 2020-08-09 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_auto_20200809_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskform',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
