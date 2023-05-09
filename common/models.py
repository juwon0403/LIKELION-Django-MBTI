
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    mbti = models.CharField(max_length=200)
# Create your models here.
