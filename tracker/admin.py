from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
from django.contrib.auth.models import Group
# from admin_interface.models import Theme

class UserAdminConfig(UserAdmin):
    model = CustomUser
    search_fields = ('username', 'email')
    list_filter = ('first_name', 'is_active', 'is_staff', 'is_student')
    list_display = ('username', 'id', 'email','is_active', 'is_staff', 'is_student')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_student')}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})}
    }
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'username',
                    'email',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_student',
                ),
            },
        ),
    )


admin.site.unregister(Group)
admin.site.register(CustomUser, UserAdminConfig)
admin.site.register(Student)
admin.site.register(Step1)
admin.site.register(Step2)
# admin.site.register(Step3)
# admin.site.register(Step4)
# admin.site.register(Step5)


admin.site.site_header = "CIMS Admin"
admin.site.site_title = "CBA Internship Management System Admin Portal"
admin.site.index_title = "Welcome to CBA Internship Management System Admin Portal"


