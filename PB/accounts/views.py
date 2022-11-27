from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from accounts.serializers import RegistrationSerializer, ProfileViewSerializer, LoginSerializer, ProfileUpdateSerializer
from django.shortcuts import get_object_or_404
from accounts.models import User
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
""" class ProfileView(viewsets.ModelViewSet):
    def retrieve(self):
        user = User.objects.get(email=self.request.user)
        return user


 """
class ProfileView(RetrieveAPIView):
    serializer_class = ProfileViewSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = User.objects.get(email=self.request.user)
        return user


class ProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = ProfileViewSerializer(self.get_object(), data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance = serializer.instance
        return Response(ProfileViewSerializer(instance=instance).data, status=status.HTTP_200_OK)

class RegisterUserView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)
    #authentication_classes = (TokenAuthentication,)
    #permission_classes = (IsCreationOrIsAuthenticated,)
    #Token.objects.create(user=user)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_202_ACCEPTED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    # def get(self, request):
    #     user = self.request.user
        
    #     get_object_or_404(Token, user=self.request.user).delete()
    #     return Response(status=status.HTTP_202_ACCEPTED) 
    
    # def post(self, request):
    #     return self.logout(request)

    def get(self, request, format=None):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)





""" As a user, I can enrol/drop a class (either one instance or all future occurrences) 
that has not started yet and has not reached its capacity. 
This can only happen if I have an active subscription.
As a user, I want to see my class schedule and history in chronological order """ 