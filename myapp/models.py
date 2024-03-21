from django.db import models

class Coordinates(models.Model):
    id = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
