from django.db import models
from django.contrib.auth.models import User as DJANGOUSER

class User(DJANGOUSER):
    PERMISSIONS = (
        ('G', 'Guest'),
        ('U', 'User'),
        ('M', 'Mod'),
        ('A', 'Admin'),
    )
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=PERMISSIONS)

