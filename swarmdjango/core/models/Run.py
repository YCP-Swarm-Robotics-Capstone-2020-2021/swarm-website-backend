from django.db import models
from django.contrib.postgres.fields import JSONField


class Run(models.Model):
    dateTime = models.DateTimeField()
    deviceID = models.TextField(default='NotSet')
    filePath = models.TextField(default='NotSet')
    run = JSONField()