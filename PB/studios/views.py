from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from rest_framework.generics import CreateAPIView
from .models import Studio, Amenity
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from .serializers import StudioSerializer, AmenitySerializer
from django.shortcuts import get_object_or_404
# Create your views here.


class CreateStudioView(CreateAPIView):
    permission_classes = [IsAdminUser]

    queryset = Studio.objects.all()
    serializer_class = StudioSerializer

    def perform_create(self, serializer):
        studio = get_object_or_404(Studio, id=self.request.data.get('id'))
        return serializer.save(studio=studio)


class StudioView(generic.DetailView):
    permission_classes = [IsAdminUser]

    def get_object(self, **kwargs):
        studio_id = self.kwargs.get("id")
        return get_object_or_404(Studio, id=studio_id)


class EditStudioView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Studio.objects.all()
    serializer_class = StudioSerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(EditStudioView(instance=instance).request.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': serializer.errors})


class UpdateAmenitiesView(generics.UpdateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Amenity.objects.all()
    serializer_class = AmenitySerializer
    lookup_field = 'pk'

    def update(self, request, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(UpdateAmenitiesView(instance=instance).request.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': serializer.errors})


longitude = -80
latitude = 25
user_location = Point(longitude, latitude, srid=4326)


class ViewClosestStudiosView(generic.ListView):
    model = Studio
    context_object_name = 'studios'
    queryset = Studio.objects.annotate(distance=Distance('geolocation', user_location)).order_by('distance')[0:6]


class ViewStudioView(generic.DetailView):
    def get_object(self, **kwargs):
        studio_id = self.kwargs.get("studio_id")
        return get_object_or_404(Studio, id=studio_id)
