from django.urls import path
from . import views 

urlpatterns = [
    path("my-portfolio/",views.my_portfolio, name="my_portfolio"),  
]   
