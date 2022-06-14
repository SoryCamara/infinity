from distutils.command.upload import upload
from email.policy import default
from tabnanny import verbose
from django.db import models
from accounts.models import Profil
from django.utils.text import slugify
from tinymce import models as tinymce_models

class Categorie(models.Model):
    categorie = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True, max_length=255)
    timestamp = models.DateField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.categorie)
            
        super(Categorie, self).save(args, kwargs)

    class Meta:
        ordering = ['-timestamp']
    
    
    def __str__(self):
        return f" {self.categorie} "        
    


class Post(models.Model):
    STATUS_CHOICE = (
        ('publié', 'publié'),
        ('brouillon', 'brouillon')
    )
    cat = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Categorie')
    user = models.ForeignKey(Profil, on_delete=models.CASCADE, verbose_name="Editeur")
    title = models.CharField(max_length=255, verbose_name="Titre de l'article", unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    content = tinymce_models.HTMLField()
    post_image = models.ImageField(upload_to="post/article/", verbose_name="image")
    status = models.CharField(max_length=200, choices=STATUS_CHOICE)
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Date de redaction")
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            
        super(Post, self).save(args, kwargs)
        
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-timestamp']
        
    
    def __str__(self):
        return f" {self.title} "
        
    
    
class Hero(models.Model):
    title = models.CharField(max_length=255, default="Infinity Media")
    introduction = models.TextField()
    
    def __str__(self):
        return f" {self.title} "
    

class Logo(models.Model):
    text_alternatif = models.CharField(max_length=20)
    image = models.ImageField(upload_to="logo")
    
    def __str__(self):
        return f" {self.text_alternatif} "
    


class Direction(models.Model):
    name = models.CharField(max_length=200)
    role = models.TextField()
    image = models.ImageField(upload_to="partenaire/")
    
    class Meta:
        verbose_name = 'Direction'
        verbose_name_plural = 'Direction'
    
    
    def __str__(self):
        return f" {self.name} "
    
     
    
class Partnaire(models.Model):
    partenaire = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to="partenaire/")
    
    class Meta:
        verbose_name = 'Nos partenaires'
        verbose_name_plural = 'Nos partenaires'
    
    
    def __str__(self):
        return f" {self.partenaire} "