from django.urls import path
from .views import home
from .contact import contact_submit  # Correct import from contact.py

urlpatterns = [
    path('', home),
    path('contact/', contact_submit),
]
