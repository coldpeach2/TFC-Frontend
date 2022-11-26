from django.views import generic
from rest_framework.generics import CreateAPIView, ListAPIView
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


class ClassScheduleViewAPI(ListAPIView):
    """ As a user, I want to see the class schedule of a specific studio on its page.
        Classes must appear in the order of their start time (from now), and the class information must be shown.
        Past or cancelled classes should not be listed. """
    queryset = Class.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ClassSerializer
