from django.db import models

# Create your models here.

class Data(models.Model):

    timestamp = models.DateTimeField(null=False, editable=False, unique=True)
    record = models.BigIntegerField(unique=True, editable=False, null=False)

    ws_10m_avg = models.FloatField()
    
    ws_10m_max = models.FloatField()

    class Meta:
        ordering = ['id']

    
