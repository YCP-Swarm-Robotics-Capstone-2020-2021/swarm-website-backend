from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class CustomUSerManager(BaseUserManager):
    def create_superuser(self, email, username, firstName, lastName, accountLevel, isActive, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, username, firstName, lastName, accountLevel, isActive, password, **other_fields)

    def create_user(self, email, username, firstName, lastName, accountLevel, isActive, password, **other_fields):
        if not email or username:
            raise ValueError('You must provide an email and username for an account')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, firstName=firstName,
                          lastName=lastName, accountLevel=accountLevel,
                          isActive=isActive, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.TextField(unique=True)
    password = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    firstName = models.CharField(max_length=20, blank=True)
    lastName = models.TextField(max_length=20, blank=True)
    accountLevel = models.IntegerField(default=0)
    isActive = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    objects = CustomUSerManager()

    def __str__(self):
        return self.username
