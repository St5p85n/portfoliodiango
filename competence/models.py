from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)