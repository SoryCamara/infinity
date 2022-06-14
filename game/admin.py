from django.contrib import admin
from .models import *


@admin.register(Gaming)
class GamingAdmin(admin.ModelAdmin):
    list_display = ['game_title', 'game_categorie', 'timestamp']
    list_display_links = ['game_title']