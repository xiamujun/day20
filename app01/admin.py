from django.contrib import admin

# Register your models here.
from .models import Business,Host
admin.site.register(Business)
admin.site.register(Host)