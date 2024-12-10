from rest_framework import viewsets
from .serializer import ProgrammerSerializer, AprendizSerializer
from .models import programmer, Aprendiz


# Create your views here.

class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = programmer.objects.all()
    serializer_class = ProgrammerSerializer
    
class AprendizViewSet(viewsets.ModelViewSet):
    queryset = Aprendiz.objects.all()
    serializer_class = AprendizSerializer