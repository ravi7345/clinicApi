from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        doctor = Doctor(username=validated_data['username'])
        doctor.set_password(validated_data['password'])
        doctor.save()
        return doctor
