from django.shortcuts import render
from django.views import generic
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Studio, Amenity, Classes
from accounts.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import ClassScheduleSerializer, StudiosForUserSerializer
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
# Create your views here.


class StudiosForUserView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudiosForUserSerializer

    def get_queryset(self):
        lon = self.request.user.lon
        lat = self.request.user.lat

        studio_key = {}
        point_set = []

        for studio in Studio.objects.all():
            point = Point(studio.lon, studio.lat, srid=4326)
            studio_key[studio] = point
            point_set.append(point)

        point_set.sort(key=lambda p: (p.x - lon)**2 + (p.y - lat)**2)

        closest_studios = []

        for loc in point_set:
            for key in studio_key:
                if loc == studio_key[key]:
                    closest_studios.append(key)

        return closest_studios


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
        queryset = Classes.objects.filter(studio=studio)
        print(queryset.values())
        return queryset.values()

