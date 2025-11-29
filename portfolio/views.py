from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages 
from .models import Portfolio

# Create your views here.
@login_required
def my_portfolio(request):
    try:
        portfolio = Portfolio.objects.get(user=request.user)
    except Portfolio.DoesNotExist:
        messages.error(request, "Portfolio not found.")
        portfolio = None
    return render(request, 'portfolio/my_portfolio.html', {'portfolio': portfolio}) 
