from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


@login_required(login_url="login")
def LandingPage(request):
    return render(request, "tracker/dashboard.html")




@login_required(login_url="login")
def Step1Page(request):
    step1 = Step1.objects.filter(student=request.user)
    form = Step1Form()
    if step1:
        context = {"step2": step1[0]}
    else:    
        context = {"step2": step1}
    if request.method == "POST":
        if step1:
            form = Step1Form(request.POST, request.FILES, instance=step1[0])
        else:
            form = Step1Form(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save(commit=False).student = request.user
            form.save()
            return redirect("step2")
        
    return render(request, "tracker/step1.html", context)

@login_required(login_url="login")
def Step2Page(request):
    step2 = Step2.objects.filter(student=request.user)
    form = Step2Form()
    if step2:
        context = {"step2": step2[0]}
    else:    
        context = {"step2": step2}

    if request.method == "POST":
        if step2:
            form = Step2Form(request.POST, instance=step2[0])
        else:
            form = Step2Form(request.POST)
        if form.is_valid():
            form.save(commit=False).student = request.user
            form.save()
            return redirect("step3")
    return render(request, "tracker/step2.html", context)

@login_required(login_url="login")
def Step3Page(request):
    return render(request, "tracker/step3.html")

@login_required(login_url="login")
def Step4Page(request):
    return render(request, "tracker/step4.html")

@login_required(login_url="login")
def Step5Page(request):
    return render(request, "tracker/step5.html")

def RegisterPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account was created for " + form.cleaned_data.get("username"))
            return redirect("login")
        else:
            messages.error(request, "Error creating account, make sure the credentials are correct or it's secure enough.")

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