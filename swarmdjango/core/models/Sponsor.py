from django.db import models

from core.models import User
from core.models import PersonalPage

class Sponsor(User):
    companyName = models.TextField()
    page = models.OneToOneField('PersonalPage', on_delete=models.CASCADE, blank=True)