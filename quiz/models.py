from django.db import models
from users.models import User

class Category(models.Model):
    category = models.CharField(max_length=20, primary_key=True)

    def __repr__(self):
        return self.category

class Quiz(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.FloatField(max_length=5)
    date_created = models.DateTimeField(auto_now_add=True)

