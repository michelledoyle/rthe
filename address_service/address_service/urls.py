from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define the index view function to display a simple message
def index(request):
    return HttpResponse("Welcome to the Address Service API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('address/', include('address.urls')),  # Include address app URLs
    path('', index),  # Add a default route for the root URL
]
