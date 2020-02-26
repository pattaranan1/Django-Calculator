from django.db import models

# Create your models here.

class Calculated_history(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    operator = models.CharField(max_length=1)
    result = models.FloatField()