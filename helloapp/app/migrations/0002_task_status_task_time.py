# Generated by Django 4.0.4 on 2022-08-07 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
