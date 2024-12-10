from rest_framework import serializers
from .models import programmer, Aprendiz


class ProgrammerSerializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        #fields = ('fullname', 'nickname', 'age')
        fields = '__all__'

class AprendizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aprendiz
        #fields = ('nombre', 'apellido', 'sexo')
        fields = '__all__'


