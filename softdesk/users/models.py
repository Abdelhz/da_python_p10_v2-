from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)
    #email = models.EmailField()
    #password = models.CharField(max_length=128)
    date_of_birth = models.DateField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True) 