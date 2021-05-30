from django.db.models import fields
from rest_framework import serializers
from historicos.models import Historicos
class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historicos
        fields = '__all__'