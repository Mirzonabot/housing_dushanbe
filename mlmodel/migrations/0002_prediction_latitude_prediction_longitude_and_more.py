# Generated by Django 4.1.4 on 2023-01-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mlmodel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='prediction',
            name='longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='area',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='floor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='rooms',
            field=models.IntegerField(default=0),
        ),
    ]
