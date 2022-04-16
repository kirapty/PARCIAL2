from django.db import models
from numpy import object0
from django.db import models

# Create your models here.
class Years(models.Model):
    Pais = models.CharField(max_length=200)
    año = models.CharField(max_length=200)
    porcentaje = models.CharField(max_length=200)
    website = models.CharField(max_length=200)