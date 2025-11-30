from django.contrib.auth.models import User
from django.db import models

class Cryptocurrency (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100), default="My Portfolio"

    def __str__(self):
        return f"{self.user.username}'s Portfolio"

class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE),
    cryptocurrency = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    average_purchase_price = models.DecimalField(max_digits=20, decimal_places=8)

    def __str__(self):
        return f"{self.cryptocurrency.name}: {self.amount}"