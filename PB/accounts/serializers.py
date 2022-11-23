from rest_framework import serializers
from accounts.models import User


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
