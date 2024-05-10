from django.contrib.auth import views as auth_views

from django.urls import path
from . import views




urlpatterns = [
    path("", views.LandingPage, name="landing"),

    # Auth
    path("register/", views.RegisterPage, name="register"),
    path("login/", views.LoginPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
]