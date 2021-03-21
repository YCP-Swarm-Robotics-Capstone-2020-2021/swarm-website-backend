from django.contrib.auth.models import AbstractUser
from django.db import models


# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#auth-custom-user
# https://stackoverflow.com/questions/51308530/attributeerror-type-object-myuser-has-no-attribute-username-field
class User(AbstractUser):
    username = models.TextField()
    password = models.TextField()
    email = models.EmailField()
    firstName = models.TextField()
    lastName = models.TextField()
    accountLevel = models.IntegerField(default=0)
