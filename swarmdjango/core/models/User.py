from django.db import models

class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.EmailField()
    firstName = models.TextField()
    lastName = models.TextField()
    accountLevel = models.IntegerField(default=0)
