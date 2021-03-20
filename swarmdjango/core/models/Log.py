from django.db import models
from django.contrib.postgres.fields import JSONField


class Log(models.Model):
    dateTime = models.DateTimeField()
    deviceID = models.TextField(default='NotSet')
    # Here would be the runs field, but Django just uses foreign keys
    filePath = models.TextField(default='NotSet')
    log = JSONField()