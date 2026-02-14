from django.db import models

# Create your models here.
class Categorie(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Competence(models.Model):
    NIVEAUX_POSSIBLE = [
        (1,'Debutant'),
        (2,'Intermediare'),
        (3,'Expert'),
    ]
    libelle = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    niveaux = models.IntegerField(choices=NIVEAUX_POSSIBLE, default=1)
    categori = models.ForeignKey(Categorie,on_delete=models.CASCADE, related_name='competence')
