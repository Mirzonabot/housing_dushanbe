# Generated by Django 4.1.4 on 2023-01-08 22:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0003_alter_prediction_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prediction',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 8, 22, 3, 0, 741618)),
        ),
    ]