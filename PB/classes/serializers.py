from rest_framework import serializers
from classes.models import Classes
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class ClassScheduleSerializer(serializers.Serializer):
    class Meta:
        model = Classes
        fields = ('studio', 'name', 'description', 'coach', 'keywords', 'capacity', 'times', 'enrolled')