from django.shortcuts import render
from django.views import generic
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from .models import Studio, Amenity, Classes
from accounts.models import User, UserSubscription
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import ClassScheduleSerializer, StudiosForUserSerializer, StudioSearchSerializer, \
    ClassSearchSerializer
from django.shortcuts import get_object_or_404
from django.contrib.gis.geos import Point
from rest_framework import filters
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
        queryset = Classes.objects.filter(studio=studio).order_by('times')
        #print(queryset.values())
        return queryset.values()


class UserStudioSearch(generics.ListCreateAPIView):
    """As a user, I want to search/filter through the listed studios (mentioned earlier). Search/filter includes
    stdio name, amenities, class names, and coaches that hold classes in those studios."""

    permission_classes = [IsAuthenticated]

    search_fields = ['name', 'classes__name', 'classes__coach', 'amenity__type']
    filter_backends = (filters.SearchFilter,)
    queryset = Studio.objects.all()
    serializer_class = StudioSearchSerializer


class UserClassSearch(generics.ListCreateAPIView):
    """As a user, I want to search/filter a studio's class schedule.
    The search/filter can be based on the class name, coach name, date, and time range."""

    permission_classes = [IsAuthenticated]

    search_fields = ['name', 'coach', 'start_date', 'start_time', 'end_time']
    filter_backends = (filters.SearchFilter,)
    queryset = Classes.objects.all()
    serializer_class = ClassSearchSerializer


class EnrolUserView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    # search_fields = ['name', 'coach', 'start_date', 'start_time', 'end_time']
    # filter_backends = (filters.SearchFilter,)
    # serializer_class = ClassSearchSerializer

    def get_queryset(self):
        studio_id = self.kwargs.get("id")
        studio = get_object_or_404(Studio, studios_classes=studio_id)
        queryset = Classes.objects.filter(studio=studio).order_by('times')
        return queryset

    def get_object(self):
        name = ... ###please help
        class_obj = Classes.objects.get(name=name)
        user = self.request.user
        subscription = UserSubscription.objects.filter(user=user)
        is_active = getattr(subscription, 'active')

        if class_obj.enrolled + 1 <= class_obj.capacity:
            if is_active:
                class_obj.enrolled.add(user)
                return "Enrolled"
            else:
                return "Must be subscribed"
        else:
            return "Class full"


class UserScheduleView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassScheduleSerializer

    def get_queryset(self):
        user = self.request.user
        user_classes = []

        for class_obj in Classes.objects.all():
            if class_obj.enrolled.filter(user) is not None:
                user_classes.append(class_obj)

        return user_classes



