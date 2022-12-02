from rest_framework import serializers
from .models import Studio, Amenity, Classes
import re
import json


# class StudioCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['name', 'address', 'lon', 'lat', 'postal_code', 'phone_num', 'images']
#
#     def validate(self, data: dict) -> dict:
#         postal_code_regex = r"/^[A-Za-z]\d[A-Za-z][ -]?\d[A-Za-z]\d$/"
#         phone_num_regex = r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"
#
#         if not re.match(phone_num_regex, data['phone_num']):
#             raise serializers.ValidationError({'phone_num': 'Please enter a valid phone number.'})
#
#         if not re.match(postal_code_regex, data['postal_code']):
#             raise serializers.ValidationError({'postal_code': 'Please enter a valid postal code.'})
#
#         return data
#
#     def save(self):
#         studio = Studio(name=self.validated_data['name'], address=self.validated_data['address'],
#                         lon=self.validated_data['lon]'], lat=self.validated_data['lat'],
#                         postal_code=self.validated_data['postal_code'], phone_num=self.validated_data['phone_num'],
#                         images=self.validated_data['images'])
#
#         studio.save()
#         return studio
#
#
# class AmenitySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Amenity
#         fields = ['type', 'quantity', 'studio']
#
#     def validate(self, data: dict) -> dict:
#         if data['quantity'] < 0:
#             raise serializers.ValidationError({'quantity': 'Must enter a non-negative number.'})
#         return data
#
#     def save(self):
#         amenity = Amenity(type=self.validated_data['type'], quantity=self.validated_data['quantity'],
#                           studio=self.validated_data['studio'])
#
#         amenity.save()
#         return amenity

# class UserLocationSerializer(serializers.ModelSerializer):
#     #user_loc = serializers.SerializerMethodField()
#     class Meta:
#         model = User
#         fields = ('email', 'lon', 'lat', 'user_loc')
#
#     def get_user_loc(self, obj):
#         point = obj.user_loc()
#         #print(point)
#         return point


class StudiosForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ('name', 'address', 'postal_code', 'phone_num', 'images', 'lon', 'lat')


class ClassScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('id', 'name', 'description', 'coach', 'keywords', 'capacity', 'start_time', 'end_time')


class StudioSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class ClassSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class ClassEnrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('id', 'name', 'start_time', 'enrolled')


