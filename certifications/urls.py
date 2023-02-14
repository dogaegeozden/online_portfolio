# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import certifications

# URL PATTERNS
urlpatterns = [
    path('certifications/', certifications, name="certifications"),
]
