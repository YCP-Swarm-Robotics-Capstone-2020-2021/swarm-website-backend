from django.db import models

from core.models import Entry

class Wiki(models.Model):
    title = models.TextField()
    entries = models.ManyToManyField('Entry')
    briefDescription = models.TextField()