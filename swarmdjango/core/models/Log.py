from django.db import models
from django.contrib.postgres.fields import JSONField

#from core.models import Robot
#from core.models import Run

class Log(models.Model):
    dateTime = models.DateTimeField()
    #robot = models.OneToOneField('Robot', on_delete=models.CASCADE)
    #run = models.OneToOneField('Run', on_delete=models.CASCADE)
    log = models.JSONField()