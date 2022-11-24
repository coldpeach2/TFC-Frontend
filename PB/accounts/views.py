from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from accounts.serializers import RegistrationSerializer, ProfileViewSerializer, LoginSerializer
from django.shortcuts import get_object_or_404
from accounts.models import User
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status, permissions
from django.contrib.auth import get_user_model, authenticate, login, logout
import rest_framework
import rest_framework.decorators
import django
from rest_framework import viewsets as drf_viewsets
from rest_framework import mixins as drf_mixins
from rest_framework.authtoken.serializers import AuthTokenSerializer
import django
from accounts.permissions import IsCreationOrIsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

class ProfileView(RetrieveUpdateAPIView):
    serializer_class = ProfileViewSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        user = get_object_or_404(User, email=self.request.user)
        serializer = ProfileViewSerializer(self.get_object(), data=data, partial=True)
        content ={
            "first_name":str(user.first_name),
            "last_name":str(user.last_name),
            "email":str(user.email),
            "avatar":user.avatar,
            "phone_num": str(user.phone_num)
        }
        return Response(data=content, status=status.HTTP_202_ACCEPTED)
   
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
    #authentication_classes = (TokenAuthentication,)
    permission_classes = (IsCreationOrIsAuthenticated,)
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



"""  def post(self, request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user=authenticate(email=email, password=password)
        if user is not None:
            response={
                "message":"Login Successful",
                "token":user.auth_token.key
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message":"Invalid email or password"})
                def get(self, request):
        user = request.user
        content ={
            "user":str(user),
            "auth":str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)

 """

"""     @rest_framework.decorators.action(methods=["POST"], detail=False)
    def login(self, request, format=None):
     
       # Obtain an authentication token by providing valid credentials.
       
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = rest_framework.authtoken.models.Token.objects.get_or_create(user=user)
        return rest_framework.response.Response({"token": token.key})

    @rest_framework.decorators.action(methods=["POST"], detail=False)
    def logout(self, request, format=None):

       #Invalidate the currently owned authentication token.

        #**Permissions** :

       # * _Authentication_ is required
     
        django.shortcuts.get_object_or_404(rest_framework.authtoken.models.Token, user=request.user).delete()
        return rest_framework.response.Response(status=rest_framework.status.HTTP_202_ACCEPTED) 



""" 
