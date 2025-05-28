from rest_framework import serializers
from . models import Avenger

class AvengerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Avenger
        fields ='__all__'