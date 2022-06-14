from django.urls import path
from . import views 

app_name = 'game'

urlpatterns = [
    path('', views.list_game, name='liste'),
]
