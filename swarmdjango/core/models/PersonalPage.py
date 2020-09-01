from django.db import models

class PersonalPage(models.Model):
    pageType = models.TextField()
    pageTitle = models.TextField()