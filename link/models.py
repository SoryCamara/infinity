from django.db import models

# Create your models here.
class Media(models.Model):
    intro = models.CharField(max_length=255, verbose_name="Text", default="Infinity Media")
    fb_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    
    
    def __str__(self):
        return f" {self.fb_link} "