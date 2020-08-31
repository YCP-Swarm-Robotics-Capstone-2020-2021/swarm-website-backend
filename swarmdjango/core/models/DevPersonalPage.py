from django.db import models

from core.models import Contribution

class DevPersonalPage(models.Model):
    expectedGraduationYear = models.IntegerField()
    biography = models.TextField()
    motivationForWorking = models.TextField()
    contributions = models.ManyToManyField(Contribution)