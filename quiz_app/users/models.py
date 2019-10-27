from django.db import models
from django.contrib.auth.models import User as DJANGOUSER
from quiz.models import quiz


class User(DJANGOUSER):
    PERMISSIONS = (
        ('G', 'Guest'),
        ('U', 'User'),
        ('M', 'Mod'),
        ('A', 'Admin'),
    )
    name = models.CharField(max_length=30)
    shirt_size = models.CharField(max_length=1, choices=PERMISSIONS)

class Profile(models.Model):
    avatar = models.ImageField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    join_date = models.ForeignKey(User, on_delete=models.CASCADE)
    user_quizies = models.ForeignKey(default=False)
    user_comments = models.ForeignKey(default=False)
    hyperlink_settings = models.CharField(default=False)
    solved_quizies = models.BooleanField(default=False)
