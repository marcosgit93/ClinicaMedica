from pacientes.models import Pacientes
from rest_framework import viewsets
from pacientes.api.serializers import PacientesSerializer


class PacientesViewset(viewsets.ModelViewSet):
    queryset = Pacientes.objects.all()
    serializer_class  = PacientesSerializer