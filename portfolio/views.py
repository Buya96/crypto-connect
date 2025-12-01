from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages 
from .models import Portfolio, Holding, Cryptocurrency 

# Create your views here.
@login_required
def my_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    
    holdings = Holding.objects.none()

    return render(request, "portfolio/my_portfolio.html", {
        "portfolio": portfolio,
        "holdings": holdings,
    })
    

@login_required
def add_holding(request):
    portfolio  = Portfolio.objects.get(user=request.user)

    if request.method == "POST":
        crypto_name = request.POST.get("crypto_name")
        amount = request.POST.get("amount")
        avg_price = request.POST.get("avg_price")


        # Validate inputs
        if crypto_name and amount and avg_price:
            # Get or create the cryptocurrency
            crypto, created = Cryptocurrency.objects.get_or_create(name=crypto_name)

            # Create the holding
            holding = Holding.objects.create(
                portfolio=portfolio,
                cryptocurrency=crypto,
                amount=float(amount),
                average_price=float(avg_price)
            )
            messages.success(request, f"Holding for {crypto_name} added successfully.")
            return redirect('home')
        else:
            messages.error(request, "All fields are required.")

    return render(request, "portfolio/add_holding.html", {"portfolio": portfolio}) 

@login_required
def edit_holding(request, holding_id):
    portfolio  = Portfolio.objects.get(user=request.user)
    holding = Holding.objects.get(id=holding_id, portfolio=portfolio)

    if request.method == "POST":
        holding.amount = float(request.POST.get("amount"))
        holding.average_price = float(request.POST.get("avg_price"))
        holding.save()
        messages.success(request, f"Holding for {holding.cryptocurrency.name} updated successfully.")
        return redirect('home')
    
    return render(request, "portfolio/edit_holding.html", {"holding": holding})

@login_required
def delete_holding(request, holding_id):
    portfolio = Portfolio.objects.get(user=request.user)
    holding = Holding.objects.get(id=holding_id, portfolio=portfolio)
    holding.delete()
    messages.success(request, f"Holding for {holding.cryptocurrency.name} deleted successfully.")
    return redirect('home') 
    


