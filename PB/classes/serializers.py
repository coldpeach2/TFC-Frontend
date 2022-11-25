from .models import Class
from rest_framework import serializers


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['name', 'description', 'coach', 'key_words', 'capacity', 'times', 'end_recursion', 'recurring',
                  'studio']

    def validate(self, data: dict) -> dict:
        if data['capacity'] < 0:
            raise serializers.ValidationError({'capacity': 'Must enter a non-negative number.'})
        if data['recurring'] == '':
            raise serializers.ValidationError({'recurring': 'This field is required'})

        return data

    def save(self):
        gym_class = Class(name=self.validated_data['name'], description=self.validated_data['description'],
                          coach=self.validated_data['coach'], key_words=self.validated_data['key_words'],
                          capacity=self.validated_data['capacity'], times=self.validated_data['times'],
                          end_recursion=self.validated_data['end_recursion'],
                          recurring=self.validated_data['recurring'], studio=self.validated_data['studio'])

        gym_class.save()
        return gym_class