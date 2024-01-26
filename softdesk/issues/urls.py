from django.urls import path, include
from .views import IssuesViewSet, CommentsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'issues', IssuesViewSet)
router.register(r'comments', CommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]