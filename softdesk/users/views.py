"""
This module defines the views for the Django REST Framework app.

It includes a viewset for the CustomUser model, which allows users to be viewed or edited.
The viewset includes custom logic for creating a user and for determining the permissions
for different actions.
"""

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserSerializer
from .permissions import IsOwnerOrReadOnly

class CustomUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = CustomUserSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new user based on the request data.
        Args:
            request: The request object containing the data for user creation.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
        Returns:
            Response: The response containing the serialized user data and the HTTP status code.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_permissions(self):
        """
        Return the list of permission classes based on the action.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
