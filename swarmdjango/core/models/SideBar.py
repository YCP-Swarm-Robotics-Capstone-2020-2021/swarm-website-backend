from django.db import models
from django.db.models import JSONField

class SideBar(models.Model):
    content = JSONField(blank=True, null=True)