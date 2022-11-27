from django.shortcuts import render
from django.views import generic
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Studio, Amenity, Classes
from accounts.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import StudioCreateSerializer, AmenitySerializer, ClassScheduleSerializer, StudiosForUserSerializer, UserLocationSerializer
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
# Create your views here.



class ViewStudioView(generic.DetailView):
    permission_classes = [IsAuthenticated]
    def get_object(self, **kwargs):
        studio_id = self.kwargs.get("studio_id")
        return get_object_or_404(Studio, id=studio_id)

        

class StudioClassScheduleView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassScheduleSerializer

    def get_queryset(self):
        studio_id = self.kwargs.get("id")
        studio = get_object_or_404(Studio, studios_classes=studio_id)
        queryset = Classes.objects.filter(studio=studio).order_by('times')
        print(queryset.values())
        return queryset.values()

