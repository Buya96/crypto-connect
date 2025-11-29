from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages 
from .models import Portfolio

# Create your views here.
@login_required
def my_portfolio(request):
    portfolio = portfolio.objects.filter(user=request.user)
    holdings = holdings.objects.filter(user=request.user)
    
    return render(request, "portfolio/my_portfolio.html", {
        "portfolio": portfolio,
        "holdings": holdings, 
    })
