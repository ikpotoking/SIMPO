

from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name','middle_name', 'last_name', 'email', 'phone_number','gender', 'profile_picture', 'password']
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            gender=validated_data['gender'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return User.objects.create(**validated_data)

