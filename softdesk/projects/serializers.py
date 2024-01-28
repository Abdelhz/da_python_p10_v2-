"""
This module contains the serializers for the Project and Contributor models.
"""

from rest_framework import serializers
from .models import Project, Contributor

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.

    This serializer includes all fields of the Project model in the serialization.
    """
    class Meta:
        """
        Meta class for ProjectSerializer.

        This class defines the model to be used, the fields to be included in the serialization.
        """
        model = Project
        fields = ['title', 'description', 'contributors', 'project_type', 'project_author', 'created_time',
        'updated_time']

class ContributorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Contributor model.

    This serializer includes all fields of the Contributor model in the serialization.
    """
    class Meta:
        """
        Meta class for ContributorSerializer.

        This class defines the model to be used, the fields to be included in the serialization.
        """
        model = Contributor
        fields = ['user', 'project', 'date_given_permission', 'role', 'permission',
        'created_time', 'updated_time']
