from re import template
from django.shortcuts import render 
from django.http import HttpResponse
from blog.models import *
from accounts.models import Profil
from game.models import Gaming

def index(request):
    
    posts = Post.objects.filter(status='publié')[:4]
    direction = Direction.objects.order_by('-id')[:3]
    partenaires = Partnaire.objects.order_by('-id')[:4]
    games = Gaming.objects.all()[:8]
    authors = Profil.objects.all()[:2]
    
    template_name = 'layouts/index.html'
    context = {
        'posts': posts,
        'authors': authors,
        'games': games,
        'direction': direction,
        'partenaires': partenaires,
    }
    
    return render(request, template_name, context)