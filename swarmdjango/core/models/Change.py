from django.db import models

from core.models import User


class Change(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    dateTime = models.DateTimeField(auto_now_add=True)
    context = models.TextField()
    textAdded = models.TextField()

    class Meta:
        get_latest_by = 'dateTime'
