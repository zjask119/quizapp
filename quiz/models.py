from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.FloatField(max_length=5, default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return self.name

