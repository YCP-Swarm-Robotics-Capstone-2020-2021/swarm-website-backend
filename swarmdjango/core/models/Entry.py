from django.db import models

from core.models import SideBar
from core.models import Change
from core.models import Heading
from core.models import Comment
from core.models import User


class Entry(models.Model):
    title = models.TextField()
    text = models.TextField()
    sideBar = models.OneToOneField('SideBar', on_delete=models.CASCADE, blank=True)
    contributors = models.ManyToManyField('User')
    headings = models.ManyToManyField('Heading', blank=True)
    comments = models.ManyToManyField('Comment', blank=True)
    log = models.ManyToManyField('Change')

    class Meta:
        get_latest_by = 'log'
