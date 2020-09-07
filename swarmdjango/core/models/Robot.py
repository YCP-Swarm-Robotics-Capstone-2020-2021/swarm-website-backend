from django.db import models


class Robot(models.Model):
    name = models.TextField()
    ip = models.GenericIPAddressField()
