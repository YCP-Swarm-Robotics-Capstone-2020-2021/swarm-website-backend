from django.db import models

from core.models import Contribution
from core.models import PersonalPage

class DevPersonalPage(PersonalPage):
    expectedGraduationYear = models.IntegerField()
    biography = models.TextField()
    motivationForWorking = models.TextField()
    contributions = models.ManyToManyField(Contribution)