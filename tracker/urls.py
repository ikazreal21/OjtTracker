from django.contrib.auth import views as auth_views

from django.urls import path
from . import views




urlpatterns = [
    path("", views.LandingPage, name="landing"),

    path("step1/", views.Step1Page, name="step1"),
    path("step2/", views.Step2Page, name="step2"),
    path("step3/", views.Step3Page, name="step3"),
    path("step4/", views.Step4Page, name="step4"),
    path("step5/", views.Step5Page, name="step5"),

    # Auth
    path("register/", views.RegisterPage, name="register"),
    path("login/", views.LoginPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
]