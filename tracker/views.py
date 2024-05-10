from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

def LandingPage(request):
    return render(request, "tracker/base.html")


def RegisterPage(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created for " + form.cleaned_data.get("username"))
            return redirect("login")

    context = {"form": form}
    return render(request, "tracker/register.html", context)


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("landing")
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, "tracker/login.html")

def LogoutPage(request):
    logout(request)
    return redirect("login")