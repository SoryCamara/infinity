
from django.shortcuts import render, redirect
from .forms import NewsletterForm
from django.contrib import messages
from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
# from .forms import EmailSignupForm
from .models import Newsletter

from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError

import json
import requests

api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID

from django.shortcuts import render
from django.contrib import messages



from django.shortcuts import render
from django.contrib import messages

from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# Subscription Logic
def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))




# Views here.
def subscription(request):
    if request.method == "POST":
        email = request.POST['email']
        subscribe(email)                    # function to access mailchimp
        messages.success(request, "Email reçu. Merci de votre inscription! ") # message

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))






































# Create your views here.

# Subscription Logic
# def subscribe(email):

#     mailchimp = Client()
#     mailchimp.set_config({
#         "api_key": api_key,
#         "server": server,
#     })

#     member_info = {
#         "email_address": email,
#         "status": "subscribed",
#     }

#     try:
#         response = mailchimp.lists.add_list_member(list_id, member_info)
#         print("response: {}".format(response))
#     except ApiClientError as error:
#         print("An exception occurred: {}".format(error.text))



# def subscription(request):
#     # form = EmailSignupForm(request.POST or None)
#     if request.method == "POST":
#         # if form.is_valid():
#         email = request.POST['email']
#         new_email = Newsletter()
#         new_email.email = email 
#         new_email.save()
        
#         # email_signup_qs = Newsletter.objects.filter(email=email)
#         # if email_signup_qs.exists():
#         #     messages.warning(request, "Vous avez déjà souscrit(e) à la newsletter")
#         # else:
#         #     subscribe(email)
#         #     messages.info(request, "Merci d'avoir souscrit(e) à la newsletter")
#         #     new_mail.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


























# # Mailchimp Settings
# api_key = settings.MAILCHIMP_API_KEY
# server = settings.MAILCHIMP_DATA_CENTER
# list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# # Subscription Logic
# def subscribe(email):

#     mailchimp = Client()
#     mailchimp.set_config({
#         "api_key": api_key,
#         "server": server,
#     })

#     member_info = {
#         "email_address": email,
#         "status": "subscribed",
#     }

#     try:
#         response = mailchimp.lists.add_list_member(list_id, member_info)
#         print("response: {}".format(response))
#     except ApiClientError as error:
#         print("An exception occurred: {}".format(error.text))




# # Views here.
# def subscription(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         qs = Newsletter.objects.filter(email=email)
#         if qs.exists():
#             messages.error(request, 'Vous êtes deja inscrit(e)')
            
#         subscribe(email)  # function to access mailchimp
#         Newsletter.objects.create(email=email)
#         messages.success(request, "Email received. thank You! ") # message
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

