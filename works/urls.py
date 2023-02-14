# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import works

# URL PATTERN
urlpatterns = [
    path('works/', works, name="works"),
]
