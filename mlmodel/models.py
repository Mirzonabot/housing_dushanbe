from django.db import models

# Create your models here.

class Prediction(models.Model):
    
    floor = models.IntegerField(default=0)
    rooms = models.IntegerField(default=0)
    area = models.FloatField(default=0)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    price = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.created_on)