from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(unique=True)
    password = models.TextField()
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.TextField(max_length=20, blank=True)
    accountLevel = models.IntegerField(default=0);
    isActive = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

# https://github.com/veryacademy/YT-Django-DRF-Simple-Blog-Series-JWT-Part-3/blob/master/django/users/models.py