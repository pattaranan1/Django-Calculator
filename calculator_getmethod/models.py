from django.db import models

# Create your models here.
class CalculatedGetHistory(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    operator = models.CharField(max_length=1)
    result = models.FloatField()
    
    def __unicode__(self):
        return f'{self.x} {self.operator} {self.y} = {self.result}'

    def __str__(self):
        return f'{self.x} {self.operator} {self.y} = {self.result}'
    
    