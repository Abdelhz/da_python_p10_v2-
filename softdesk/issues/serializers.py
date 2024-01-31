"""
This module contains the serializers for the Issue and Comment models.
"""

from rest_framework import serializers
from .models import Issue, Comment


class IssueSerializer(serializers.ModelSerializer):
    """
    Serializer for the Issue model.

    This serializer includes all fields of the Issue model in the serialization.
    """
    class Meta:
        """
        Meta class for IssueSerializer.

        This class defines the model to be used, the fields to be included in the serialization.
        """
        model = Issue
        fields = ['id', 'project', 'title', 'description', 'tag', 'priority', 'status', 'issue_author',
        'assignee', 'created_time', 'updated_time']

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.

    This serializer includes all fields of the Comment model in the serialization.
    """
    class Meta:
        """
        Meta class for CommentSerializer.

        This class defines the model to be used, the fields to be included in the serialization.
        """
        model = Comment
        fields = ['id', 'description', 'comment_author', 'issue', 'created_time', 'updated_time']
