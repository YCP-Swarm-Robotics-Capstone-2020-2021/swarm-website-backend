from django.db import models
from core.models import Log


class Run(models.Model):
    dateTime = models.DateTimeField()
    deviceID = models.TextField(default='NotSet')
    runID = models.IntegerField(default='NotSet')
    logID = models.ForeignKey(Log, on_delete=models.CASCADE)
    filePath = models.TextField(default='NotSet')