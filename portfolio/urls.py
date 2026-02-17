from django.urls import path
from . import views 

urlpatterns = [
    path("", views.my_portfolio, name="home"),           # ← Maps "/"
    path("my-portfolio/", views.my_portfolio, name="my_portfolio"),
    path("add-holding/", views.add_holding, name="add_holding"),
    path("edit-holding/<int:holding_id>/", views.edit_holding, name="edit_holding"),
    path("delete-holding/<int:holding_id>/", views.delete_holding, name="delete_holding"),
    path("signup/", views.signup, name="signup"),
]

