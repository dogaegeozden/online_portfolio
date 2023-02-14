"""Online_Portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# LIBRARIES
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

# URL PATTERNS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myprofile.urls')),
    path('', include('works.urls')),
    path('', include('resumes.urls')),
    path('', include('certifications.urls')),
    path('', include('blog.urls')),
    path('', include('contact.urls')),
    path('', include('privacy_policy.urls')),
    path('', include('terms_and_conditions.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Activate the debug tool bar if debug is True in the settings.py
if settings.DEBUG == True:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
