"""
This module defines the URL routes for this Django app.

It includes routes for the root of the app, as well as a signup route.
The root route uses a router to automatically generate routes for the CustomUserViewSet.
"""


from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'', views.CustomUserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.CustomUserViewSet.as_view({'post': 'create'}), name='signup'),
]