from django.urls import path, include
from rest_framework import routers
from .views import ProjectViewSet, ContributorViewSet

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'contributors', ContributorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]