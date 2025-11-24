from django.contrib.auth.models import User
from django.db import models

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    api_id = models.CharField(max_length=50)

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Holding(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    crypto = models.ForeignKey(Cryptocurrency, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    avg_purchase_price = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)

class Transaction(models.Model):
    holding = models.ForeignKey(Holding, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10)  # 'buy' or 'sell'
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    price_per_unit = models.DecimalField(max_digits=20, decimal_places=8)
    transaction_date = models.DateTimeField(auto_now_add=True)
