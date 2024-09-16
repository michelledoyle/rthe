# address/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_or_update_address, name='create_or_update_address'),
]