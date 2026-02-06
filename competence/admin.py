from django.contrib import admin

from competence.models import Categorie


# Register your models here.
@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('libelle','description')