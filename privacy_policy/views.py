# LIBRARIES
from django.shortcuts import render
# MODELS
from .models import MetaDescription, PrivacyPolicyPageVisit
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

def privacy_policy(request):
    """A view function which renders the privacy policy page."""

    # Creating a query set called all_meta_description_objs 
    all_meta_description_objs = MetaDescription.objects.all()

    # Getting the visitor's ip address.
    ip = get_ip(request)

    # Getting the visitor's user agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the PrivacyPolicyPageVisit data model.
    PrivacyPolicyPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Creating dictionary called context from key value pairs.
    context = {
        'all_meta_description_objs': all_meta_description_objs,
    }

    # Rendering the request, html page and the context dictionary.
    return render(request, 'privacy_policy/privacy_policy.html', context=context)
