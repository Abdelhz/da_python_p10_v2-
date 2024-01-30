"""
This module defines the URL routes for this Django app.

It includes routes for the ProjectViewSet and ContributorViewSet view sets.
Nested routes are used to link contributors to projects.
"""

from django.urls import path, include
from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from .views import ProjectViewSet, ContributorViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

projects_router = nested_routers.NestedDefaultRouter(router, r'projects', lookup='project')
projects_router.register(r'contributors', ContributorViewSet, basename='project-contributors')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(projects_router.urls)),
]
