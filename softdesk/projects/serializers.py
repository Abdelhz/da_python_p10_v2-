from rest_framework import serializers
from .models import Project, Contributor
from dateutil.relativedelta import relativedelta


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'description', 'contributors', 'project_type', 'project_author', 'created_time', 'updated_time']

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ['user', 'project', 'date_given_permission', 'role', 'permission', 'created_time', 'updated_time']