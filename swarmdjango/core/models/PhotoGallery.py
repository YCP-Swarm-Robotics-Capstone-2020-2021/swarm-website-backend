from django.db import models

from core.models import User

class PhotoGallery(models.Model):
    fileName = models.TextField()
    caption = models.TextField()
    uploadedBy = models.OneToOneField('User', on_delete=models.CASCADE)