from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from classes.serializers import ClassScheduleSerializer
from django.shortcuts import get_object_or_404
from classes.models import Classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions
from django.contrib.auth import get_user_model, authenticate, login, logout
import rest_framework
import rest_framework.decorators
import django
from rest_framework import viewsets
from rest_framework import mixins as drf_mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer
import django
from accounts.permissions import IsCreationOrIsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

""" As a user, I want to see the class schedule of a specific studio on its page. 
Classes must appear in the order of their start time (from now), and the class information must be shown. 
Past or cancelled classes should not be listed.
As a user, I can enrol/drop a class (either one instance or all future occurrences) that has not started yet and has not reached its capacity. 
This can only happen if I have an active subscription.
As a user, I want to see my class schedule and history in chronological order """


class ClassScheduleViewAPI(ListAPIView):
    """ As a user, I want to see the class schedule of a specific studio on its page. 
        Classes must appear in the order of their start time (from now), and the class information must be shown. 
        Past or cancelled classes should not be listed. """
    queryset = Classes.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ClassScheduleSerializer