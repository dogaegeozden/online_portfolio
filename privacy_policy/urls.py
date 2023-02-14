# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import privacy_policy

# URL PATTERNS
urlpatterns = [
    path('privacy-policy/', privacy_policy, name="privacy-policy"),
]
