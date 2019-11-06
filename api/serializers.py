from .models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


class UserSerializerWithToken(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            creatingProfileFor=validated_data['creatingProfileFor'],
            firstName=validated_data['firstName'],
            middleName=validated_data['middleName'],
            lastName=validated_data['lastName'],
            gender=validated_data['gender'],
            contactNo=validated_data['contactNo'],
            email=validated_data['email'],
            password=validated_data['password'],
            confirm=validated_data['confirm']
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ('creatingProfileFor', 'firstName', 'middleName', 'lastName', 'gender', 'contactNo', 'email', 'password', 'confirm')
