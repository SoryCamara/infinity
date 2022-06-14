from .models import Newsletter
from django import forms

class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(
        label = '',
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Votre adresse email',
            'name': 'email',
            'id': 'email',
            'class': 'newsletter-input'
        })
    )
    
    class Meta:
        model = Newsletter
        fields = ('email', )