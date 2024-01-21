from rest_framework import serializers
from .models import CustomUser, Project, Contributor, Issue, Comment
from dateutil.relativedelta import relativedelta

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        date_of_birth = data.get('date_of_birth', None)
        if date_of_birth and date_of_birth > date.today() - relativedelta(years=15):
            raise serializers.ValidationError("You must be at least 15 years old to register.")
        return data

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'contributors', 'type', 'author']

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'project', 'date_given_permission', 'role', 'permission']

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ['title', 'description', 'tag', 'priority', 'project', 'author', 'assignee', 'created_time', 'status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['description', 'author', 'issue', 'created_time']