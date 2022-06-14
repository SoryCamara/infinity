from django.db import models

# Create your models here.


# def get_in_touch(request):
#     name = 

class GetInTouch(models.Model):
    name = models.CharField(max_length=255, verbose_name="Votre nom")
    email = models.EmailField(max_length=255, verbose_name="Votre adresse email")
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True, verbose_name="Date")
    
    def __str__(self):
        return f" {self.name} "