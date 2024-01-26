from rest_framework import permissions

class CanViewProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.contributors.objects.filter(user=request.user, project=obj, permission__in=['can_view', 'can_edit', 'can_delete']).exists()

class CanEditProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.contributors.objects.filter(user=request.user, project=obj, permission__in=['can_edit', 'can_delete']).exists()

class CanDeleteProject(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.contributors.objects.filter(user=request.user, project=obj, permission='can_delete').exists()

class IsProjectAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.project_author == request.user

class IsProjectAuthorOrContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.project.project_author == request.user or obj.user == request.user