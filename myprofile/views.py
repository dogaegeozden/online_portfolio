# LIBRARIES
from django.shortcuts import render
# MODELS
from myprofile.models import MetaDescription, ProfilePic, Bio, ToolsOrLanguagesMainVisual, ToolOrLanguage, Activity, SocialMediaLinks, MainPageVisit, ActivityImageClick, ProfilePictureClick, ToolsAndLanguagesImageClick
# CUSTOM FUNCTIONS
from custom_functions.visitors_ip_address import get_ip
from custom_functions.visitors_user_agent import get_user_agent

# VIEW FUNCTIONS
def my_profile(request):
    """A view function to render the main page of the online portfolio"""

    # Creating a query set called all_meta_description_objs from all the objects that are created in the database with MetaDescription data class.
    all_meta_description_objs = MetaDescription.objects.all()

    # Creating a query set called all_profile_picture_objs from all the objects that are created in the database with ProfilePic data class.
    all_profile_picture_objs = ProfilePic.objects.all()

    # Creating a query set called all_bio_objs from all the objects that are created in the database with Bio data class.
    all_bio_objs = Bio.objects.all()

    # Creating a query set called all_tools_and_languages_main_visual_objs from all the objects that are created in the database with ToolsOrLanguagesMainVisual data class.
    all_tools_and_languages_main_visual_objs = ToolsOrLanguagesMainVisual.objects.all()

    # Creating a query set called all_tools_and_languages_objs from all the objects that are created in the database with ToolOrLanguage data class.
    all_tools_and_languages_objs = ToolOrLanguage.objects.all()

    # Creating a query set called all_activity_objs from all the objects that are created in the database with Activity data class.
    all_activity_objs = Activity.objects.all()

    # Getting the visitor's ip address.
    ip = get_ip(request)

    # Getting the visitor's user_agent.
    user_agent = get_user_agent(request)

    # Creating an object in the database using the MainPageVisit data model.
    MainPageVisit.objects.create(ip_address=ip, user_agent=user_agent)

    # Checking if the post request's id is equal to activity_image_choice_request
    if request.POST.get("id") == "activity_image_choice_request":
        # Creating an object in the database using the ActivityImageClick data model.
        ActivityImageClick.objects.create(activity_image_choice=request.POST.get("activityImageChoice"), ip_address=ip, user_agent=user_agent)

    # Checking if the post request's id is equal to profile_picture_choice_request
    if request.POST.get("id") == "profile_picture_choice_request":
        # Creating an object in the database using the ProfilePictureClick data model.
        ProfilePictureClick.objects.create(profile_picture_choice=request.POST.get("profilePictureChoice"), ip_address=ip, user_agent=user_agent)

    # Checking if the post request's id is equal to tools_and_languages_images_click_data_request
    if request.POST.get("id") == "tools_and_languages_images_click_data_request":
        # Creating an object in the database using the ToolsAndLanguagesImageClick data model
        ToolsAndLanguagesImageClick.objects.create(tools_and_languages_image_choice=request.POST.get("toolsAndLanguagesImageChoice"), ip_address=ip, user_agent=user_agent)

    # Creating a dictionary called context from key value pairs. 
    context = {
        'all_meta_description_objs': all_meta_description_objs,
        'all_profile_picture_objs': all_profile_picture_objs,
        'all_bio_objs': all_bio_objs,
        'all_tools_and_languages_main_visual_objs': all_tools_and_languages_main_visual_objs,
        'all_tools_and_languages_objs': all_tools_and_languages_objs,
        'all_activity_objs': all_activity_objs,
    }

    # Rendering the request, html page and context dictionary.
    return render(request, 'myprofile/home.html', context=context)
