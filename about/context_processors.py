from .models import *


def aboutus(request):
    about = About.objects.first()
    
    return dict(about=about)