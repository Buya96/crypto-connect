from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Portfolio, Holding, Cryptocurrency
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login


@login_required
def my_portfolio(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)
    holdings = Holding.objects.filter(portfolio=portfolio)
    return render(
        request,
        "portfolio/my_portfolio.html",
        {"portfolio": portfolio, "holdings": holdings},
    )


@login_required
def add_holding(request):
    portfolio, created = Portfolio.objects.get_or_create(user=request.user)

    if request.method == "POST":
        crypto_name = request.POST.get("crypto_name")
        amount = request.POST.get("amount")
        avg_price = request.POST.get("avg_price")

        if not crypto_name or not amount or not avg_price:
            messages.error(request, "All fields are required.")
            return render(
                request, "portfolio/add_holding.html", {"portfolio": portfolio}
            )

        try:
            amount = float(amount)
            avg_price = float(avg_price)
        except ValueError:
            messages.error(
                request, "Amount and average price must be valid numbers."
            )
            return render(
                request, "portfolio/add_holding.html", {"portfolio": portfolio}
            )

        if amount <= 0 or avg_price <= 0:
            messages.error(
                request, "Amount and average price must be greater than zero."
            )
            return render(
                request, "portfolio/add_holding.html", {"portfolio": portfolio}
            )

        crypto_name_clean = crypto_name.strip()
        crypto, created = Cryptocurrency.objects.get_or_create(
            name=crypto_name_clean
        )

        Holding.objects.create(
            portfolio=portfolio,
            cryptocurrency=crypto,
            amount=amount,
            average_purchase_price=avg_price,
        )

        messages.success(
            request, f"Holding for {crypto_name_clean} added successfully."
        )
        return redirect("home")

    return render(request, "portfolio/add_holding.html", {"portfolio": portfolio})


@login_required
def edit_holding(request, holding_id):
    portfolio = get_object_or_404(Portfolio, user=request.user)
    holding = get_object_or_404(Holding, id=holding_id, portfolio=portfolio)

    if request.method == "POST":
        amount = request.POST.get("amount")
        avg_price = request.POST.get("avg_price")

        if not amount or not avg_price:
            messages.error(request, "All fields are required.")
            return render(
                request, "portfolio/edit_holding.html", {"holding": holding}
            )

        try:
            amount = float(amount)
            avg_price = float(avg_price)
        except ValueError:
            messages.error(
                request, "Amount and average price must be valid numbers."
            )
            return render(
                request, "portfolio/edit_holding.html", {"holding": holding}
            )

        if amount <= 0 or avg_price <= 0:
            messages.error(
                request, "Amount and average price must be greater than zero."
            )
            return render(
                request, "portfolio/edit_holding.html", {"holding": holding}
            )

        holding.amount = amount
        holding.average_purchase_price = avg_price
        holding.save()

        messages.success(
            request,
            f"Holding for {holding.cryptocurrency.name} updated successfully.",
        )
        return redirect("home")

    return render(request, "portfolio/edit_holding.html", {"holding": holding})


@login_required
def delete_holding(request, holding_id):
    portfolio = get_object_or_404(Portfolio, user=request.user)
    holding = get_object_or_404(Holding, id=holding_id, portfolio=portfolio)

    if request.method == "POST":
        holding_name = holding.cryptocurrency.name
        holding.delete()
        messages.success(
            request, f"Holding for {holding_name} deleted successfully."
        )
        return redirect("home")

    return render(
        request,
        "portfolio/confirm_delete_holding.html",
        {"holding": holding},
    )
    
def signup(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, "Account created and you are now logged in.")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
