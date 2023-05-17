from rest_framework import serializers
from app.models import Cobertura
from Planes.models import Plan




class CoberturaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Cobertura
        fields =  '__all__'
    

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields =  '__all__'
    

class LocalizacionSerealizer(serializers.Serializer):
    longitud = serializers.FloatField()
    latitud = serializers.FloatField()
    
