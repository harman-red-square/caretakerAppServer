from django.db import models


# Create your models here.
class Network(models.Model):
    geoLocation = models.BooleanField(default=False)

