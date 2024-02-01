"""
This module defines the data models for this Django app.

It includes a CustomUser model that extends the built-in AbstractUser model,
and a Project model that represents a project that users can contribute to.
"""

from django.db import models
from users.models import CustomUser

class Project(models.Model):
    """
    Project model that represents a project that users can contribute to.

    This model includes fields like title, description, contributors, project_type,
    project_author, created_time, and updated_time.
    """
    PROJECT_TYPE_CHOICES = [
        ('back-end', 'Back-end'),
        ('front-end', 'Front-end'),
        ('android', 'Android'),
        ('ios', 'IOS'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    contributors = models.ManyToManyField(CustomUser, through='Contributor', related_name='contributed_projects')
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPE_CHOICES)
    project_author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_projects')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class Contributor(models.Model):
    """
    Contributor model that represents a user's contribution to a project.

    This model includes fields like user, project, and permission.
    """
    PROJECT_PERMISSION_CHOICES = [
        ('can_view', 'Can_View'),
        ('can_edit', 'Can_Edit'),
        ('can_delete', 'Can_Delete'),
        # add more permissions as needed
        # permissions needs to be well defined later on
    ]
    role_choices = [
        ('author', 'Author'),
        ('contributor', 'Contributor'),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=role_choices, default='contributor')
    permission = models.CharField(max_length=20, choices=PROJECT_PERMISSION_CHOICES, default='can_view')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
