from django.core.exceptions import ValidationError as DjangoValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_repeat')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        self.validated_data.pop('password_repeat')
        return User.objects.create_user(**self.validated_data)

    def validate_password(self, value):
        # Validate password with django password_validation
        try:
            validate_password(value)
        except DjangoValidationError as error:
            raise serializers.ValidationError(error)
        return value

    def validate(self, data):
        # Additional backend validation on password repeat (firstly should be realized on frontend)
        if data['password_repeat'] != data['password']:
            raise serializers.ValidationError("Passwords don't match")
        return data


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email')

