from rest_framework import serializers
from .models import Issue, Comment


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['project', 'title', 'description', 'tag', 'priority', 'status', 'issue_author', 'assignee', 'created_time', 'updated_time']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'comment_author', 'issue', 'created_time', 'updated_time']