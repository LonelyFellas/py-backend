from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.CharField(max_length=50)
    tel = models.CharField(max_length=15, blank=True, null=True)

    REQUIRED_FIELDS = ['role', 'email', 'tel']

    def __str__(self):
        return self.username
