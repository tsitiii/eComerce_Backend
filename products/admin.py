from django.contrib import admin
from django.core.checks import register
from .models import *


admin.site.register(Product)
admin.site.register(Cart)
