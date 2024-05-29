from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .utils import *


@login_required(login_url="login")
def LandingPage(request):
    if request.user.student.is_first_time:
        return redirect("personal-info")
    elif request.user.student.is_approve:
        return render(request, "tracker/dashboard.html")
    else:
        return redirect("pending")



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

@login_required(login_url="login")
def ProfilePage(request):
    details = Student.objects.get(user=request.user)
    context = {"details": details}
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=details)
        if form.is_valid():
            form.save(commit=False).user = request.user
            form.save(commit=False).is_first_time = False
            form.save(commit=False).is_approve = True
            form.save()
            return redirect("profile")
    return render(request, "tracker/profile.html", context)


# Company Views

@login_required(login_url="login")
def CompanyPage(request):
    details = Company.objects.filter(user=request.user)
    if not details:
        Company.objects.create(user=request.user)
    return render(request, "tracker/company/dashboard.html")

@login_required(login_url="login")
def TimeLogPage(request):
    interns = Student.objects.filter(is_approve=True, company_name=request.user.company.name)
    context = {"interns": interns}
    return render(request, "tracker/company/time_log.html", context)

@login_required(login_url="login")
def ListInternsPage(request):
    interns = Student.objects.filter(is_approve=True, company_name=request.user.company.name)
    context = {"interns": interns}
    return render(request, "tracker/company/list_of_intern.html", context)

@login_required(login_url="login")
def ViewInternPage(request, pk):
    details = Student.objects.get(id=pk)
    context = {"details": details}
    return render(request, "tracker/company/view_intern.html", context)

@login_required(login_url="login")
def CompanyProfilePage(request):
    details = Company.objects.filter(user=request.user)
    if details:
        form = CompanyForm(instance=details[0])
    else:
        form = CompanyForm()
    if request.method == "POST":
        if details:
            form = CompanyForm(request.POST, request.FILES, instance=details[0])
        else:
            form = CompanyForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save(commit=False).user = request.user
            form.save()
            return redirect("company-profile")
    context = {"details": details[0], "form": form}
    return render(request, "tracker/company/profile.html", context)



def RegisterPage(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        if form.is_valid():
            user = form.save()
            user.is_student = True
            user.save()
            messages.success(request, "Account was created for " + form.cleaned_data.get("username"))
            Student.objects.create(user=user, email=email, first_name=first_name, last_name=last_name)
            return redirect("login")
        else:
            messages.error(request, "Error creating account, make sure the credentials are correct or it's secure enough.")

    context = {"form": form}
    return render(request, "tracker/register.html", context)

@login_required(login_url="login")
def RegisterPage2(request):
    details = Student.objects.filter(user=request.user)
    if details:
        form = ProfileForm(instance=details[0])
        print(form)
    else:
        form = ProfileForm()
    if details:
        context = {"details": details[0], "form": form}
    else:
        context = {"details": details, "form": form}
    if request.method == "POST":
        if details:
            form = ProfileForm(request.POST, request.FILES, instance=details[0])
            print(form)
        else:
            form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save(commit=False).user = request.user
            form.save(commit=False).is_first_time = True
            user = form.save()
            user.is_student = True
            user.save()
            return redirect("student-info")
    return render(request, "tracker/register2.html", context)

@login_required(login_url="login")
def RegisterPage3(request):
    details = Student.objects.filter(user=request.user)
    if details:
        form = ProfileForm(instance=details[0])
    else:
        form = ProfileForm()
    if details:
        context = {"details": details[0], "form": form}
    else:
        context = {"details": details, "form": form}
    if request.method == "POST":
        if details:
            form = ProfileForm(request.POST, request.FILES, instance=details[0])
        else:
            form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save(commit=False).user = request.user
            form.save(commit=False).is_first_time = False
            user = form.save()
            user.is_student = True
            user.save()
            return redirect("landing")
    return render(request, "tracker/register3.html", context)


@login_required(login_url="login")
def RegisterPage4(request):
    details = Student.objects.filter(user=request.user)
    if details:
        form = ProfileForm(instance=details[0])
        print(form)
    else:
        form = ProfileForm()
    if details:
        context = {"details": details[0], "form": form}
    else:
        context = {"details": details, "form": form}
    if request.method == "POST":
        if details:
            form = ProfileForm(request.POST, request.FILES, instance=details[0])
            print(form)
        else:
            form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save(commit=False).user = request.user
            form.save(commit=False).is_first_time = False
            user = form.save()
            user.is_student = True
            user.save()
            return redirect("landing")
    return render(request, "tracker/register4.html", context)

@login_required(login_url="login")
def PendingPage(request):
    return render(request, "tracker/pending.html")

@login_required(login_url="login")
def FilesPage(request):
    return render(request, "tracker/files_to_download.html")

def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_student:
                login(request, user)
                return redirect("landing")
            else:
                login(request, user)
                return redirect("company")
        else:
            messages.info(request, "Username or password is incorrect")

    return render(request, "tracker/login.html")

def LogoutPage(request):
    logout(request)
    return redirect("login")