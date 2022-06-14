from re import template
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'layouts/blog.html'
    context = {
        'page_obj': page_obj
    }
    
    
    return render(request, template_name, context)