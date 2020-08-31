from django.db import models

class Change(models.Model):
    #TODO:
    #userId
    dateTime = models.DateTimeField(auto_now_add = True)
    context = models.TextField()
    textAdded = models.TextField()