from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Utilisateur(AbstractUser):
    telephone = models.CharField(max_length=11)
    address = models.CharField(max_length=50)