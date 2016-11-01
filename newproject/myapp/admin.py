from django.contrib import admin

# Register your models here.
from .models import Result

class ResultsAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'password', 'email']

admin.site.register(Result, ResultsAdmin);
