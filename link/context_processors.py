from .models import *

def social(request):
    media = Media.objects.first()
    return dict(media=media)