from django.urls import path
from . import views 

urlpatterns = [
    path("", views.my_portfolio, name="home"),           # ← Maps "/"
    path("my-portfolio/", views.my_portfolio, name="my_portfolio"),
]