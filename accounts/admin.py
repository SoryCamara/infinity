from django.contrib import admin
from .models import *


@admin.register(Profil)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ['user']
