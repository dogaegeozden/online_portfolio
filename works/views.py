# LIBRARIES
from django.shortcuts import render
from django import template
# MODELS
from works.models import MetaDescription, GraphicDesign, WebDevelopment, WorksPageVisit, GraphicDesignProjClickData, WebDevProjClickData
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

# VIEW FUNCTIONS
def works(request):
    """A view function for the works page of the online portfolio application"""

    # Creating a query set called all_meta_description_objs by selecting all the objects in the database that created with the MetaDescription data class.
    all_meta_description_objs = MetaDescription.objects.all()

    # Creating a query set called all_graphic_design_objs by selecting all the objects in the database that created with the GraphicDesign data class.
    all_graphic_design_objs = GraphicDesign.objects.all()

    # Creating a variable called number_of_graphic_design_objs by counting the total number of object in the database that created with the GraphicDesign data class.
    number_of_graphic_design_objs = GraphicDesign.objects.count()

    # Creating a query set called all_web_development_objs by selecting all the object that created with the WebDevelopment data model from the database.
    all_web_development_objs = WebDevelopment.objects.all()

    # Getting visitor's ip address.
    ip = get_ip(request)

    # Getting the visitor's user agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the WorksPageVisit data class.
    WorksPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Checking if the post request's requestID is equal to graphic_design_project_click_data
    if request.POST.get("requestID") == "graphic_design_project_click_data":
        # Creating an object in the database using the GraphicDesignProjClickData
        GraphicDesignProjClickData.objects.create(project_choice=request.POST.get("projectChoice"), ip_address=ip, user_agent=user_agent)

    # Checking if the post request's requestID is equal to web_development_project_link_click_data
    if request.POST.get("requestID") == "web_development_project_link_click_data":
        # Creating an object in the database using the WebDevProjClickData
        WebDevProjClickData.objects.create(project_choice=request.POST.get("projectChoice"), ip_address=ip, user_agent=user_agent)

    # Creating a dictionaryh called context with key value pairs 
    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_graphic_design_objs': all_graphic_design_objs,
        'number_of_graphic_design_objs': number_of_graphic_design_objs,
        'all_web_development_objs': all_web_development_objs,
    }

    # Rendering the request, html page and the context.
    return render(request, 'works/works.html', context=context)
