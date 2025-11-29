from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages 
from .models import Portfolio, Holding

# Create your views here.
@login_required
def my_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    holdings = Holding.objects.none()  # Empty queryset for now

    
    return render(request, "portfolio/my_portfolio.html", {
        "portfolio": portfolio,
        "holdings": holdings, 
    })
