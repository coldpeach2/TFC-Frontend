from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import RegistrationSerializer
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework.response import Response
from django.contrib.auth import get_user_model
import rest_framework
import rest_framework.decorators
import django
from rest_framework import viewsets as drf_viewsets
from rest_framework import mixins as drf_mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer
import django

# Create your views here.

class ProfileDetailUpdateView(RetrieveUpdateAPIView):
    serializer_class = RegistrationSerializer
   
    def get_object(self):
        return get_object_or_404(User, id=self.get['id'])


class RegisterUserView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated]


    @rest_framework.decorators.action(methods=["POST"], detail=False)
    def login(self, request, format=None):
        """
        Obtain an authentication token by providing valid credentials.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = rest_framework.authtoken.models.Token.objects.get_or_create(user=user)
        return rest_framework.response.Response({"token": token.key})

    @rest_framework.decorators.action(methods=["POST"], detail=False)
    def logout(self, request, format=None):
        """
        Invalidate the currently owned authentication token.

        **Permissions** :

        * _Authentication_ is required
        """
        django.shortcuts.get_object_or_404(rest_framework.authtoken.models.Token, user=request.user).delete()
        return rest_framework.response.Response(status=rest_framework.status.HTTP_202_ACCEPTED)



""" 
class UpdateUserView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateUserSerializer """
