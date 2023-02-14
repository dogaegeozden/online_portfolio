# LIBRARIES
from django.urls import path
# VIEW FUNCTIONS
from .views import resumes

# URL PATTERNS
urlpatterns = [
    path('resumes/', resumes, name="resumes"),
]
