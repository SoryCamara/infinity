from tkinter.tix import Tree
from turtle import width
from django import forms
from django.http import HttpResponse
from pkg_resources import require
from .models import GetInTouch
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Nom", required='required', widget=forms.TextInput(attrs={
        'placeholder': 'Votre nom',
        'class': 'contact-input',
        'id': '1',
        'name' : 'name',
    }))

    email = forms.EmailField(label="Email", required='required', widget=forms.EmailInput(attrs={
        'placeholder':'Votre adresse email',
        'class': 'contact-input',
        'id': '2',
        'name': 'email'
    }))
    
    content = forms.CharField(label="Message", required='required', widget=forms.Textarea(attrs={
        'placeholder': 'Votre message',
        'class': 'message',
        'id': '3',
        'name': 'message',
        
    }))
    
    def get_info(self):

        # Cleaned data
        cl_data = super().clean()

        name = cl_data.get('name').strip()
        from_email = cl_data.get('email')
        content = cl_data.get('content')
        # return HttpResponse(name)

        # msg = f'{name} with email {from_email} said:'
        # msg += cl_data.get('message')


        return name, from_email, content

    def send(self):

        name, from_email, content = self.get_info()

        send_mail(
            subject='Equipe Infinity Media',
            message=content,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[from_email, ]
        )
    
    class Meta:
        model = GetInTouch
        fields = ('name', 'email', 'content')