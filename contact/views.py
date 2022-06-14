from re import template
from django.shortcuts import render
from .models import GetInTouch
from .forms import ContactForm
from django.core.mail import send_mail

from django.core.mail import send_mail
from django.conf import settings

from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.urls import reverse_lazy



from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect



class ContactView(FormView):
    template_name = 'layouts/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:me')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)



def send_email(request):
    subject = request.POST.get('name', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')


# Create your views here.
def get_in_touch(request):
    
    form = ContactForm()
    
    if request.method == "POST":

        form = ContactForm(request.POST)
        contact = None
        if form.is_valid():
            contact = GetInTouch.objects.create(**form.cleaned_data)
        
        contact.save()
        
        # send_mail(    
        #     subject="L'equipe Infinity Media",
        #     message='Nous vous remercions d\'avoir pris contact avec notre équipe',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[settings.RECIPIENT_ADDRESS]
        # )
        form = ContactForm()
        
    # print(form)
    
    template_name = 'layouts/contact.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

# 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
# git push https://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@github.com/SoryCamara/infinity.git
