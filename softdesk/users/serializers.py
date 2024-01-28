"""
This module contains the serializer for the CustomUser model.

The CustomUserSerializer includes validation logic to ensure that users are at least 15 years old.
"""

from datetime import date
from rest_framework import serializers
from dateutil.relativedelta import relativedelta
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for the CustomUser model.

    This serializer includes validation logic to ensure that users are at least 15 years old.
    """
    class Meta:
        """
        Meta class for CustomUserSerializer.

        This class defines the model to be used, the fields to be included in the serialization,
        and any extra arguments.
        """
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password',
        'can_be_contacted', 'can_data_be_shared', 'created_time', 'updated_time']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        """
        Validate the input attributes to ensure the 'date_of_birth' is at least 15 years old.
        
        :param attrs: A dictionary of input attributes
        :return: The validated input attributes
        """
        date_of_birth = attrs.get('date_of_birth', None)
        if date_of_birth and date_of_birth > date.today() - relativedelta(years=15):
            raise serializers.ValidationError("You must be at least 15 years old to register.")
        return attrs
