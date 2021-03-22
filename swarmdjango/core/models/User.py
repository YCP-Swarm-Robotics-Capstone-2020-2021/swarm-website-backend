from django.db import models
from django.contrib.auth.models import User


class User(User):
    pass
    # username = models.TextField()
    # password = models.TextField()
    # email = models.EmailField()
    # firstName = models.TextField()
    # lastName = models.TextField()
    # accountLevel = models.IntegerField(default=0);
