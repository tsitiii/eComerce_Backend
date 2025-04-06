from django.contrib import admin
from django.core.checks import register
from .models import User


class CustomAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name',  'email']
    list_filter = ['email']
admin.site.register(User, CustomAdmin)