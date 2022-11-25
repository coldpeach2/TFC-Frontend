from django.views import generic
from rest_framework.generics import CreateAPIView
from .models import Class
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import ClassSerializer
from django.shortcuts import get_object_or_404


class CreateStudioView(CreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def perform_create(self, serializer):
        gym_class = get_object_or_404(Class, id=self.request.data.get('id'))
        return serializer.save(gym_class=gym_class)

