from distutils.command.upload import upload
from django.db import models
from blog.models import Categorie


class Gaming(models.Model):
    game_categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, verbose_name='Categorie')
    game_title = models.CharField(max_length=255, verbose_name="Titre du jeu", unique=True)
    game_image = models.ImageField(upload_to='game', verbose_name="Image")
    timestamp = models.DateField(auto_now_add=True, verbose_name="Date de sortie")
    
    class Meta:
        verbose_name = 'Jeu'
        verbose_name_plural = 'Jeux'
        ordering = ['-timestamp']
        
    
    def __str__(self):
        return f"{self.game_title}" 
    