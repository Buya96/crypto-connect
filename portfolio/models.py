from django.contrib.auth.models import User
from django.db import models

class Cryptocurrency (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Portfolio"