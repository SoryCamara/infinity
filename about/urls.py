from django.urls import path
from . import views 

app_name = 'about'

urlpatterns = [
    path('us/', views.about, name='us'),
]
