from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import Profile


class LoginSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginSerializer, cls).get_token(user)
        token['username'] = user.username
        token['password'] = user.password
        return token


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'password', 'email_address', 'mobile']

    def validate_password(self, data):
        if len(data) < 8:
            raise serializers.ValidationError("This password is too short. It must contain at least 8 characters.")

        elif not any(char.isalpha() for char in data):
            raise serializers.ValidationError("It must contain at least one English letter")

        elif not any(char.isdigit() for char in data):
            raise serializers.ValidationError("It must contain at least one digit")

        return data

    def create(self, validated_data):
        return Profile.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'username', 'email_address', 'mobile']