from django.db import models
from django.contrib.auth.models import User
from main.models import Quiz

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics')
    quizes = models.ManyToManyField(Quiz)
    # comments = models.OneToOneField(Comment)   #


    def __str__(self):
        return f'{self.user.username} Profile'

