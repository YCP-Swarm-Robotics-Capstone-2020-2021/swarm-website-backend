from django.db import models

class Comment(models.Model):
    #TODO:
    #userId
    text = models.TextField()
    dateTime = models.DateTimeField(auto_now_add = True)
    replies = models.ManyToManyField('self')
