from django.urls import path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.CustomUserViewSet, basename='users')

urlpatterns = router.urls

'''
urlpatterns = [
    path('', include(router.urls)),
    # path('users/', views.users_list, name='users_list'),
    # add more paths as needed
]
'''