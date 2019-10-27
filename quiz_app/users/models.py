from django.db import models
from django.contrib.auth.models import User as DJANGOUSER

class User(DJANGOUSER):
    PERMISSIONS = (
        ('G', 'Guest'),
        ('U', 'User'),
        ('M', 'Mod'),
        ('A', 'Admin'),
    )
    permissions = models.CharField(max_length=1, choices=PERMISSIONS)

