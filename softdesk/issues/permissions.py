from rest_framework import permissions

class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.contributors.filter(id=request.user.id).exists()

class IsIssueAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.issue_author == request.user

class CanAssignIssue(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.contributors.filter(user=request.user, can_assign_issues=True).exists()