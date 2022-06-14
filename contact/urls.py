from django.urls import path
from .views import *

app_name = 'contact'

urlpatterns = [
    # path('me/', ContactView.as_view() , name="me"),
    path('me/', get_in_touch, name="me"),
    
]
