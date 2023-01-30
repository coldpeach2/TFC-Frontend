from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from accounts.serializers import RegistrationSerializer, ProfileViewSerializer, LoginSerializer, ProfileUpdateSerializer, ActivateUserSubscriptionSerializer, PaymentHistorySerializer
from django.shortcuts import get_object_or_404
from accounts.models import User, UserSubscription, PaymentHistory
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
from rest_framework.authtoken.models import Token

# Create your views here.
class ProfileView(RetrieveAPIView):
    serializer_class = ProfileViewSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = User.objects.get(email=self.request.user)
        return user


class ProfileUpdateView(UpdateAPIView):
    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

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
    authentication_classes = []

class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []

    def post(self, request):
        serializer = LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        print(token)
        return Response({"token": token.key}, status=status.HTTP_202_ACCEPTED)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)


class ActivateUserSubscriptionView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActivateUserSubscriptionSerializer
    model = UserSubscription

    def perform_create(self, serializer):
        serializer.is_valid(raise_exception=True)
        serializer.save(user = self.request.user)


class UserSubscriptionView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]


class UpdateAccountView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActivateUserSubscriptionSerializer
    queryset = UserSubscription.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj

    def update(self, request, *args, **kwargs):
        data = request.data
        serializer = ActivateUserSubscriptionSerializer(self.get_object(), data=data, partial=True, context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        instance = serializer.instance
        return Response(ActivateUserSubscriptionSerializer(instance=instance).data, status=status.HTTP_200_OK)

class PaymentHistoryView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentHistorySerializer

    def get_queryset(self):
        user = self.request.user
        user_subscription = UserSubscription.objects.get(user=user)
        print(user_subscription.id)
        payments = PaymentHistory.objects.filter(user_id=user_subscription.id)
        return payments
