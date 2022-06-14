from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    timestamp = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.email}"