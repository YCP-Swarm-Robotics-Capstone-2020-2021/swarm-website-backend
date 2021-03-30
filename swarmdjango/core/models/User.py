from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    username = models.TextField(unique=True)
    password = models.TextField()
    email = models.EmailField()
    firstName = models.TextField()
    lastName = models.TextField()
    accountLevel = models.IntegerField(default=0);

    USERNAME_FIELD = 'username'

# https://github.com/veryacademy/YT-Django-DRF-Simple-Blog-Series-JWT-Part-3/blob/master/django/users/models.py