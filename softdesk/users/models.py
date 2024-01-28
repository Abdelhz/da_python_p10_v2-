"""
This module defines the data models for this Django app.

It includes a CustomUser model that extends the built-in AbstractUser model.
The CustomUser model includes additional fields like date_of_birth, can_be_contacted,
can_data_be_shared, created_time, and updated_time.
"""

from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    CustomUser model that extends the built-in AbstractUser model.

    This model includes additional fields like date_of_birth, can_be_contacted,
    can_data_be_shared, created_time, and updated_time.
    """
    date_of_birth = models.DateField(null=True, blank=True)
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
