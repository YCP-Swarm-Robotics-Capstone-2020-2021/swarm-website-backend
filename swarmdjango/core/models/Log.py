from django.db import models
from django.contrib.postgres.fields import JSONField


class Log(models.Model):
    dateTime = models.DateTimeField()
    deviceID = models.TextField()
    runs = JSONField()
    filePath = models.TextField()
    log = JSONField()