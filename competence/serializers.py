from rest_framework import serializers

from competence.models import Categorie


class CategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'
