from django.db import models

from core.models import User

class Change(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, blank=True)
    dateTime = models.DateTimeField(auto_now_add = True)
    context = models.TextField()
    textAdded = models.TextField()