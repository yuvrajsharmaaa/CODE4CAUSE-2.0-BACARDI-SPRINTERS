from rest_framework import serializers
from .models import PersonalityTest

class PersonalityTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalityTest
        fields = '__all__'
