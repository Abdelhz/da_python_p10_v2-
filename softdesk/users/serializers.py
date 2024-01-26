from rest_framework import serializers
from .models import CustomUser
from dateutil.relativedelta import relativedelta
from datetime import date


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'date_of_birth', 'email', 'password', 'can_be_contacted', 'can_data_be_shared', 'created_time', 'updated_time']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        date_of_birth = data.get('date_of_birth', None)
        if date_of_birth and date_of_birth > date.today() - relativedelta(years=15):
            raise serializers.ValidationError("You must be at least 15 years old to register.")
        return data