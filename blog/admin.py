from django.contrib import admin
from .models import *


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['categorie', 'timestamp']
    list_display_links = ['categorie', 'timestamp']
    
    


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'cat', 'user', 'timestamp']
    list_display_links = ['title']



@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    
    


@admin.register(Logo)
class logoAdmin(admin.ModelAdmin):
    list_display = ['text_alternatif']
    list_display_links = ['text_alternatif']
    
    

@admin.register(Partnaire)
class partenaireAdmin(admin.ModelAdmin):
    list_display = ['partenaire']
    list_display_links = ['partenaire']
    
    


@admin.register(Direction)
class partenaireAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']