from rest_framework import serializers
from .models import User



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password','full_name', 'phone_number' ,'date_of_birth']
        

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email','token','username', 'password','full_name', 'phone_number' ,'date_of_birth']
        read_only_fields = ['token','full_name', 'phone_number' ,'date_of_birth']