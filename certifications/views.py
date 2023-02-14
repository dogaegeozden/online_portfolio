# LIBRARIES
from django.shortcuts import render
# MODELS
from certifications.models import MetaDescription, Certification, CertificationPageVisit, CertificationClick
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

# VIEW FUNCTIONS
def certifications(request):
    """A view function which renders the certifications page."""

    # Creating a query set called all_meta_description_objs by selecting all the MetaDescription objects from the database.
    all_meta_description_objs = MetaDescription.objects.all()

    # Creating a query set called all_certification_objs by selecting all the Certification objects from the database.
    all_certification_objs = Certification.objects.all()

    # Getting the visitor's ip address.
    ip = get_ip(request)

    # Getting the user's user agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the CertificationPageVisit data model.
    CertificationPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Checking if the post request's id is equal to certchoinf.
    if request.POST.get("id") == "certchoinf": 

        # Creating an object in the database using the CertificationClick data model.
        CertificationClick.objects.create(ip_address=ip, user_agent=user_agent, certification_choice=request.POST.get("certificationChoice"))

    # Creating a dictionary called context which includes all the query sets that are created in this views file.
    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_certification_objs': all_certification_objs,
    }

    # Rendering the request, html page and the context.
    return render(request, 'certifications/certifications.html', context=context)
