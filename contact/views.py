# LIBRARIES
from django.shortcuts import render, get_object_or_404
from contact.models import MetaDescription, ContactPPic, Message, ContactPageVisit
from django.http import HttpResponseRedirect
import json, urllib
# FORMS
from .forms import MessageForm
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent
# Importing the validators.
from django.core.validators import FileExtensionValidator
from custom_validators.validators import validate_file_size
# PYTHON MODULES
from logging import basicConfig, DEBUG, debug, disable, CRITICAL

# Doing the basic configuration for the debugging feature
basicConfig(filename='contact_app_log.txt', level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# VIEW FUNCTIONS
def contact(request):
    """A view function to render contact page of the online portfolio application"""

    # Creating a query set from all the objects that are created with ContactPic data class.
    all_contact_page_picture_obj = ContactPPic.objects.all()

    # Creating a query set from all the MetaDescription objects.
    all_meta_description_objs = MetaDescription.objects.all()

    # Getting the user's ip address.
    ip = get_ip(request)

    # Getting the user's user agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the ContactPageVisit class.
    ContactPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Creating an empty form.
    contact_form = MessageForm()

    # Checking if the request method is POST and the msgSendBtn is used to send the post request.  
    if request.method == "POST" and 'msgSendBtn' in request.POST:

        # Filling the contact form with the information received from the post request
        contact_form = MessageForm(request.POST)

        # Checking if the form is valid
        if contact_form.is_valid(): # check if the data is good

            # Printing form data.
            print(contact_form.cleaned_data)

            # Creating an object in the databaser using the Message data class.
            Message.objects.create(ip_address=ip, user_agent=user_agent, **contact_form.cleaned_data,)

            # Clearing the form.
            contact_form = MessageForm()

            # Redirecting the user to contact page.
            return HttpResponseRedirect("/contact/")

        # Checking if the form is not valid.
        else:
            # Logging the errors in debug mode to contact_app_log.txt file.
            debug(contact_form.errors)

    # Creating context from the objects in the database and from the forms to be able to use them in the template.
    context = {
        "all_meta_description_objs": all_meta_description_objs,
        "all_contact_page_picture_obj": all_contact_page_picture_obj,
    }

    # Rendering the request, html page and the context.
    return render(request, 'contact/contact.html', context=context)
