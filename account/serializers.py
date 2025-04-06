from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response

class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username','email', 'password']
        extra_kwargs = {
            'password': {'required': True}
        }
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(required=True)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email is None or password is None:
            raise serializers.ValidationError('An email and password are required to log in.')

        User = get_user_model()
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid email or password.')

        if not user.check_password(password):
            raise serializers.ValidationError('Invalid email or password.')

        attrs['user'] = user 
        return attrs

    def to_representation(self, instance):
        user = instance['user']  
        return {
            'access': str(self.get_token(user)),  # Access token
            'refresh': str(self.get_token(user)),  # Refresh token
        }