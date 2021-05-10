from django.db import models


class Log(models.Model):
    dateTime = models.DateTimeField()
    deviceID = models.TextField(default='NotSet')
    filePath = models.TextField(default='NotSet')