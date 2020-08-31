from django.db import models

class PersonalPage(models.Model):

    #TODO:
    #add 'userId' field, will probably want to be a relationship
    #see Contribution/DevPersonalPage relationship

    pageType = models.TextField()
    pageTitle = models.TextField()