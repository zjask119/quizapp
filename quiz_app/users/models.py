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

# class Profile(models.Model):
#     avatar = models.ImageField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_quizies = models.ForeignKey(default=False)
    # user_comments = models.ForeignKey(default=False)

