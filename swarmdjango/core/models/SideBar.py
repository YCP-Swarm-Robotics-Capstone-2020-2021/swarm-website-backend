from django.db import models
from django.contrib.postgres.fields import JSONField

class SideBar(models.Model):
    content = JSONField()