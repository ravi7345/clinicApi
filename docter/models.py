from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class Doctor(AbstractUser):
    
    # Add related_name to groups field
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='doctor_set',  # Add related_name argument
        related_query_name='doctor'
    )

    # Add related_name to user_permissions field
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='doctor_set',  # Add related_name argument
        related_query_name='doctor'
    )