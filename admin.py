from django.contrib import admin
from .models import registertable
# Register your models here.

class showuser(admin.ModelAdmin):
    list_display = ["name","email","phone","password"]

admin.site.register(registertable,showuser)