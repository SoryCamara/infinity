from django.contrib import admin
from .models import GetInTouch



@admin.register(GetInTouch)
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    list_display_links = ['name', 'email']
