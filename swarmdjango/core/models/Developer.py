from django.db import models

from core.models import User
from core.models import PersonalPage

class Developer(User):
    teamRole = models.TextField()
    page = models.OneToOneField('PersonalPage', on_delete=models.CASCADE)