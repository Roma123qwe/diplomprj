from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(blank=True, null=True, max_length=128)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []