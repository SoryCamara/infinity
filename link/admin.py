from django.contrib import admin
from .models import *

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['fb_link']
    list_display_links = ['fb_link']