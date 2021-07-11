# User needs to send data in json format to app, in order to create new entry in postgres db

from rest_framework import serializers
from .models import TemperaturesByCity

class TempyByCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperaturesByCity
        fields = '__all__'

