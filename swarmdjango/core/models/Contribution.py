from django.db import models

class Contribution(models.Model):
    link = models.TextField()
    descriptions = models.TextField()
    fileName = models.TextField()