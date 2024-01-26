from rest_framework.decorators import action
from rest_framework import viewsets, permissions
#from projects.models import Project, Contributor
from users.models import CustomUser
from .models import Issue, Comment
from .serializers import IssueSerializer, CommentSerializer
from .permissions import CanAssignIssue, IsIssueAuthor, IsContributor

class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer

@action(detail=True, methods=['post'])
def assign(self, request, pk=None):
    issue = self.get_object()  # get the issue
    user_id = request.data.get('user_id')  # get the user_id from the request data

    # check if the user is a contributor to the project
    if not issue.project.contributors.filter(id=user_id).exists():
        return Response({'error': 'User is not a contributor to the project'}, status=status.HTTP_400_BAD_REQUEST)

    # get the user
    user = CustomUser.objects.get(id=user_id)

    # assign the issue to the user
    issue.assignee = user
    issue.save()

    return Response({'status': 'issue assigned'})
    
    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated, IsContributor]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [permissions.IsAuthenticated, IsIssueAuthor]
        elif self.action == 'assign':
            permission_classes = [permissions.IsAuthenticated, CanAssignIssue]
        else:
            permission_classes = [permissions.IsAuthenticated, IsContributor]
        return [permission() for permission in permission_classes]
    

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        pass
