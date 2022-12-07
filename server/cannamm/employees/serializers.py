from rest_framework import serializers
from .models import *

class EmployeeSerializer(serializers.ModelSerializer):
    #city = serializers.StringRelatedField(many=False)
    class Meta:
        model = Employee
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
