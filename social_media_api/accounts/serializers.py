# accounts/serializers.py
from rest_framework import serializers
from rest_framework import serializers  # Add this import
from django.contrib.auth import get_user_model  # Add this import
from rest_framework.authtoken.models import Token  # Add this import

from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    bio = serializers.CharField(max_length=500, allow_blank=True)
    profile_picture = serializers.ImageField(max_length=100, allow_empty_file=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)  # This function should work now
        Token.objects.create(user=user)  # This function should work now
        return user