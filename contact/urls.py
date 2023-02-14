# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import contact

# URL PATTERS
urlpatterns = [
    path('contact/', contact, name="contact"),
]
