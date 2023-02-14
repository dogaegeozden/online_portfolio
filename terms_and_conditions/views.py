# LIBRARIES
from django.shortcuts import render
# MODELS
from terms_and_conditions.models import MetaDescription, TermsAndConditionsPageVisit
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

# Create your views here.

def termsAndConditions(request):
    """A view function for the terms and conditions page of the online portfolio application"""

    # Creating a query set called all_meta_description_objs by selecting all the objects from the database which are created with the MetaDescription data class.
    all_meta_description_objs = MetaDescription.objects.all()

    # Getting the visitor's ip address.
    ip = get_ip(request)

    # Getting the visitor's user agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the TermsAndConditionsPageVisit data class.
    TermsAndConditionsPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Creating a dictionary called context.
    context = {
        'all_meta_description_objs': all_meta_description_objs,
    }

    # Rendering the request, html page and the context
    return render(request, 'terms_and_conditions/terms_and_conditions.html', context)
