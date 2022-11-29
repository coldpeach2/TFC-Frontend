from rest_framework import serializers
from accounts.models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'avatar', 'phone_num', 'password', 'password2']
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}},
    }

    def validate(self, data: dict) -> dict:
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Passwords must match.'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email is already in use.'})
        return data

    def save(self, **kwargs):
        user = User(first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'],
                    email=self.validated_data['email'], phone_num=self.validated_data['phone_num'], avatar=self.validated_data['avatar'])
        user.set_password(self.validated_data['password'])
        user.save()
        return user

class ProfileViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'phone_num')


class ProfileUpdateSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('first_name', 'last_name', 'email', 'avatar', 'phone_num')
            
        def update(self, instance, validated_data):
            for key, value in validated_data.items():
                if value:
                    setattr(instance, key, value)
            instance.save()
            return instance

class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(label="password", style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        # Take username and password from request
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if not user:
                raise serializers.ValidationError("Invalid email or password", code='authorization')
        else:
            raise serializers.ValidationError("Email and password are required", code='authorization')
        # We have a valid user, put it in the serializer's validated_data.
        # It will be used in the view.
        attrs['user'] = user
        return attrs


class ActivateUserSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    