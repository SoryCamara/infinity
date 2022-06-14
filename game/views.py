from re import template
from django.shortcuts import render
from .models import Gaming
from django.core.paginator import Paginator

def list_game(request):
    games = Gaming.objects.all().order_by('id')
    paginator = Paginator(games, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'layouts/game.html'
    context = {
        'page_obj': page_obj
    }
    
    return render(request, template_name, context)