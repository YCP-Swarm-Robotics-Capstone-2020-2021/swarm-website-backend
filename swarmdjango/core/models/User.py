from django.db import models

class User(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    firstName = models.TextField()
    lastName = models.TextField()
