from django.db import models

from core.models import PersonalPage

class SponsorPersonalPage(PersonalPage):
    missionStatement = models.TextField()
    reasonForSponsorship = models.TextField()
    companyLink = models.URLField()