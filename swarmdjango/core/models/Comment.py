from django.db import models

from core.models import User

class Comment(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE)
    text = models.TextField()
    dateTime = models.DateTimeField(auto_now_add = True)
    replies = models.ManyToManyField('self', blank=True)
