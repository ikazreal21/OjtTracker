from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import locale
import uuid

from django.core.files.storage import FileSystemStorage
from django.db import models


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    step1 = models.BooleanField(default=False)
    step2 = models.BooleanField(default=False)
    step3 = models.BooleanField(default=False)
    step4 = models.BooleanField(default=False)
    step5 = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name + "-" + self.step1 + "-" + self.step2 + "-" + self.step3 + "-" + self.step4 + "-" + self.step5

class Step1(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    swep = models.FileField(upload_to="uploads/tracker", null=True, blank=True)
    notarizewaiver = models.FileField(upload_to="uploads/tracker", null=True, blank=True)
    notarizepracticum = models.FileField(upload_to="uploads/tracker", null=True, blank=True)
    resume = models.FileField(upload_to="uploads/tracker", null=True, blank=True)
    transcript = models.FileField(upload_to="uploads/tracker", null=True, blank=True)
    medical = models.FileField(upload_to="uploads/tracker", null=True, blank=True)

    class Meta:  
        verbose_name_plural = 'Step 1'

    def __str__(self):
        return f"{self.student}"
    

    
class Step2(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    recomentation_name = models.CharField(max_length=100)
    
    class Meta:  
        verbose_name_plural = 'Step 2'

    def __str__(self):
        return self.student + "-" + self.company_name
