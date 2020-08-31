from django.db import models

class Contribution(models.Model):
    link = models.TextField()
    description = models.TextField()
    fileName = models.TextField()