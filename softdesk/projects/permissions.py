"""
This module defines custom permissions for this Django REST Framework app.

It includes permissions for viewing, editing, and deleting a project, as well as
permissions for checking if a user is the author of a project or a contributor to a project.
"""

from rest_framework import permissions

class CanViewProject(permissions.BasePermission):
    """
    Permission class to check if a user has permission to view a project.
    
    :param request: The request object
    :param view: The view object
    :param project: The project object
    :return: Boolean indicating if the user has permission
    """
    def has_object_permission(self, request, view, project):
        return project.contributor_set.filter(user=request.user,
                                           permission__in=['can_view', 'can_edit', 'can_delete']).exists()

class CanEditProject(permissions.BasePermission):
    """
    Permission class to check if a user has permission to edit a project.
    
    Parameters:
        self (object): The current instance of the class.
        request (object): The request object.
        view (object): The view object.
        project (object): The project object to check permissions for.
    
    Returns:
        bool: True if the user has permission, False otherwise.
    """
    def has_object_permission(self, request, view, project):
        return project.contributor_set.filter(user=request.user, permission__in=['can_edit', 'can_delete']).exists()

class CanDeleteProject(permissions.BasePermission):
    """
    Permission class to check if a user has permission to delete a project.
    
    Parameters:
        self (object): The current instance of the class.
        request (object): The request object.
        view (object): The view object.
        project (object): The project object.
    
    Returns:
        bool: True if the user has permission to delete the project, False otherwise.
    """
    def has_object_permission(self, request, view, project):
        return project.contributor_set.filter(user=request.user, permission='can_delete').exists()

class IsProjectAuthor(permissions.BasePermission):
    """
    Permission class to check if a user is the author of a project.
    
    :param request: The request object
    :param view: The view object
    :param contributor: The contributor to check permission for
    :return: True if the contributor has permission, False otherwise
    """
    def has_object_permission(self, request, view, contributor):
        return contributor.project.project_author == request.user

class IsProjectAuthorOrContributor(permissions.BasePermission):
    """
    Permission class to check if a user is the author of a project or a contributor to a project.
    
    :param request: the request object
    :param view: the view object
    :param contributor: the contributor object
    :return: True if the contributor has permission, False otherwise
    """
    def has_object_permission(self, request, view, contributor):
        return contributor.project.project_author == request.user or contributor.user == request.user
