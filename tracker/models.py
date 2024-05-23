from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import locale
import uuid

from django.core.files.storage import FileSystemStorage
from django.db import models


class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)

class Company(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    recommendation_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    # Perosnal Info
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    adddress = models.CharField(max_length=100, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    # Student Info
    student_id = models.CharField(max_length=100, null=True, blank=True)
    adviser = models.CharField(max_length=100, null=True, blank=True)
    hours = models.CharField(max_length=100, null=True, blank=True)
    year_level = models.CharField(max_length=100, null=True, blank=True)
    semester = models.CharField(max_length=100, null=True, blank=True)
    # Job Info
    postition = models.CharField(max_length=100, null=True, blank=True)
    starting_date = models.DateField(null=True, blank=True)
    resume = models.FileField(upload_to="uploads/resume", null=True, blank=True)
    company_name = models.CharField(max_length=100, null=True, blank=True)


    is_approve = models.BooleanField(default=False)
    is_first_time = models.BooleanField(default=True)

    # OJT Requirements
    date_created = models.DateTimeField(auto_now_add=True)
    step1 = models.BooleanField(default=False)
    step2 = models.BooleanField(default=False)
    step3 = models.BooleanField(default=False)
    step4 = models.BooleanField(default=False)
    step5 = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}-{self.step1}-{self.step2}-{self.step3}-{self.step4}-{self.step5}"
    
    def starting_dates(self):
        return self.starting_date.strftime("%B %d, %Y")

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
