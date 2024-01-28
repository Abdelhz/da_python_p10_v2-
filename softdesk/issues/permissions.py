"""
This module defines custom permissions for this Django REST Framework app.

It includes permissions for checking if a user is a contributor to a project, if a user is the author of an issue,
and if a user can assign issues.
"""

from rest_framework import permissions

class IsContributor(permissions.BasePermission):
    """
    Permission class to check if a user is a contributor to a project.
    
    Args:
        self: The object itself.
        request: The request being made.
        view: The view that is being accessed.
        obj: The object being accessed.
    
    Returns:
        bool: True if the request user has permission, False otherwise.
    """
    def has_object_permission(self, request, view, obj):
        return obj.project.contributors.filter(id=request.user.id).exists()

class IsIssueAuthor(permissions.BasePermission):
    """
    Permission class to check if a user is the author of an issue.
        
    Parameters:
        self (object): The current instance of the class.
        request (object): The request being made by the user.
        view (object): The view being accessed by the user.
        obj (object): The object on which the action is to be performed.
        
    Returns:
        bool: True if the requesting user has permission, False otherwise.
    """
    def has_object_permission(self, request, view, obj):
        return obj.issue_author == request.user

class CanAssignIssue(permissions.BasePermission):
    """
    Permission class to check if a user has the permission to assign issues.
    
    Args:
        self: The object itself.
        request: The request made.
        view: The view used.
        obj: The object to be checked for permission.
    Returns:
        bool: True if the user has permission, False otherwise.
    """
    def has_object_permission(self, request, view, obj):
        return obj.project.contributors.filter(user=request.user, can_assign_issues=True).exists()
