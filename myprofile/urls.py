# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import my_profile

# URL PATTERS
urlpatterns = [
    path('', my_profile, name="home"),
]
