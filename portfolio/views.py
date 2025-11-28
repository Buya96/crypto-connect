from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Portfolio

# Create your views here.
@login_required
def my_portfolio(request):
    portfolio = Portfolio.objects.get(user=request.user)
    return render(request, "portfolio/my_portfolio.html", {"portfolio": portfolio})
