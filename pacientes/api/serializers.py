from pacientes.models import Pacientes
from rest_framework import serializers

class PacientesSerializer (serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'