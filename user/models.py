from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    password = models.CharField(max_length=50, blank=True)
    password2 = models.CharField(max_length=50, blank=True)

    REQUIRED_FIELDS = ['password', 'password2']

    def __str__(self):
        return self.username
