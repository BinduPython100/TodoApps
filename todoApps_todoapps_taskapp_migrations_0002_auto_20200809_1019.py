# Generated by Django 3.0.8 on 2020-08-09 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskform',
            old_name='date',
            new_name='created_on',
        ),
        migrations.AlterField(
            model_name='taskform',
            name='choice',
            field=models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=30, null=True),
        ),
    ]
