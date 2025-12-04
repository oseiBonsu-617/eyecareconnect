from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('clinician', 'Clinician'),
        ('assistant', 'Assistant')
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='clinician')

    def __str__(self):
        return f"{self.username} ({self.role})"