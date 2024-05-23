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

    # Profile Page
    path("profile/", views.ProfilePage, name="profile"),
    
    # Company
    path("company/", views.CompanyPage, name="company"),
    path("company-profile/", views.CompanyProfilePage, name="company-profile"),
    path("list-interns/", views.ListInternsPage, name="list-interns"),
    path("view-intern/<str:pk>", views.ViewInternPage, name="view-intern"),
    path("time-log/", views.TimeLogPage, name="time-log"),


    # Register Page 
    path("personal-info/", views.RegisterPage2, name="personal-info"),
    path("student-info/", views.RegisterPage3, name="student-info"),
    path("job-info/", views.RegisterPage4, name="job-info"),
    path("pending/", views.PendingPage, name="pending"),

    # Auth
    path("register/", views.RegisterPage, name="register"),
    path("login/", views.LoginPage, name="login"),
    path("logout/", views.LogoutPage, name="logout"),
]