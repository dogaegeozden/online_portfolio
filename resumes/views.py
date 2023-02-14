# LIBRARIES
from django.shortcuts import render
# MODELS
from resumes.models import MetaDescription, AboutCurrentPosition, Experience, Education, Resume, ResumePageVisit, ResumeFileClicks
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

def resumes(request):
    """A view function for the resumes page of the online portfolio application"""

    # Creating a query set from all the objects that are created in the database with the MetaDescription data model.
    all_meta_description = MetaDescription.objects.all()

    # Creating a query set from all the objects that are created in the database with the AboutCurrentPosition data model.
    all_about_current_position_objs = AboutCurrentPosition.objects.all()

    # Creating a query set from all the objects that are created in the database with the Experince data model.
    all_experience_objs = Experience.objects.all()

    # Creating a query set from all the objects that are created in the database with the Education data model.
    all_education_objs = Education.objects.all()

    # Creating a query set from all the objects that are created in the database with the Resume data model.
    all_resume_objs = Resume.objects.all()

    # Getting the visitor's ip address.
    ip = get_ip(request)

    # Getting the visitor's user agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the ResumePageVisit model
    ResumePageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Checking if the post request's id is equal to resume_choice_request
    if request.POST.get("id") == "resume_choice_request":
        # Creating an object in the database using the ResumeFileClicks data model.
        ResumeFileClicks.objects.create(resume_choice=request.POST.get("resumeChoice"), ip_address=ip, user_agent=user_agent)

    # Creating a dictionary called context from the key value pairs.
    context = {
        'all_meta_description': all_meta_description,
        'all_about_current_position_objs': all_about_current_position_objs,
        'all_experience_objs': all_experience_objs,
        'all_education_objs': all_education_objs,
        'all_resume_objs': all_resume_objs,
    }

    # Rendering the request, html page and the context dictionary.
    return render(request, 'resumes/resumes.html', context=context)
