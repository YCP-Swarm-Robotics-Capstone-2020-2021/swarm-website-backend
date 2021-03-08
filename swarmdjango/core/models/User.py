from django.contrib.auth.models import AbstractUser
from django.db import models


# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#auth-custom-user
class User(AbstractUser):
    username = models.TextField()
    password = models.TextField()
    email = models.EmailField()
    firstName = models.TextField()
    lastName = models.TextField()
    accountLevel = models.IntegerField(default=0)
