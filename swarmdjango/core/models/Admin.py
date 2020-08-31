from django.db import models

from core.models import User
from core.models import PersonalPage

class Admin(User):
    receiveUpdates = models.BooleanField()
