from .models import Class
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name', 'description', 'coach', 'key_words', 'capacity', 'start_date', 'end_date', 'start_time',
                  'end_time', 'frequency', 'studio', 'enrolled', 'cancelled_date']

    def validate(self, data: dict) -> dict:
        if data['capacity'] < 0:
            raise serializers.ValidationError({'capacity': 'Must enter a non-negative number.'})

        return data

    def save(self):
        gym_class = Class(name=self.validated_data['name'], description=self.validated_data['description'],
                          coach=self.validated_data['coach'], key_words=self.validated_data['key_words'],
                          capacity=self.validated_data['capacity'], start_date=self.validated_data['start_date'],
                          end_date=self.validated_data['end_date'], start_time=self.validated_data['start_time'],
                          end_time=self.validated_data['end_time'], frequency=self.validated_data['frequency'],
                          studio=self.validated_data['studio'], enrolled=self.validated_data['enrolled'],
                          cancelled_date=self.validated_data['cancelled_date'])

        gym_class.save()
        return gym_class
