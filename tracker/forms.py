from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import ModelForm, ValidationError
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['step1', 'step2', 'step3', 'step4', 'step5']

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class Step1Form(ModelForm):
    class Meta:
        model = Step1
        fields = '__all__'

class Step2Form(ModelForm):
    class Meta:
        model = Step2
        fields = '__all__'