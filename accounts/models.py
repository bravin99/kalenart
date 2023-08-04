from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id_number = models.CharField(max_length=55, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar-images/', null=True, blank=True)
