"""
This module defines the views for the Project and Contributor models in the Django REST Framework app.

It includes a viewset for the Project model, which allows projects to be viewed, created, updated, or deleted.
The viewset includes custom logic for determining the queryset and the permissions for different actions.
"""

from rest_framework import viewsets, permissions
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer
from .permissions import CanViewProject, CanEditProject, CanDeleteProject, IsProjectAuthor, IsProjectAuthorOrContributor

class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Project model.

    This ViewSet allows projects to be viewed, created, updated, or deleted.
    It includes custom logic for determining the queryset and the permissions for different actions.
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        """
        Return the queryset of projects that the current user is a contributor of.
        """
        return Project.objects.filter(contributors=self.request.user)

    def get_permissions(self):
        """
        Return a list of permission classes based on the self.action value.
        """
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]

        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.IsAuthenticated, CanViewProject]

        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [permissions.IsAuthenticated, CanEditProject]

        elif self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, CanDeleteProject]

        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """
        Perform the creation of a new project using the given serializer.
        Args:
            self: The current instance of the class.
            serializer: The serializer instance used for creating the project.
        Returns:
            None
        """
        project = serializer.save(project_author=self.request.user)
        if not Contributor.objects.filter(user=self.request.user, project=project).exists():
            Contributor.objects.create(user=self.request.user,
                                       project=project, role='author', permission='can_delete', can_assign_issues=True)

class ContributorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for the Contributor model.

    This ViewSet allows contributors to be viewed, created, updated, or deleted.
    It includes custom logic for determining the queryset and the permissions for different actions.
    """
    serializer_class = ContributorSerializer

    def get_queryset(self):
        """
        Return the queryset of contributors for a specific project.
        """
        return Contributor.objects.filter(project_id=self.kwargs['project_pk'])

    def create(self, request, *args, **kwargs):
        """
        Override the create method to automatically set the project field.
        """
        request.data['project'] = self.kwargs['project_pk']
        return super().create(request, *args, **kwargs)

    def get_permissions(self):
        """
        Return the Contributor queryset filtered by the project_id from the kwargs.
        """
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.IsAuthenticated, IsProjectAuthorOrContributor]

        elif self.action == 'create':
            permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]

        elif self.action in ['update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated, IsProjectAuthor]

        elif self.action == 'destroy':
            permission_classes = [permissions.IsAuthenticated, IsProjectAuthorOrContributor]

        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]
