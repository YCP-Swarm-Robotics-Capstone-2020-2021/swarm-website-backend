from django.db import models

from core.models import SideBar
from core.models import Change
from core.models import Heading
from core.models import Comment

class Entry(models.Model):
    title = models.TextField()
    text = models.TextField()
    sideBar = models.OneToOneField('SideBar', on_delete=models.CASCADE)
    #TODO:
    #contributors
    headings = models.ManyToManyField('Heading')
    comments = models.ManyToManyField('Comment')
    log = models.ManyToManyField('Change')