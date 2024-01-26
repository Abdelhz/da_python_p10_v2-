from rest_framework import viewsets, permissions
from .models import Project, Contributor
from .serializers import ProjectSerializer, ContributorSerializer
from .permissions import CanViewProject, CanEditProject, CanDeleteProject, IsProjectAuthor, IsProjectAuthorOrContributor

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
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
        project = serializer.save(project_author=self.request.user)
        if not Contributor.objects.filter(user=self.request.user, project=project).exists():
            Contributor.objects.create(user=self.request.user, project=project, role='author', permission='can_delete', can_assign_issues=True)

class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer

    def get_permissions(self):
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