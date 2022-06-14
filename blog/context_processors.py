from .models import Hero, Logo

def hero_section(request):
    main = Hero.objects.first()
    logo = Logo.objects.first()
    
    return dict(main=main, logo=logo)