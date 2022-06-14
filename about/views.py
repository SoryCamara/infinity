from django.shortcuts import render

# Create your views here.
def about(request):
    
    template_name = 'layouts/about.html'
    context = {}
    
    return render(request, template_name, context)