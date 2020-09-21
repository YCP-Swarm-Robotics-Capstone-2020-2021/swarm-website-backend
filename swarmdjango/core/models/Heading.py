from django.db import models

from core.models import Change

class Heading(models.Model):
    title = models.TextField()
    text = models.TextField()
    subHeadings = models.ManyToManyField('self', blank=True)
    log = models.ManyToManyField('Change')