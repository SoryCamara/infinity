from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Redacteur")
    profile = models.ImageField(upload_to="profil")
    bio = models.TextField()
    
    
    def __str__(self):
        return f" {self.user.username} "