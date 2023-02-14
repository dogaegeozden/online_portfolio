# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import termsAndConditions

# URL PATTERNS
urlpatterns = [
    path('terms-and-conditions/', termsAndConditions, name="terms-and-conditions"),
]
