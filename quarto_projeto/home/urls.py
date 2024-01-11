from django.urls import path
from .views import meu_home

urlpatterns = [
    path('', meu_home ),
]