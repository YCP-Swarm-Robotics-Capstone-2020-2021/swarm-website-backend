from django.db import models
from core.models import Robot


class Run(models.Model):
    dateTime = models.DateTimeField()
    robots = models.ManyToManyField(Robot)
